import {game} from '@/lib/models/game.ts';
import {handleError} from 'vue';
import jwtInterceptor from '@/helpers/http.ts';

async function addNewGame(name: string,
													singleplayer: boolean,
													multiplayer: boolean,
													releaseDate: Date,
													latestUpdate: Date,
													downloadSize: number,
													achievements: number,
													mk: boolean,
													controller: boolean): Promise<game|null>{
	try{
		const res = await jwtInterceptor.post(`api/games/newGame`, {
			name: `${name}`,
			singleplayer: `${singleplayer}`,
			multiplayer: `${multiplayer}`,
			releaseDate: `${releaseDate}`,
			latestUpdate: `${latestUpdate}`,
			downloadSize: `${downloadSize}`,
			achievements: `${achievements}`,
			mkSupport: `${mk}`,
			controllerSupport: `${controller}`
		});
		if(res.status == 200)
			return res.data;
		else
			return null;
	}catch(ex){
		if(ex.status == 404)
			return null;
		handleError(ex);
		return ex.response;
	}
}

async function addTagToGame(gameId: number, tagId: number): Promise<boolean|string> {
	try{
		const res = await jwtInterceptor.post(`api/games/${gameId}/addTag/${tagId}`);
		return res.status == 200;
	}
	catch(ex){
		if(ex.status == 400){
			return ex.response;
		}
		handleError(ex)
		return ex.response;
	}
}

async function addLauncherToGame(gameId: number, launcherId: number): Promise<boolean|string> {
	try{
		const res = await jwtInterceptor.post(`api/games/${gameId}/addLauncher/${launcherId}`);
		return res.status == 200;
	}
	catch(ex){
		if(ex.status == 400){
			return ex.response;
		}
		handleError(ex)
		return ex.response;
	}
}

async function getAllGames(): Promise<game[]|string>{
	try{
		const res = await jwtInterceptor.get(`api/games/allGames`);
		if(res.status == 200){
			let games: game[] = []
			for(let i = 0; i<res.data.length; i++){
				games.push(new game(
					Number(res.data[i].id),
					String(res.data[i].name),
					Boolean(res.data[i].singleplayer),
					Boolean(res.data[i].multiplayer),
					new Date(res.data[i].releaseDate),
					new Date(res.data[i].latestUpdate),
					Number(res.data[i].downloadSize),
					Number(res.data[i].achievements),
					Boolean(res.data[i].mk),
					Boolean(res.data[i].controller)));
			}
			return games;
		}
		else{
			return "Unable to fetch all games";
		}
	}catch(ex){
		if(ex.status == 400 || ex.status == 500){
			return "Unable to fetch all games";
		}
		handleError(ex);
		return ex.response;
	}
}

export {
	addNewGame,
	addTagToGame,
	addLauncherToGame,
	getAllGames,
}