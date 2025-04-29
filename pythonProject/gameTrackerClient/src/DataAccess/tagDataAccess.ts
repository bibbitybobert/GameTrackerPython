import {tag} from '@/lib/models/tag.ts';
import {handleError} from 'vue';
import jwtInterceptor from '@/helpers/http.ts';

async function addNewTag(name: string): Promise<tag|null>{
	try{
		const res = await jwtInterceptor.post(`api/tags/newTag`, {
			name: `${name}`
		});
		if(res.status==200){
			return res.data;
		}
		else{
			return null;
		}
	}
	catch(ex){
		if(ex.status == 400)
			return null;
		handleError(ex);
		return ex.response;
	}
}

async function getAllTags(): Promise<tag[] | null>{
	try{
		const res = await jwtInterceptor.get(`api/tags/getAllTags`);
		if(res.status == 200){
			let tagsList: tag[] = [];
			for(let i = 0; i < res.data.length; i++){
				tagsList.push(new tag(Number(res.data[i].id), res.data[i].name));
			}
			return tagsList;
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

async function getGameTags(gameId): Promise<tag[] | null>{
	try{
		const res = await jwtInterceptor.get(`api/tags/getTagsForGame/${gameId}`);
		if(res.status == 200){
			let tagsList: tag[] = [];
			for(let i = 0; i < res.data.length; i++){
				tagsList.push(new tag(Number(res.data[i].id), res.data[i].name));
			}
			return tagsList;
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

export {
	addNewTag,
	getAllTags,
	getGameTags,
}