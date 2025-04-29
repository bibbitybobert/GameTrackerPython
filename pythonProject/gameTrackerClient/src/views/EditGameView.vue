<template>
	<div>
		<Toast/>
		<h1>Update game {{gameName}}</h1>
		<Form v-slot="$form" @submit="OnSubmit" id="newGameBox" :resolver="resolver" :initialvalues>
			<InputText
				class="inputGameName"
				type="text"
				placeholder="Game Name"
				v-model="gameName"
				required
				disabled
			/>
			<CheckboxGroup class="playerSupport">
				<div class="flex-auto">
					<Checkbox v-model="singleplayer" inputId="Singleplayer" value="singleplayer" binary disabled/>
					<label for="Singleplayer">Singleplayer</label>
				</div>
				<div class="flex auto">
					<Checkbox v-model="multiplayer" inputId="Multiplayer" value="multiplayer" binary disabled/>
					<label for="Multiplayer">Multiplayer</label>
				</div>
			</CheckboxGroup>
			<div class="datesGroup">
				<DatePicker
					v-model="releaseDate"
					showIcon
					fluid
					iconDisplay="input"
					inputId="releaseDate"
					placeholder="Release Date"
					class="datePicker"
					required
					disabled
				/>
				<DatePicker
					v-model="latestUpdate"
					showIcon
					fluid
					iconDisplay="input"
					inputId="lastestUpdate"
					placeholder="Latest Update"
					class="datePicker"
					required
				/>
			</div>
			<br>
			<div class="sizeAndAchievements">
				<InputNumber
					v-model="downloadSize"
					suffix=" MB"
					placeholder="Download Size in MB"
					required
					:max-fraction-digits="3"
					class="field"
					/>
				<InputNumber
					v-model="achievementNum"
					placeholder="Number of Achievements"
					class="field"
					/>
			</div>
			<CheckboxGroup class="peripheralSupport">
				<div class="flex-auto">
					<Checkbox v-model="mkSupport" inputId="mkSupport" value="mkSupport" binary disabled/>
					<label for="mkSupport">Mouse and Keyboard</label>
				</div>
				<div class="flex auto">
					<Checkbox v-model="controllerSupport" inputId="controllerSupport" value="controllerSupport" binary disabled/>
					<label for="controllerSupport">Controller</label>
				</div>
			</CheckboxGroup>
			<div class="relations">
				<Select
					v-model="launcher"
					:options="allLaunchers"
					optionLabel="name"
					filter
					placeholder="Select a Launcher"
					class="select"
				/>
				<MultiSelect
					v-model="gameTags"
					:options="allTags"
					optionLabel="name"
					filter
					placeholder="Select Tags"
					class="select"
				/>
			</div>
			<br>
			<br>
			<Button
				label="Update Game"
				@click="OnSubmit"
				:loading="loading"
			/>
		</Form>
	</div>
</template>

<script setup lang="ts">
import {InputText, Button, Toast, Checkbox, DatePicker, InputNumber, MultiSelect, Select} from 'primevue';
import {useToast} from 'primevue/usetoast';
import {Form} from '@primevue/forms';
import {ref, onMounted} from 'vue';
import { useField } from 'vee-validate';
import {getAllTags, getGameTags} from '@/DataAccess/tagDataAccess.ts'
import {getAllLaunchers, getGameLauncher} from '@/DataAccess/launcherDataAccess.ts'
import { addLauncherToGame, getGameById, addTagToGame, updateGame} from '@/DataAccess/gameDataAccess.ts';
import router from '@/router';
import { useRoute } from 'vue-router';


const loading = ref(false);
const allTags = ref();
const allLaunchers = ref();
const tagOptions = ref();
const editGame = ref();

const route = useRoute();

const {value: gameName} = useField('gameName');
const {value: singleplayer} = useField('singleplayer');
const {value: multiplayer} = useField('multiplayer');
const {value: releaseDate} = useField('releaseDate');
const {value: latestUpdate} = useField('latestUpdate');
const {value: downloadSize} = useField('downloadSize');
const {value: achievementNum} = useField('achievementNum');
const {value: mkSupport} = useField('mkSupport');
const {value: controllerSupport} = useField('controllerSupport');
const {value: launcher} = useField('launcher');
const {value: gameTags} = useField('gameTags');

const OnSubmit = async () =>{
	if(singleplayer.value == undefined)
		singleplayer.value = false;
	if(multiplayer.value == undefined)
		multiplayer.value = false;

	if(mkSupport.value == undefined)
		mkSupport.value = false;
	if(controllerSupport.value == undefined)
		controllerSupport.value = false;

	const updatedGame = await updateGame(
		route.params.gameId,
		gameName.value,
		!!singleplayer.value,
		!!multiplayer.value,
		releaseDate.value.toISOString(),
		latestUpdate.value.toISOString(),
		downloadSize.value,
		achievementNum.value,
		!!mkSupport.value,
		!!controllerSupport.value
	);

	if(updatedGame != null && gameTags.value !== undefined) {
		for (let i = 0; i < gameTags.value.length; i++) {
			await addTagToGame(updatedGame.id, gameTags.value[i].id);
		}
	}

	if(updatedGame != null && launcher.value !== undefined){
		await addLauncherToGame(updatedGame.id, launcher.value.id);
	}

	await router.push('/');
}

onMounted(async () => {
	allTags.value = await getAllTags();
	allLaunchers.value = await getAllLaunchers();

	const id = route.params.gameId;
	editGame.value = await getGameById(id);
	setData()
	launcher.value = await getGameLauncher(id);
	gameTags.value = await getGameTags(id);
});

function setData() {
	gameName.value = editGame.value.name;
	singleplayer.value = editGame.value.singleplayer;
	multiplayer.value = editGame.value.multiplayer;
	releaseDate.value = editGame.value.releaseDate;
	latestUpdate.value = editGame.value.latestUpdate;
	downloadSize.value = editGame.value.downloadSize;
	achievementNum.value = editGame.value.achievements;
	mkSupport.value = editGame.value.mk;
	controllerSupport.value = editGame.value.controller;
}

</script>

<style scoped>
Form{
	text-align: center;
	width: 100%;
	align-self: center;
	row-gap: 15px;
}

.inputGameName{
	width: 50%;
}

h1{
	text-align: center;
}

.playerSupport{
	display: flex;
	width: 100%;
	justify-content: center;
}

.playerSupport div{
	margin: 5px;
	display: inline-flex;
	align-content: center;
	justify-content: center;
}

.playerSupport div label{
	text-align: center;
	justify-content: center;
	align-content: center;
}

.peripheralSupport{
	display: flex;
	width: 100%;
	justify-content: center;
}

.peripheralSupport div{
	margin: 5px;
	display: inline-flex;
	align-content: center;
	justify-content: center;
}

.peripheralSupport div label{
	text-align: center;
	justify-content: center;
	align-content: center;
}

.datesGroup{
	width: 50%;
	display: inline-flex;
}

.datesGroup .datePicker{
	display: flex;
	width: 50%;
	justify-content: center;
}

.sizeAndAchievements{
	width: 50%;
	display: inline-flex;
}

.sizeAndAchievements .field{
	display: flex;
	width: 50%;
	justify-content: center;
}

.relations{
	width: 50%;
	display: inline-flex;
}

.relations .select{
	display: flex;
	width: 50%;
	justify-content: center;
}


</style>