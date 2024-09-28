const { defineConfig } = require('@vue/cli-service')

const dotenv = require('dotenv')
const dotenvExpand = require('dotenv-expand')

var myEnv = dotenv.config({path: '../.env'})
dotenvExpand(myEnv)

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
	host: 'localhost',
	port: process.env.VUE_DEV_PORT,
	proxy: {
	  '^/api': {
		target: process.env.API_URL,
		changeOrigin: true,
	  },
	}
  }
})
