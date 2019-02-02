const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')


module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',
    devServer: {
		proxy: {
		    '/api*': {
			target: 'http://localhost:5000/'
		    }
		}
    },
    transpileDependencies:[/node_modules[/\\\\]vuetify[/\\\\]/],
    configureWebpack: {
        plugins: [
          new VuetifyLoaderPlugin()
        ]
      }
}
