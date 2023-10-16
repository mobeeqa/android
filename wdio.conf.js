exports.config = {
    runner: 'local',
    path: '/wd/hub',
    specs: ['./test/signup.js'],
    capabilities: [
        {
            "appium:platformName": 'Android',
            "appium:automationName": "UiAutomator2",
            "appium:app": "/Users/risnasetiyana/Downloads/app-staging-debug.apk",
            "appium:udid": "emulator-5554",
            "appium:appWaitActivity": "*",
            "appium:appGrantPermissions": "true",
            //"appium:port": "4723",
        },
    ],
    services: ['appium'],
    appium: {
        command: 'appium',
    },
    mochaOpts: {
        timeout: 50000
    },
};