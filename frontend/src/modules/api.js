import axios from 'axios';
import { logout } from "@/modules/auth";

const api = axios.create();

api.interceptors.response.use(
	response => {
	  return response;
	},
	error => {
		if (error.response && error.response.status === 401) {
			console.log("Unauthorized api!");
			logout();
		}
		return Promise.reject(error);
	}
);

export async function getAccountInfo() {
	return api.post("/api/protected/get_my_account_info")
		.then(response => {
			return JSON.parse(response.data)
		})
		.catch(e => { return null })
}