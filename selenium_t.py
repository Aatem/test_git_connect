from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://infodialog.ru/o-kompanii")
#assert "Python" in driver.title

elem = driver.find_element(By.CLASS_NAME, "monoblock-ul")
rezult = elem.text.split(';\n')


name = ['Name']
tb = pd.DataFrame(data=rezult, columns=name)
tb.to_csv("name.csv", index=False)
print('sfsd')
driver.close()