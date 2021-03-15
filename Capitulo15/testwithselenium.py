from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastNameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

### Método 1 ###
firstnameField.send_keys('Ryan')
lastNameField.send_keys('Mitchel')
submitButton.click()
################

### Método 2 ###
actions = ActionChains(driver).click(firstnameField).send_keys('Ryan')\
                               .click(lastNameField).send_keys('Mitchell')\
                               .send_keys(Keys.RETURN)
actions.perform()
################

print(driver.find_element_by_tag_name('body').text)

driver.close()
