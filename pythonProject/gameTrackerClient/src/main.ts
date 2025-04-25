import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Lara from '@primeuix/themes/lara';
import ToastService from 'primevue/toastservice';


const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
	theme: {
		preset: Lara
	}
})
app.use(ToastService)

app.mount('#app')
