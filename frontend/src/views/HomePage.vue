<script setup>
import { logout } from "@/modules/auth";
import { getAccountInfo } from "@/modules/api";
import { onMounted, ref } from "vue";

const name = ref('')

onMounted(async () => {
	let user = await getAccountInfo()
	if (user !== null) {
		name.value = user.name
	} else {
		logout()
	}
})
</script>

<template>
  <div class="home">
	<p class="title">Welcome to VisionForge, {{name}}</p>
	<p class="description">You have been successfully authorized</p>
	<button @click="logout" class="logout-btn">logout</button>
  </div>
</template>

<style scoped lang="scss">
.home {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	height: 100vh;
	width: 100%;

	.title {
		font-size: 40px;
		margin-bottom: 0;
	}

	.description {
		margin-bottom: 30px;
		font-size: 16px;
		color: var(--text);
	}

	.logout-btn {
		background: var(--lavander);
		border-radius: 15px;
		border: none;
		width: 30%;
		max-width: 500;
		height: 60px;
		color: var(--hinted-text);
		font-weight: 600;
		font-size: 18px;
	}
}
</style>