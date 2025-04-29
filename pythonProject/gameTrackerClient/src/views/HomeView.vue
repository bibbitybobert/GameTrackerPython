<template>
	<div>
		<h1 class="introduction">
			Welcome to GameTracker
		</h1>
		<div class="s"></div>
<!--		<button-->
<!--				@click="LogOut"-->
<!--				type="submit"-->
<!--				class="max-w-40 w-full rounded-full appearance-none border-0 p-4 outline-0 text-xl mb-6 font-medium bg-white/30 hover:bg-white/40 active:bg-white/20 text-primary-contrast/80 cursor-pointer transition-colors duration-150"-->
<!--		>-->
<!--				Sign Out-->
<!--		</button>-->
		<DataTable :value="games" :size="small" v-model:selection="selectedGame" selectionMode="single" dataKey="id" @rowSelect="OnRowSelect">
			<Column field="name" header="Name" dataType="string" style="width: 20%"></Column>
			<Column field="downloadSize" header="Download Size" dataType="float">
				<template #body="{ data }">
					{{ formatSize(data.downloadSize) }}
				</template>
			</Column>
			<Column field="releaseDate" header="Release Date" dataType="date">
				<template #body="{ data }">
					{{ formatDate(data.releaseDate) }}
				</template>
			</Column>
			<Column field="latestUpdate" header="Latest Update" dataType="date">
				<template #body="{ data }">
					{{ formatDate(data.latestUpdate) }}
				</template>
			</Column>
			<Column field="achievements" header="achievements" dataType="integer"></Column>
			<Column field="singleplayer" header="SP" dataType="boolean" class="boolCol">
				<template #body="{ data }">
						<i class="pi" :class="{ 'pi-check-circle text-green-500': data.singleplayer, 'pi-times-circle text-red-400': !data.singleplayer }"></i>
				</template>
			</Column>
			<Column field="multiplayer" header="MP" dataType="boolean" class="boolCol">
				<template #body="{ data }">
						<i class="pi" :class="{ 'pi-check-circle text-green-500': data.multiplayer, 'pi-times-circle text-red-400': !data.multiplayer }"></i>
				</template>
			</Column>
			<Column field="mk" header="MK" dataType="boolean" class="boolCol">
				<template #body="{ data }">
						<i class="pi" :class="{ 'pi-check-circle text-green-500': data.mk, 'pi-times-circle text-red-400': !data.mk}"></i>
				</template>
			</Column>
			<Column field="controller" header="C" dataType="boolean" class="boolCol">
				<template #body="{ data }">
						<i class="pi" :class="{ 'pi-check-circle text-green-500': data.controller, 'pi-times-circle text-red-400': !data.controller }"></i>
				</template>
			</Column>
		</DataTable>

	</div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import {DataTable, Column} from 'primevue';
import {game} from '@/lib/models/game.ts';
import {ref} from 'vue';
import {getAllGames} from '@/DataAccess/gameDataAccess.ts';
import { useField } from 'vee-validate';
import router from '@/router';

const games = ref();
const selectedGame = ref();

onMounted(async () => {
	games.value = await getAllGames();
});

const formatDate = (value) => {
	return value.toLocaleDateString('en-US', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
    });
};

const formatSize = (value) => {
	return `${value} MB`
}

const OnRowSelect = (event) => {
	var gameId = event.data.id;
	router.push(`/edit/${gameId}`);
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

.boolCol{
	width: 1%;
}

Column{
	align-content: center;
	justify-content: center
}
</style>
