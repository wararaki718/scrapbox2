const path = require('path')
const Dotenv = require('dotenv-webpack')

// load dotenv filename
let dotenv_filename = process.env.DOTENV_FILE;
if(dotenv_filename === undefined) {
  dotenv_filename = '.env.prd'
}
console.log(process.env.DOTENV_FILE)
console.log(dotenv_filename)

module.exports = {
  webpack: config => {
    config.plugins = config.plugins || []

    config.plugins = [
      ...config.plugins,

      // Read the .env file by using webpack lib.
      new Dotenv({
        path: path.join(__dirname, dotenv_filename),
        systemvars: true
      })
    ]

    return config
  }
}
