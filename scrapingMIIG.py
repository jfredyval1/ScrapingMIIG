# Librerías
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
options.add_argument('--strat-minimized')
options.add_argument('--disable-extensions')

driver_path = 'Chrome Complementos/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options=options)
# Iniciar en pantalla 02
driver.set_window_position(2000,0)
driver.minimize_window()
# Inicializar el navegador
driver.get('https://miig.sgc.gov.co')
time.sleep(2)
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(2)
# Aceptar terminos y condiciones
iframe = driver.find_element_by_xpath("//iframe[contains(@id,'DlgFrame')]")
driver.switch_to.frame(iframe)
cookieAccpet = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl51_g_86a698c1_69cf_4a86_a26f_463629494e12_ctl00_rbTerminos_0"]')))
cookieAccpet.click()
time.sleep(3)
cookieAccpet = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '//*[@id="ctl00_ctl51_g_86a698c1_69cf_4a86_a26f_463629494e12_ctl00_btnAceptar"]')))
cookieAccpet.click()

driver.switch_to.default_content()
# Iniciar navegación
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="ctl00_ctl51_g_1b55f9d1_80ba_407b_ab58_82eed386edb2_ctl00_wpCajaBusqueda_csr_sbox"]')))\
    .send_keys('Hidrogeología')
time.sleep(2)
#Enviar búsqueda
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="ctl00_ctl51_g_1b55f9d1_80ba_407b_ab58_82eed386edb2_ctl00_wpCajaBusqueda_csr_SearchLink"]')))\
    .click()
# Crear listas vacías para almacenar información
titulo =list()
fecha=list()
# Navegación en páginas MIIG y capturar informaciòn en dataframe
numpag = int(input("Ingrese el número de recursos identificados por el buscador: "))# Número de páginas que serán consultadas
numpag = round(numpag/20)
# En caso de obtener menos de 21 recursos asignar número 1
if numpag <= 20:
	numpag=1
	
print("Inicia exploración en página 1")
for i in range(1,numpag+1,1):
    if i <= numpag+1:
        time.sleep(3)
        print('Explorando página: ', i+1)
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, 'ms-srch-group-content')))
        texto_busqueda = driver.find_element_by_class_name('ms-srch-group-content')
        texto_busqueda = texto_busqueda.text
        texto_col = texto_busqueda.split('\n')
        for i in range(0, len(texto_col), 3): # Salto de 3 dado que las variables
            titulo.append(texto_col[i])       # organizan de la forma:
            fecha.append(texto_col[i + 1])    # Título, Fecha, Texto con hipervínculo ver elemento
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PageLinkNext"]'))).click()
        time.sleep(3)
        df = pd.DataFrame({'Título': titulo, 'Fecha': fecha, 'Buesqueda por:': 'Hidrogeología'})
# Cerrar navegador, imprimir resultados y guardarlos en archivo .csv
driver.quit()
print(df)
df.to_csv('ConsultaMIIG.csv',index=False,sep='|')
