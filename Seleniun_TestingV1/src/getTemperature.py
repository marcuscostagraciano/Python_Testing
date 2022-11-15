from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def getTemp() -> str:
    """
    Returns:
        str: Returns the current temperature.
    """
    with webdriver.Chrome() as nav:
        nav.get("https://www.google.com/")
        nav.find_element(By.NAME, "q").send_keys(
            "previsão do tempo itinga joinville")
        nav.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        return nav.find_element(By.ID, "wob_tm").text
