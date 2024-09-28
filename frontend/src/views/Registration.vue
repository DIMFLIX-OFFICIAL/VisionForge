<script setup>
import {onMounted, ref} from "vue";
import {registration, isAuthenticated} from "@/modules/auth";
import { toast } from "@/modules/swal2";
import { router } from "@/router/index";

const username = ref('');
const email = ref('');
const password = ref('');
const name = ref('');

async function register() {
	if (!email.value || !username.value || !password.value || !name.value) {
		toast("Не все поля не заполнены!", "error")
		return;
	}

	const err = await registration(email.value, username.value, password.value, name.value)

	if (err) {
		toast(err, "error")
	}
}

onMounted(async () => {
	if (await isAuthenticated()) {
		router.push("/");
	}
})
</script>

<template>
	<div class="bg">
		<div class="auth-container">
			<div class="block">
				<p class="title">Регистрация</p>
				<input placeholder="Почта" v-model="email" type="email">
				<input placeholder="Имя" v-model="name" type="text">
				<input placeholder="Логин" v-model="username" type="text">
				<input placeholder="Пароль" v-model="password" type="password">
			</div>

			<div class="block">
				<button class="auth-btn" @click="register">Зарегистрироваться</button>
				<router-link to="/auth/login" class="another-way">Уже есть аккаунт?</router-link>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.bg {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 100vh;
}

.auth-container {
	background: var(--sbg);
	width: 80%;
	max-width: 600px;
	border-radius: 15px;
	padding: 50px 0 30px;
	box-sizing: border-box;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.block {
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}
.title {
	font-size: 27px;
	font-weight: 700;
	margin-bottom: 30px;
	color: var(--text)
}

.auth-container input {
	background: var(--light-sbg);
	width: 90%;
	height: 60px;
	border-radius: 15px;
	border: none;
	padding-left: 10px;
	box-sizing: border-box;
	color: var(--text);
	font-weight: 600;
	font-size: 16px;
	outline: none;
	margin-bottom: 15px;
}

.auth-container input::placeholder {
	color: var(--button);
}

.auth-container input:-webkit-autofill, .auth-container input:-webkit-autofill:focus{
    -webkit-box-shadow: 0 0 0 30px var(--light-sbg) inset;
    -webkit-text-fill-color: var(--text);
}

.auth-btn {
	background: var(--lavander);
	border-radius: 15px;
	border: none;
	width: 90%;
	height: 60px;
	color: var(--hinted-text);
	font-weight: 600;
	font-size: 18px;
}

.another-way {
	color: var(--lavander);
	font-size: 17px;
	font-weight: 600;
	text-decoration: none;
	margin-top: 10px;
}
</style>
