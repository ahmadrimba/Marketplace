from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Ganti dengan URL codespaces kamu atau localhost:5000
    driver.get("http://localhost:5000/login")

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("testpass")
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    time.sleep(2)

    assert "/market" in driver.current_url
    print("✅ Login test passed.")

except Exception as e:
    print("❌ Login test failed:", e)

finally:
    driver.quit()
