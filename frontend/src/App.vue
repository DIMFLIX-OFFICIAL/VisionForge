<template>
  <router-view/>
</template>

<style lang="scss">
:root {
    --bg: #eff1f5;
	--sbg: #E7E9EE;
    --light-sbg: #ccd0da;
	--lavander: #7287fd;
    --text: #4c4f69;
	--hinted-text: #ffffff;

	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-webkit-text-size-adjust: 100%;
	font-family: 'Noto', sans-serif;
	font-weight: 700
}
*{
	box-sizing: border-box;
}
body {
	background: var(--bg);
	color: var(--text);
	margin: 0;
}

button{
	padding: 6px 25px;
	border-radius: 10px;
	color: white;
	outline: none;
	border: none;
	font-size: 20px;
	font-family: 'Noto', sans-serif;
	font-weight: 700
}

h1{
	margin: 0;
}

p{
	margin: 0;
}
</style>
