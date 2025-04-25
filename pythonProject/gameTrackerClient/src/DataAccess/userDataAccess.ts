import {user} from '@/lib/models/user.ts'
import { handleError } from 'vue';
import jwtInterceptor from '@/helpers/http.ts';
import axios  from 'axios';

async function getUserById(id: string): Promise<user | undefined>{
	try{
		const res = await jwtInterceptor.post(`/users/${id}`);
		return response.data.value;
	}catch(ex){
		handleError(ex);
		return ex.response;
	}
}

async function getUserByEmail(email: string): Promise<user | undefined>{
	try{
		const res = await jwtInterceptor.get(`http://localhost:5000/api/users/email/${email}`);
		if(res.status == 200)
			return res.data.value;
		else if(res.status == 404)
			return undefined;
	}catch(ex){
		if(ex.status == 404)
			return undefined;
		handleError(ex);
		return ex.response;
	}
}

async function loginUser(email: string, password: string): Promise<user | undefined> {
	try{
		const res = await jwtInterceptor.post('/api/users/login', {
			email: `${email}`,
			password: `${password}`
		});
		if(res.status == 200) {
			localStorage.setItem("user", res.data.id);
			return res.data.id;
		}
		else{
			return null;
		}
	}catch(ex){
		if(ex.status == 404)
			return null;
		handleError(ex);
		return ex.response;
	}
}

async function logout(): Promise<boolean>{
	localStorage.setItem("user", null);
	return true;
}

async function registerUser(fName: string,
														lName: string,
														email: string,
														password: string): Promise<user | undefined>{
	try{
		const res = await jwtInterceptor.post('/api/users/register', {
			fName: fName,
			lName: lName,
			email: email,
			password: password
		});

		if(res.status == 200){
			localStorage.setItem("user", res.data.id);
			return res.data.id;
		}
		else{
			return null;
		}

	}catch(ex){
		handleError(ex);
		return ex.response;
	}
}

export{
	getUserById,
	getUserByEmail,
	loginUser,
	logout,
	registerUser,
}