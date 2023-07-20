from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your Chrome WebDriver executable
webdriver_path = '/usr/local/bin'

# Replace with the URL of the YouTube video page
video_url = 'https://studio.youtube.com/channel/UCowu_0rYjGJ_G5v1CgY1xbQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'

# Start the WebDriver
driver = webdriver.Chrome(webdriver_path)

# Open the YouTube video page
driver.get(video_url)

# Wait for the settings button to be visible
settings_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'ytcp-icon-button[icon="icons:arrow-drop-down"]'))
)

# Click on the settings button
settings_button.click()

# Wait for the dropdown menu to be visible
dropdown_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'tp-yt-iron-dropdown'))
)

# Find the "Unlisted" option in the dropdown menu and click on it
unlisted_option = dropdown_menu.find_element(By.XPATH, '//div[@class="ytcp-text-dropdown-trigger-content style-scope ytcp-video-metadata"]//span[contains(text(), "Unlisted")]')
unlisted_option.click()

# Wait for the "Save" button to be visible
save_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'ytcp-button#done-button'))
)

# Click on the "Save" button
save_button.click()

# Close the WebDriver
driver.quit()
