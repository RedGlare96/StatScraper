from configparser import ConfigParser
import undetected_chromedriver as uc

cookie_name = 'chrome-data'
bin_dir = 'chrome-bin/chrome.exe'
version_number = 102

if __name__ == '__main__':
    print('CookieGen')
    print('Reading logs')
    config = ConfigParser()
    config.read('masterconfig.ini')
    bin_dir = config['browser']['bin_dir']
    version_number = int(config['browser']['version'])

    cookie_file = cookie_name
    print('The script will now open the browser with Linkedin. Log in with an account and RETURN BACK to this window')
    input('Press any key to continue: ')
    print('Opening browser')
    options = uc.ChromeOptions()
    options.user_data_dir = cookie_file
    options.binary_location = bin_dir
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    options.add_argument('--window-size=1024,640')
    options.add_argument('--disk-cache-size=1073741824')
    driver = uc.Chrome(headless=False, options=options, version_main=version_number)
    driver.get('https://www.linkedin.com/uas/login')
    input('Press the enter key to confirm settings')
    print('The script will now open the browser with Facebook. Log in with an account and RETURN BACK to this window')
    input('Press any key to continue: ')
    print('Connecting to site')
    driver.get('https://www.facebook.com/login.php')
    input('Press the enter key to confirm settings')
    print('The script will now open the browser with Instagram. Log in with an account and RETURN BACK to this window')
    input('Press any key to continue: ')
    print('Connecting to site')
    driver.get('https://www.instagram.com/accounts/login/')
    input('Press the enter key to confirm settings')
    input('You have reached the end of Cookiegen process. Press enter to exit and close the browser')
    print('Closing browser')
    driver.close()
    driver.quit()