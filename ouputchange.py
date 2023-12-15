from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize a WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()

# Open the first page and get some output
driver.get("http://localhost:63342/www.bemysenses.com/texttospeech.html?_ijt=4tcn0f5e10u77s3jtb8qq7ostd&_ij_reload=RELOAD_ON_SAVE")
output_element = driver.find_element_by_id("output_id")
output_text = output_element.text

# Close the first page
driver.close()

# Initialize a new WebDriver for the second page
driver = webdriver.Chrome()

# Open the second page
driver.get("https://example.com/second_page")

# Find the input element on the second page and input the text obtained from the first page
input_element = driver.find_element_by_id("input_id")
input_element.send_keys(output_text)

# Optionally, submit the form or perform other actions
# input_element.submit()

# Wait for some time to see the changes on the second page
time.sleep(5)

# Close the WebDriver
driver.quit()
