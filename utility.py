"""
module to hold required functions
"""
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver_path_with_browser_name(browser_name):
    """
    function to get teh correct driver for the browser being used

    param: 
    browser_name -> name of browser you are using

    """

    # TODO I should clean this up and put in a check if none is input
    if browser_name.lower() == "chrome":
        driver_path = ChromeDriverManager().install()
    elif browser_name.lower() == "firefox":
        driver_path = GeckoDriverManager().install()

    print(driver_path)
    return driver_path
