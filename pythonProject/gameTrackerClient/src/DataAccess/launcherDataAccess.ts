import {launcher} from '@/lib/models/launcher.ts'
import {handleError} from 'vue';
import jwtInterceptor from '@/helpers/http.ts';
import { tag } from '@/lib/models/tag.ts';

async function addNewLauncher(name: string): Promise<launcher|null>{
	try{
		const res = await jwtInterceptor.post('api/launcher/newLauncher',{
			name: `${name}`
		});

		if(res.status == 200)
			return res.data;
		else
			return null;
	}
	catch(ex){
		if(ex.status == 400)
			return null;
		handleError(ex);
		return ex.response;
	}
}

async function getAllLaunchers(): Promise<tag[] | null>{
	try{
		const res = await jwtInterceptor.get(`api/launcher/getAllLaunchers`);
		if(res.status == 200){
			let launcherList: launcher[] = [];
			for(let i = 0; i < res.data.length; i++){
				launcherList.push(new launcher(Number(res.data[i].id), res.data[i].name));
			}
			return launcherList;
		}
		else
			return null;
	}
	catch(ex){
		if(ex.status == 400 || ex.status == 500)
			return null;
		handleError(ex);
		return null;
	}
}


export{
	addNewLauncher,
	getAllLaunchers,
}