import {fail, redirect} from "@sveltejs/kit";
import type {Actions, PageServerLoad} from "./$types";
import {auth} from '$lib/stores/auth';
import { hash } from '@node-rs/argon2';


export const load: PageServerLoad = async (event) => {
    if(event.locals.user) {
        return redirect(302, '/')
    }
    return{};
}

export const actions: Actions = {
    login: async (event) => {
        const formData = await event.request.formData();
        const email = formData.get('email') as string;
        const password = formData.get('password') as string;

				const res	= await auth.login(email, password)

				return redirect(302, '/');
    },

		register: async(event) => {
			return redirect(302, '/login/register');
		}
}