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
    register: async (event) => {
        const formData = await event.request.formData();
        const fName = formData.get('fName') as string;
        const lName = formData.get('lName') as string;
				const email = formData.get('email') as string;
				const password = formData.get('password') as string;
				const confirmPassword = formData.get('confirmPassword') as string;

				if(password != confirmPassword){
					return fail(400, {message: 'Passwords must match'});
				}

        await auth.register(fName, lName, email, password)
    },
}