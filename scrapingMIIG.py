# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Opciones de navegación

options =webdriver.ChromeOptions()
options.add_argument('--strat-maximized')
options.add_argument('--disable-extensions')

driver_path = 'Chrome Complementos/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(driver_path)
# Iniciar en pantalla 02
driver.set_window_position(2000,0)
driver.maximize_window()
# Inicializar el navegador
driver.get('https://miig.sgc.gov.co')
time.sleep(1)
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(1)
# Aceptar terminos y condiciones
iframe = driver.find_element_by_xpath("//iframe[contains(@id,'DlgFrame')]")
driver.switch_to.frame(iframe)
cookieAccpet = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl51_g_86a698c1_69cf_4a86_a26f_463629494e12_ctl00_rbTerminos_0"]')))
cookieAccpet.click()
cookieAccpet = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl51_g_86a698c1_69cf_4a86_a26f_463629494e12_ctl00_btnAceptar"]')))
cookieAccpet.click()

driver.switch_to.default_content()

