import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import './assets/main.css';

import axios from './plugins/axios';

import * as mdb from 'mdb-ui-kit';
import 'mdb-ui-kit/css/mdb.min.css';

const app = createApp(App);

app.use(router, mdb);
app.use(axios, {
  baseUrl: 'http://localhost:8000',
});

app.mount('#app');
