from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
prefs = {
    "profile.managed_default_content_settings.images": 2,
    "profile.default_content_setting_values.notifications": 2,
    "profile.managed_default_content_settings.stylesheets": 2,
    "profile.managed_default_content_settings.plugins": 1,
    "profile.managed_default_content_settings.popups": 2,
    "profile.managed_default_content_settings.geolocation": 2,
    "profile.managed_default_content_settings.media_stream": 2,
}
options.add_experimental_option("prefs", prefs)
options.add_argument("user-agent=" + "placeholder")
options.add_argument("headless")
options.add_argument("--disable-gpu")


def main():
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 5)
    driver.get(url="placeholder")
    wait.until(ec.element_to_be_clickable((By.XPATH, "placeholder")))
    driver.find_element(By.XPATH, "placeholder").click()


if __name__ == "__main__":
    main()
