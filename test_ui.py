from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')  # No UI
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get("http://localhost:5000/")
    assert "ToDo" in driver.page_source
    print("Selenium test passed!")
finally:
    driver.quit()
