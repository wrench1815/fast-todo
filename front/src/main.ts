import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import axios from 'axios';
import VueAxios from 'vue-axios';

import * as mdb from 'mdb-ui-kit';
import 'mdb-ui-kit/css/mdb.min.css';

const app = createApp(App);

app.use(router, mdb);

app.use(VueAxios, axios);
app.provide('axios', app.config.globalProperties.axios);
axios.defaults.baseURL = 'http://localhost:8000/';

app.mount('#app');
