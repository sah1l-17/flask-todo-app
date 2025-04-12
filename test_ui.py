from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Use the locally installed ChromeDriver
service = Service(executable_path="/usr/bin/chromedriver")  # Adjust path if needed
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://localhost:5000/")
    assert "ToDo" in driver.page_source
    print("Selenium test passed!")
finally:
    driver.quit()