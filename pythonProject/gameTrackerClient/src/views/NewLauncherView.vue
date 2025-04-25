<template>
	<div>
		<Toast/>
		<h1>Add New Launcher</h1>
		<Form v-slot="$form" @submit="OnSubmit" id="newLauncherBox" :resolver="resolver" :initialValues>
			<div>
				<InputText
					class="inputLauncherName"
					type="text"
					placeholder="Launcher Name"
					v-model="launcherName"
					required
				/>
			</div>
			<br>
			<div>
				<MultiSelect
					v-model="relatedGames"
					:options="allGames"
					optionLabel="name"
					filter
					placeholder="Select Related Games"
					class="select"
				/>
			</div>
			<br>
			<br>
			<Button
				label="Add Launcher To Database"
				@click="OnSubmit"
				:loading="loading"
			/>
		</Form>
	</div>
</template>
<script setup lang="ts">
import {InputText, Toast, MultiSelect, Button} from 'primevue';
import {Form} from '@primevue/forms'
import { onMounted, ref } from 'vue';
import {useField} from 'vee-validate';
import {addNewLauncher} from '@/DataAccess/launcherDataAccess.ts';
import router from '@/router';
import { addLauncherToGame, getAllGames } from '@/DataAccess/gameDataAccess.ts';

const loading = ref(false);
const allGames = ref();
const relatedGames = ref();

const {value: launcherName} = useField("launcherName");

onMounted(async () => {
	allGames.value = await getAllGames();
})

const OnSubmit = async() => {
	loading.value = true;
	const newLauncher = await addNewLauncher(launcherName.value);

	if(newLauncher != null && relatedGames.value != undefined){
		for(let i = 0; i < relatedGames.value.length; i++){
			await addLauncherToGame(relatedGames.value[i].id, newLauncher.id);
		}
	}

	loading.value = false;
	await router.push('/');
}

</script>

<style scoped>
Form{
	text-align: center;
	width: 100%;
	align-self: center;
	row-gap: 15px;
}

h1{
	text-align: center;
}
</style>