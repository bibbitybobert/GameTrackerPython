import {writable} from 'svelte/store';
import { encodeHexLowerCase } from '@oslojs/encoding';
import { sha256 } from '@oslojs/crypto/sha2';
import { redirect } from '@sveltejs/kit';

type AuthStore = {
    token: string | null;
    isAuthenticated: boolean;
    login: (email: string, password: string) => Promise<void>;
    register: (fName: string, lName:string, email:string, passwordHash:string) => Promise<void>;
    logout: () => void;
    sessionCookieName: string;
    validateSessionToken: (sessionToken: string) => Promise<{session: any, user: any}>
    setSessionTokenCookie: (event: any, sessionToken: string, expiresAt: Date) => Promise<void>;
    deleteSessionTokenCookie: (event: any) => Promise<void>;
}

const DAY_IN_MS = 1000 * 60 * 60 * 24;

const createAuthStore = (): AuthStore => {
    const tokenStore = writable<string| null>(null);
    const isAuthenticatedStore = writable(false);
    const sessionCookieName = 'auth-session';

    let token: string | null = null;

    tokenStore.subscribe((value) => {
        token = value;
        isAuthenticatedStore.set(!!value);
    });

    return {
        sessionCookieName: '',
        token: null,
        isAuthenticated: false,

        login: async(email: string, password: string) => {
            const res = await fetch('http://localhost:5000/users/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({email, password}),
            });

            const data = await res.json();

            if(res.ok && data.sessionToken){
                tokenStore.set(data.sessionToken);
            }else{
                throw new Error(data.message || 'Login Failed');
            }
        },

        register: async(fName: string, lName: string, email:string, password:string) => {
            console.log(`fName: ${fName}, lName: ${lName}, email: ${email}, pass: ${password}`)
            const res = await fetch('http://localhost:5000/users/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({fName, lName, email, password}),
            });

            debugger;
            const data = await res.json();
            console.log(data)
            console.log(`${res.ok}, ${data.sessionToken}, ${res.ok && data.sessionToken}`)

            if(res.ok && data.sessionToken){
                tokenStore.set(data.sessionToken);
                return redirect(302, '/')
            }else{
                throw new Error(data.message || 'Error creating new user');
            }
        },

        logout: () => {
            tokenStore.set(null);
        },

        validateSessionToken: async (sessionToken: string) => {
            const sessionId = encodeHexLowerCase(sha256(new TextEncoder().encode(sessionToken)));
            const res = await fetch('http://localhost:5000/users/validateSessionToken',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({sessionToken}),
            });

            const data = await res.json();

            if(!res.ok || !data.user || !data.session){
                return {session: null, user: null};
            }

            const {session, user} = data;


            const sessionExpired = Date.now() >= session.expiresAt.getTime();
            if(sessionExpired){
                const deleteRes = await fetch(`http://localhost:5000/user/remove/${session.id}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                if(!deleteRes.ok){
                    throw new Error(await deleteRes.json() || "Error deleting session");
                }

                return {session: null, user: null};
            }

            const renewSession = Date.now() >= session.expiresAt.getTime() - DAY_IN_MS /2;
            if(renewSession){
                const renewRes = await fetch(`http://localhost:5000/user/renew/${session.id}`,{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                if(!renewRes.ok){
                    throw new Error(await renewRes.json() || "Error renewing session");
                }
            }
            return {session, user};

        },

        setSessionTokenCookie: async (event: any, sessionToken: string, expiresAt: Date) => {
            event.cookies.set(sessionCookieName, sessionToken, {
                expires: expiresAt,
                path: '/'
            });
        },

        deleteSessionTokenCookie: async (event: any) => {
            event.cookies.delete(sessionCookieName, {
                path: '/'
            });
        }
    }
}

export const auth = createAuthStore()