<template>
<div>
	<div class="card">
		<Menubar :model="items"/>
	</div>
</div>
</template>

<script setup lang="ts">
import Menubar from 'primevue/menubar';
import 'primeicons/primeicons.css';
import { onMounted, ref } from 'vue';
import router from '@/router';
import {logout} from '@/DataAccess/userDataAccess.ts';

const homeRedirect = async () => {
	await router.push('/');
}

const aboutRedirect = async () => {
	await router.push('/about');
}

const addGameRedirect = async () => {
	await router.push('/new/game');
}

const addLauncherRedirect = async () => {
	await router.push('/new/launcher');
}

const addTagRedirect = async () => {
	await router.push('/new/tag');
}

const logoutRedirect = async () => {
	const response = await logout();
	await router.push('/login');
}

const items = ref([
	{
		label: 'Home',
		icon: 'pi pi-home',
		command: homeRedirect
	},
	{
		label: 'About',
		icon: 'pi pi-info-circle',
		command: aboutRedirect
	},
	{
		label: 'Add',
		icon: 'pi pi-plus-circle',
		items: [
			{
				label: 'New Game',
				icon: 'pi pi-desktop',
				command: addGameRedirect
			},
			{
				label: 'New Launcher',
				icon: 'pi pi-shop',
				command: addLauncherRedirect
			},
			{
				label: 'New Tag',
				icon: 'pi pi-tag',
				command: addTagRedirect
			},

		]
	},
	{
		label: 'Logout',
		icon: 'pi pi-sign-out',
		command: logoutRedirect
	}
]);
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
</style>