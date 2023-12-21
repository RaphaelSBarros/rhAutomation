from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("")

#Encontra o elemento SELECT na página e cicla por cada uma das opções, exibindo o valor e selecionando cada uma por vez
element = driver.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

#Suporte para elementos com SELECT otimizando o código de cima
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
index = 0
value = 0
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
select = Select(driver.find_element(By.ID, 'id'))
select.deselect_all() #deselecionando todas as opções
options = select.options #pega todas as opções disponíveis
element.submit() #vai caminhar por todo o DOM até achar o elemento submit do formulário, se não tiver ele gera o erro NoSuchElementException
