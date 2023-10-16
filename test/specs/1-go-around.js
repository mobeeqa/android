
describe('Access mobee without log in', () => {

    it('Skip button',  async() => {
        // access landing page & click Skip
        await driver.pause(3000)
        await driver.$('//android.view.View[@content-desc="Skip"]').click();

        // assert after click Skip
        const loginSigninButton = $('//android.view.View[@content-desc="Log In/Sign Up to Start Investing"]');
        await expect(loginSigninButton).toHaveText('Log In/Sign Up to Start Investing');
    });

    it('HOME - Deposit', async() => {
        // deposit without login
        await driver.$('//android.view.View[@content-desc="Portfolio Value"]/android.widget.ImageView[3]').click();

        //assert after click deposit
        const depositNoLogin = $('//android.view.View[@content-desc="Complete Your Profile First"]');
        await expect(depositNoLogin).toHaveText('Complete Your Profile First');
    });

    // need step to refresh or close drawer first before next action 

    it('HOME - Quick Swap', async() => {
        // quick swap before login
        await driver.$('//android.view.View[@content-desc="Portfolio Value"]/android.widget.ImageView[4]').click();

        //assert after click quick swap
        const swapNoLogin = $('//android.view.View[@content-desc="Complete Your Profile First"]');
        await expect(swapNoLogin).toHaveText('Complete Your Profile First');
    });

    it('TRADE - Acces trade tab', async() => {
        // accessing trade tab
        await driver.$('//android.widget.ImageView[@content-desc="Trade Tab 2 of 5"]').click();

        // assert after click trade tab
        const tradePage = $('//android.widget.ImageView[@content-desc="Trade Tab 2 of 5"]');
        await expect(tradePage).toHaveText('Last Price');
    });

    it('TRADE - Search for valid coin name', async() => {
        // search for valid coin w/out login
        await driver.$('//android.view.View[@content-desc="Trade"]/android.widget.EditText').setValue('tether');

        // assert the search result
        const searchResult = $('//android.widget.ImageView[@content-desc="USDT Tether Rp 1 2 5 6 . 7 8 1 2 2 3 +0.08%"]');
        await expect(searchResult).toHaveText('Tether');
    });

    // need step to clear search value first

    it('TRADE - Search for invalid coin name', async() => {
        // search for invalid coin w/out login
        await driver.$('//android.view.View[@content-desc="Trade"]/android.widget.EditText').setValue('qrwer');

        // assert the search result
        const searchResult = $('//android.view.View[@content-desc="Trade Not Found Invalid keyword or asset is not yet available on Mobee."]');
        await expect(searchResult).toHaveText('Not Found');
    });

    it('EARN - Access Earn tab', async() => {
        // accessing earn without login
        await driver.$('/android.widget.ImageView[@content-desc="Earn Tab 3 of 5"]').click();

        // assert after click earn
        const accessEarn = $('//android.view.View[@content-desc="Complete Your Profile First"]');
        await expect(accessEarn).toHaveText('Complete Your Profile First');
    });

    it('TRANSACTION - Access Transaction tab', async() => {
        // accessing transaction tab w/out log in
        await driver.$('//android.widget.ImageView[@content-desc="Transactions Tab 4 of 5"]').click();

        //assert after click transaction
        const transaction = $('//android.widget.ImageView[@content-desc="Transactions Tab 4 of 5"]');
        await expect(transaction).toHaveText('Complete Your Profile First');
    });

    it('WALLET - Access Wallet tab', async() => {
        // accessing wallet tab w/out log in
        await driver.$('//android.widget.ImageView[@content-desc="Wallet Tab 5 of 5"]').click();

        //assert after click Wallet
        const wallet = $('//android.view.View[@content-desc="Complete Your Profile First"]').click();
        await expect(wallet).toHaveText('Complete Your Profile First');
    });

    // notif might be allowed first

    it('HOME - Click Login/Sign up', async() => {
        // click login / sign up
        await driver.$('//android.view.View[@content-desc="Log In/Sign Up to Start Investing"]').click();

        // assert after click login/sign up
        const loginSignup= $('//android.widget.ImageView[@content-desc="Financial Freedom Starts Here Login/Sign Up Phone Number"]')
        await expect(loginSignup).toHaveText('Financial Freedom');
    });

})