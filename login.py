import time
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login(username, password):
    """
    A simple function which logs a user into Twitter using Selenium.
    Specifcally desigend as an experiment for use within an IDE.

    Parameters
    ----------
    username : str
        Twitter username of an existing account.
    password : str
        Twitter password of an existing account.
    """

    chromedriver_autoinstaller.install()
    # Automatically install chromedriver, avoiding need to tinker.
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/i/flow/login")
    # Get login page using Selenium
    time.sleep(5)
    # Sleep to allow page to load

    username_field = driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label")
    # Assign xpath of username form field to variable
    username_field.send_keys(username)
    # Enter the value passed as username into field
    time.sleep(1)
    # Sleep for 1sec so you can see it enter your username
    username_field.send_keys(Keys.RETURN)
    # Automated enter key press
    time.sleep(5)
    # Sleep again for 5 so password page can load

    password_field = driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label")
    # Assign xpath of password form field to variable
    password_field.send_keys(password)
    # Enter the value passed as password into field
    time.sleep(1)
    # Sleep for 1sec so you can see it enter password
    password_field.send_keys(Keys.RETURN)
    # Automated enter key press
    time.sleep(10)
    # Sleep for 10 sec so it doesn't close the page on submission


if __name__ == "__main__":
    # Enter your username and password below
    login('USERNAME','PASSWORD')
