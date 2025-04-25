<template>
	<div>
		<Toast/>
		<h1>Add New Game</h1>
		<Form v-slot="$form" @submit="OnSubmit" id="newGameBox" :resolver="resolver" :initialvalues>
			<InputText
				class="inputGameName"
				type="text"
				placeholder="Game Name"
				v-model="gameName"
				required
			/>
			<CheckboxGroup class="playerSupport">
				<div class="flex-auto">
					<Checkbox v-model="singleplayer" inputId="Singleplayer" value="singleplayer"/>
					<label for="Singleplayer">Singleplayer</label>
				</div>
				<div class="flex auto">
					<Checkbox v-model="multiplayer" inputId="Multiplayer" value="multiplayer"/>
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
					<Checkbox v-model="mkSupport" inputId="mkSupport" value="mkSupport"/>
					<label for="mkSupport">Mouse and Keyboard</label>
				</div>
				<div class="flex auto">
					<Checkbox v-model="controllerSupport" inputId="controllerSupport" value="controllerSupport"/>
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
				label="Add Game To Database"
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
import {getAllTags} from '@/DataAccess/tagDataAccess.ts'
import {getAllLaunchers} from '@/DataAccess/launcherDataAccess.ts'
import { addLauncherToGame, addNewGame, addTagToGame } from '@/DataAccess/gameDataAccess.ts';
import { tag } from '@/lib/models/tag.ts';
import { game } from '@/lib/models/game.ts';
import router from '@/router';


const loading = ref(false);
const allTags = ref();
const allLaunchers = ref();
const tagOptions = ref();

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

	const game = await addNewGame(
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

	if(game != null && gameTags.value !== undefined) {
		for (let i = 0; i < gameTags.value.length; i++) {
			await addTagToGame(game.id, gameTags.value[i].id);
		}
	}

	if(game != null && launcher.value !== undefined){
		await addLauncherToGame(game.id, launcher.value.id);
	}

	await router.push('/');
}

onMounted(async () => {
	allTags.value = await getAllTags();
	allLaunchers.value = await getAllLaunchers();
});

</script>

<style>
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