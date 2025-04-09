import type { Handle } from '@sveltejs/kit';
import {auth} from '$lib/stores/auth.js';

const handleAuth: Handle = async ({ event, resolve }) => {
	const authStore = auth
	const sessionToken = event.cookies.get(authStore.sessionCookieName);

	if (!sessionToken) {
		event.locals.user = null;
		event.locals.session = null;
		return resolve(event);
	}

	const { session, user } = await authStore.validateSessionToken(sessionToken);

	if (session) {
		await authStore.setSessionTokenCookie(event, sessionToken, session.expiresAt);
	} else {
		await authStore.deleteSessionTokenCookie(event);
	}

	console.log(user)
	event.locals.user = user;
	event.locals.session = session;
	return resolve(event);
};

export const handle: Handle = handleAuth;