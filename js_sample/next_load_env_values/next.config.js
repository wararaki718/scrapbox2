module.exports = {
    env: {
        MESSAGE: process.env.ENV_VALUE === "custom"? "load custom settings" : "load default settings"
    }
};
