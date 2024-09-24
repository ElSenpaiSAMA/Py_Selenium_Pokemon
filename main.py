#librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#establezco las opciones del navegador
opciones = Options()
opciones.add_experimental_option("detach", True)

#pongo la ubicacion de mi chromedriver
crdriver = 'C:\\Users\\mnico\\chromedriver\\chromedriver.exe'

ser = Service(crdriver)

driver = webdriver.Chrome(service=ser, options=opciones)

#establezo mi URL
driver.get('https://www.wikidex.net/wiki/WikiDex')

#busco charizard y hago click en el boton
buscar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#searchInput"))
)
buscar.send_keys("charizard")

boton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input#mw-searchButton"))
)
boton.click()
#hago click en el boton
boton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span.searchmatch"))
)
boton.click()
#busco blastoise
buscar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#searchInput"))
)
buscar.send_keys("Blastoise" + Keys.RETURN)
#extraigo informacion sobre blastoise
extraer = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#mw-content-text div.mw-parser-output p"))
)
#creo archivo con la informacion extraida
with open('Blastoise.txt', 'w', encoding='utf-8') as file:
    for index, parrafo in enumerate(extraer):
        file.write(f"{parrafo.text}\n")
        index += 1

#cierro navegador
driver.quit()
