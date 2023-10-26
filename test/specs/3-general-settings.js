describe('General Settings', () => {
    it('Access profile', async() => {
        // access landing page & click Skip
        await driver.pause(3000)
        await driver.$('//android.view.View[@content-desc="Skip"]').click();

        // assert after click Skip
        const loginSigninButton = $('//android.view.View[@content-desc="Log In/Sign Up to Start Investing"]');
        await expect(loginSigninButton).toHaveText('Log In/Sign Up to Start Investing');

        // head to profile
        await driver.$('android.widget.ImageView').click()
        await driver.pause(1000)
        
        //assert in profile page
        const profile = $('//android.widget.ImageView[@content-desc="Settings"]')
        await expect(profile).toHaveText('Settings')
    });

    it('[Settings] - Change language', async() => {
        // change language
        await driver.$('//android.widget.ImageView[@content-desc="Settings"]').click()
        await driver.$('//android.view.View[@content-desc="Language English"]').click()
        await driver.$('//android.view.View[@content-desc="Bahasa Indonesia"]').click()

        //assert
        await driver.$('android.widget.Button').click()
        const language = $('/android.view.View[@content-desc="Bahasa Bahasa Indonesia"]');
        await expect(language).toHaveText('Bahasa');

        //change back to EN
        await driver.$('//android.view.View[@content-desc="Bahasa Bahasa Indonesia"]').click()
        await driver.$('//android.view.View[@content-desc="English"]').click()
    });

    // need to reload first & head to profile then access settings

    it('[Settings] - Change currency', async() => {
        // click settings, change currency to USD
        await driver.$('//android.widget.ImageView[@content-desc="Settings"]').click()
        await driver.$('//android.view.View[@content-desc="Default Currency IDR"]').click()
        await driver.$('//android.view.View[@content-desc="USD"]').click()
        await driver.$('[android.widget.Button]').click()


        //assert
        const currency = $('//android.view.View[@content-desc="Default Currency USD"]');
        await expect(currency).toHaveText('USD');
    });

    // need to reload first & head to profile

    it('[Settings] - Change number format', async() => {
        //click number format, select period as decimal
        await driver.$('//android.view.View[@content-desc="Number Format Comma as decimal"]').click()
        await driver.$('//android.view.View[@content-desc="Period as decimal (1,234.56)"]').click()
        await driver.$('android.widget.Button').click()

        //assert
        const numberFormat = $('//android.view.View[@content-desc="Number Format Period as decimal"]')
        await expect(numberFormat).toHaveText('Period as decimal');
    });
});