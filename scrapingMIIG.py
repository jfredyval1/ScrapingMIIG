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
driver = webdriver.Chrome(driver_path,chrome_options=options)
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
time.sleep(1)
cookieAccpet = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl51_g_86a698c1_69cf_4a86_a26f_463629494e12_ctl00_btnAceptar"]')))
cookieAccpet.click()

driver.switch_to.default_content()
# Iniciar navegación
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="ctl00_ctl51_g_1b55f9d1_80ba_407b_ab58_82eed386edb2_ctl00_wpCajaBusqueda_csr_sbox"]')))\
    .send_keys('Hidrogeología')
time.sleep(1)
#Enviar busqueda
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="ctl00_ctl51_g_1b55f9d1_80ba_407b_ab58_82eed386edb2_ctl00_wpCajaBusqueda_csr_SearchLink"]')))\
    .click()
# Capturar infomración de texto
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="ctl00_ctl51_g_6459c858_7354_4a84_9992_505f0b4f1814_csr1_groupContent"]')))

texto_busqueda=driver.find_element_by_xpath('//*[@id="ctl00_ctl51_g_6459c858_7354_4a84_9992_505f0b4f1814_csr1_groupContent"]')
texto_busqueda=texto_busqueda.text
# Creación de un dataframe
texto_col = texto_busqueda.split('\n')
# Crear listas vacias para almacenar información
titulo =list()
fecha=list()
# Almacenar la información como una tabla de dos variables
for i in range(0,len(texto_col),3):    #Salto de 3 dado que las variables
    titulo.append(texto_col[i])        #organizan de la forma:
    fecha.append(texto_col[i+1])       #Títutlo, Fecha, Texto con hipervinculo ver elemento
df = pd.DataFrame({'Título':titulo,'Fecha':fecha,'Buesqueda por:':'Hidrogeología'})
print(df)