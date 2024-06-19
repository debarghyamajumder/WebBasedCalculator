from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


edge_options = Options()
edge_options.binary_location = msedge_path


driver = webdriver.Edge(options=edge_options)

try:

    expression = input("Please enter a mathematical expression: ")


    driver.get("https://web-based-calculator-zeta.vercel.app")


    input_element = driver.find_element(By.ID, "display")
    input_element.send_keys(expression)


    wait = WebDriverWait(driver, 5)
    button_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="keys"]/button[15]')))
    button_element.click()


    time.sleep(5)


    result = input_element.get_attribute("value")


    print(f"The result of the expression {expression} is: {result}")

    print("All tests passed successfully!")

finally:

    driver.quit()
