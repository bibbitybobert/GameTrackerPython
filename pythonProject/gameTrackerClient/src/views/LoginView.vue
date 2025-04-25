<template>
	<form @submit.prevent="OnSubmit">
    <div
        class="px-6 py-20 md:px-12 lg:px-20 flex items-center justify-center bg-[linear-gradient(-225deg,var(--p-primary-500),var(--p-primary-700)_48%,var(--p-primary-800))] dark:bg-[linear-gradient(-225deg,var(--p-primary-400),var(--p-primary-600)_48%,var(--p-primary-800))]"
		>
        <div class="p-12 shadow text-center lg:w-[30rem] backdrop-blur-md rounded-xl bg-[rgba(255,255,255,0.1)]" id="loginBox">
					<Toast />
            <div class="text-4xl font-medium mb-12 text-primary-contrast">Welcome</div>
						<div>
            <InputText
                type="email"
                class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !block !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
                placeholder="Email"
								v-model="email"
								required
            />
						</div>
					<div>
            <Password
                class="!appearance-none placeholder:!text-primary-contrast/40 !border-0 !p-4 !w-full !outline-0 !text-xl !mb-6 !bg-white/10 !text-primary-contrast/70 !rounded-full"
                placeholder="Password"
								v-model="password"
								required
								toggle-mask
								:feedback="false"
            />
					</div>
					<div>
            <button
                type="submit"
                class="max-w-40 w-full rounded-full appearance-none border-0 p-4 outline-0 text-xl mb-6 font-medium bg-white/30 hover:bg-white/40 active:bg-white/20 text-primary-contrast/80 cursor-pointer transition-colors duration-150"
						>
                Sign In
            </button>
					</div>
					<p>New to GameTracker? <router-link class="cursor-pointer font-medium block text-center text-primary-contrast" to="/register">Register</router-link></p>
        </div>
    </div>
	</form>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import {loginUser} from '@/DataAccess/userDataAccess.ts';
import { useField, useForm } from 'vee-validate';
import {useRoute} from 'vue-router';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { useToast } from 'primevue/usetoast';
import router from '@/router';
import Password from 'primevue/password';
import { Toast } from 'primevue';

const checked1 = ref(true);


const {value: email} = useField('email');
const {value: password} = useField('password');

const toast = useToast();

const OnSubmit = async () => {
	const response = await loginUser(email.value, password.value);
	if(response == localStorage.getItem('user')){
		console.log('toast');
		// toast.add({
		// 	severity: 'success',
		// 	summary: 'Success!',
		// 	detail: 'Logged In Successfully',
		// 	life: 3000
		// });
		await router.push({path: '/'});
	}
	else{
		toast.add({
			severity: 'error',
			summary: 'Error',
			detail: 'Unable to Log you in with those credentials',
			life: 3000
		});
	}

}

onMounted(() =>{
	const route = useRoute();
})
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
#loginBox{
	align-self: center;
	text-align: center;
	width: 50%;
}

button{
	align-self: center;
	width: fit-content;
}
</style>