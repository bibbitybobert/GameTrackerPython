

<template>
  <div>
		<Toast />
    <h1>Register</h1>
    <Form v-slot="$form" @submit="OnSubmit" id="registerBox" :resolver="resolver" :initialValues>
			<div class="nameInput">
				<InputText
						type="text"
						class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
						placeholder="First Name"
						v-model="firstName"
						required
				/>
				<Message v-if="$form.firstName?.invalid" severity="error" size="small" variant="simple">{{$form.firstName.error?.message}}</Message>
				<InputText
						type="text"
						class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
						placeholder="Last Name"
						v-model="lastName"
						required
				/>
			</div>
			<div>
				<InputText
						type="email"
						class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
						placeholder="Email"
						v-model="email"
						required
						id="email"
				/>
			</div>
			<div>
				<Password
						class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
						placeholder="Password"
						v-model="password"
						required
						id="password"
						:feedback="false"
						fluid
						toggle-mask>
				</Password>
				<template v-if="$form.password?.invalid">
					<Message v-for="(error, index) of $form.password.errors" :key="index" severity="error" size="small" variant="simple">{{error.message}}</Message>
				</template>
			</div>
			<div>
				<Password
						class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
						placeholder="Confirm Password"
						v-model="confirmPassword"
						required
						id="confirm"
						:feedback="false"
						toggle-mask
				/>
			</div>
      <button
                type="submit"
                class="max-w-40 w-full rounded-full appearance-none border-0 p-4 outline-0 text-xl mb-6 font-medium bg-white/30 hover:bg-white/40 active:bg-white/20 text-primary-contrast/80 cursor-pointer transition-colors duration-150"
						>
							Register
            </button>
    </Form>
    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script setup lang="ts">

import {InputText, Button, Password} from 'primevue';
import { useField } from 'vee-validate';
import {registerUser, getUserByEmail} from '@/DataAccess/userDataAccess.ts';
import router from '@/router';
import { useToast } from 'primevue/usetoast';
import {Form} from '@primevue/forms';
import {ref} from 'vue';
import { Message } from 'primevue';
import { Toast } from 'primevue';

const {value: firstName} = useField('firstName');
const {value: lastName} = useField('lastName');
const {value: email} = useField('email');
const {value: password} = useField('password');
const {value: confirmPassword} = useField('confirmPassword');

const toast = useToast();

const initialValues = ref({
	firstName: '',
	lastName: '',
	email: '',
	password: '',
	confirmPassword: ''
});

const resolver = ({values}) => {
	const errors = {
		firstName: [],
		lastName: [],
		email: [],
		password: [],
		confirmPassword: []
	};

	if(!values.firstName)
		errors.firstName.push({type: 'required', message: 'First Name is required'});
	if(!values.lastName)
		errors.lastName.push({type: 'required', message: 'Last name is required'});
	if(!values.email)
		errors.email.push({type: 'required', message:'Email is required'});
	if(!values.password)
		errors.password.push({type: 'required', message: 'Password is required'});
	if(!values.confirmPassword)
		errors.confirmPassword.push({type: 'required', message: 'Please enter password again'});

	if(values.password < 8)
		errors.password.push({type: 'minimum', message:'Password must be a minimum of 8 characters'});
	if(!/[a-z]/.test(values.password))
		errors.password.push({type: 'required', message: 'Password must contain a lower case letter'});
	if(!/[A-Z]/.test(values.password))
		errors.password.push({type: 'required', message: 'Password must contain an upper case letter'});
	if(!/[0-9]/.test(values.password))
		errors.password.push({type: 'required', message: 'Password must contain a number'});
	if(!/[!@#$%^&()\[\].,]/.test(values.password))
		errors.password.push({type: 'required', message: 'Password must contain a special character'});

	if(values.password && values.confirmPassword && values.password !== values.confirmPassword)
		errors.confirmPassword.push({type: 'required', message: 'Passwords must match.'});

	return {values, errors};

};

const OnSubmit = async () => {
	try {
		const emailInUseRes = await emailInUse();
		const passwordStrengthValid = checkPasswordStrength();
		const passwordsMatch = confirmPasswordMatch();
		if (emailInUseRes) {
			toast.add({
				severity: 'error',
				summary: 'Invalid Email',
				detail: 'There is already an account associated with this email.',
				life: 3000
			});
		} else if (!passwordStrengthValid) {

		} else if (!passwordsMatch) {
			toast.add({
				severity: 'error',
				summary: 'Invalid Password',
				detail: 'Passwords must match.',
				life: 3000
			});
		} else {
			const response = await registerUser(firstName.value, lastName.value, email.value, password.value);
			if (response == localStorage.getItem('user')) {
				await router.push({ path: '/' });
			}
			else {
				toast.add({
					severity: 'error',
					summary: 'Register Error',
					detail: 'Unable to register new user at this time.',
					life: 3000
				});
			}
		}
	}catch(err){
		console.error("registration error: ", err);
		toast.add({
			severity: 'error',
			summary: 'Registration Error',
			detail: 'An error occurred when attempting to register new user',
			life: 3000
		})
	}
}

const emailInUse = async () =>{
	const emailUser = await getUserByEmail(email.value);
	return !!emailUser;

}

const checkPasswordStrength = () => {
	if(!password.value){
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password is required',
			life: 3000
		});
		return false;
	}
	if(password.value.length < 8) {
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password must contain at least 8 characters.',
			life: 3000
		});
	}
	if(!/[a-z]/.test(password.value)){
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password must contain one lower case character.',
			life: 3000
		});
		return false;
	}
	if(!/[A-Z]/.test(password.value)){
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password must contain one upper case character.',
			life: 3000
		});
		return false;
	}
	if(!/\d/.test(password.value)){
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password must contain one number.',
			life: 3000
		});
		return false;
	}
	if(!/[!@#$%^&()\[\].,]/.test(password.value)){
		toast.add({
			severity: 'error',
			summary: 'Invalid Password',
			detail: 'Password must contain one special character.',
			life: 3000
		});
		return false;
	}
	return true;

}

const confirmPasswordMatch = () => {
	return (password.value === confirmPassword.value);
}
</script>

<style scoped>

div{
	display: flex;
	flex-direction: column;
	align-content: center;
}

h1{
	align-self: center;
}

form{
	text-align: center;
	width: 50%;
	align-self: center;
}

h1, p{
	text-align: center;
}

.nameInput{
	display: flex;
	flex-direction: row;
}

.nameInput input{
	width: 50%;
}

</style>