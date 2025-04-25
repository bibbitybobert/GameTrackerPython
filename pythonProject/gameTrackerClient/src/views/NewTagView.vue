<template>
	<div>
		<Toast/>
		<h1>Add New Tag</h1>
		<Form v-slot="$form" @submit="OnSubmit" id="newTagBox" :resolver="resolver" :initialValues>
			<div>
				<InputText
					class="inputTagName"
					type="text"
					placeholder="Tag Name"
					v-model="tagName"
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
				label="Add Tag To Database"
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
import {addNewTag} from '@/DataAccess/tagDataAccess.ts';
import router from '@/router';
import { addTagToGame, getAllGames } from '@/DataAccess/gameDataAccess.ts';

const loading = ref(false);
const allGames = ref();
const relatedGames = ref();

const {value: tagName} = useField('tagName');

onMounted(async () => {
	allGames.value = await getAllGames();
})

const OnSubmit = async() =>{
	loading.value = true;
	const newTag = await addNewTag(tagName.value);

	if(newTag != null && relatedGames.value.length >= 0){
		for(let i = 0; i<relatedGames.value.length; i++){
			await addTagToGame(relatedGames.value[i].id, newTag.id);
		}
	}
	loading.value=false;

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