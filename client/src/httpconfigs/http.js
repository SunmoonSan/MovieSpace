import axios from 'axios';
import apiUrl from './api';

axios.defaults.timeout = 10000;
axios.defaults.baseURL = apiUrl;

export default axios;
