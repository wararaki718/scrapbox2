// require('dotenv').config()

const path = require('path')
const Dotenv = require('dotenv-webpack')


function getEnv(node_env) {
  switch (node_env) {
    case "production":
      return ".env.prd";
    case "staging":
      return ".env.stg";
    default:
      break;
  }
  return ".env.def";
}

module.exports = {
  webpack: config => {
    config.plugins = config.plugins || []

    config.plugins = [
      ...config.plugins,

      // Read the .env file
      new Dotenv({
        path: path.join(__dirname, getEnv(process.env.NODE_ENV)),
        safe: false
      })
    ]

    return config
  }
}
