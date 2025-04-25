<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from '@/components/Header.vue';
import {useRoute} from 'vue-router';
import { onMounted } from 'vue';
import router from '@/router';

const route = useRoute();

onMounted(async () =>{
	const userId = localStorage.getItem("user");
	if(userId == "null"){
		await router.push('/login');
	}
});

</script>

<template>
	<Header v-if="!route.meta.hideNav"/>
  <RouterView />
</template>

<style>
RouterView{
	display: flex;
	flex-direction: column;
	align-content: center;
}
</style>
