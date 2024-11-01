const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig(
//   {transpileDependencies: true},
//   {publicPath: "static"})

module.exports = {
  publicPath: './', // 注意这里多个点 .
  outputDir: 'dist', // 注意结尾无 /
  assetsDir: 'assets',
}
