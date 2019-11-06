
module.exports = {
  env: {
    MESSAGE: process.env.NODE_ENV === 'production'? 'hello, production': 'hello, staging or development!'
  }
}
