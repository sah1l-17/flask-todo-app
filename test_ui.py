from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Use WebDriverManager to get the ChromeDriver (this will download it if needed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("http://localhost:5000/")
    assert "ToDo" in driver.page_source
    print("Selenium test passed!")
finally:
    driver.quit()