describe('LOGIN MOBEE', () => {
    it('PHONE - Login with empty phone number', async() => {
        // clicking continue
        await driver.$('//android.view.View[@content-desc="Continue"]').click();

        //assert 
        await driver.pause(3000)
        const popupError = $('[android.widget.ImageView]');
        await expect(popupError).toHaveText('Oops something happened...');

        //close error pop up
        await driver.$('//android.view.View[@content-desc="OK"]').click();
    });

    it('PHONE - Log in with wrong phone number', async() => {
        //input wrong phone number
        await driver.$('//android.widget.ImageView[@content-desc="Financial Freedom Starts Here Login/Sign Up Phone Number"]/android.widget.EditText').setValue('8765672937');
        await driver.$('//android.view.View[@content-desc="Continue"]').click();

        //assert
        await driver.pause(3000)
        const popupError = $('[android.widget.ImageView]');
        await isExportDeclaration(popupError).toHaveText('Oops something happened...');

        //close error pop up
        await driver.$('//android.view.View[@content-desc="OK"]').click();
    });

    it('PHONE - Login with valid phone number', async() => {
        // input phone number
        await driver.$('//android.widget.ImageView[@content-desc="Financial Freedom Starts Here Login/Sign Up Phone Number"]/android.widget.EditText').setValue('{valid number}'); // still draft
        await driver.$('//android.view.View[@content-desc="Continue"]').click();

        //input password
        await driver.pause(3000);
        await driver.$('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText')
            .setValue('{valid password}');
        
        //click Continue
        await driver.$('//android.view.View[@content-desc="Log In"]').click();

        //verify OTP bypass
        await driver.pause(4000);
        await driver.$('/android.view.View[@content-desc="Verify"]').click();

        // assert
        await driver.pause(5000)
        const successLogin = $('//android.view.View[@content-desc="Portfolio Value"]');
        await expect(successLogin).toHaveText('Portfolio Value');

    });
});