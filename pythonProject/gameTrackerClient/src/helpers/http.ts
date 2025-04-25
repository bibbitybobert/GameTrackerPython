import axios from 'axios';

const jwtInterceptor = axios.create();
jwtInterceptor.defaults.baseURL = 'http://localhost:5000';

jwtInterceptor.interceptors.request.use(async (config) => {
	console.log('JWT Interceptor sending request to:', config.url);
	return config;
});

export default jwtInterceptor;