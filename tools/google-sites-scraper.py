from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Setup the driver (Chrome)
driver = webdriver.Chrome()
url = "https://sites.google.com/view/sstasbih"

driver.get(url)
time.sleep(5) # Give the JavaScript time to load the content

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Google Sites usually wraps content in specific 'section' or 'div' classes
text_content = soup.get_text(separator='\n', strip=True)

print(text_content)
driver.quit()