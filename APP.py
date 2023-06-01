#utilisation de Selenium pour ouvrir une page web, cliquer sur un élément et récupérer des données :

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Spécifier le chemin du fichier chromedriver.exe
driver = webdriver.Chrome('C:/chromedriver.exe')

# Ouvrir la page web
driver.get('https://www.example.com')

# Cliquer sur un élément de la page
element = driver.find_element_by_xpath("//a[@href='/some-page']")
element.click()

# Attendre que la nouvelle page soit chargée
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))

# Récupérer des données depuis la page
heading = driver.find_element_by_xpath("//h1").text
paragraphs = driver.find_elements_by_xpath("//p")

# Afficher les données récupérées
print(heading)
for p in paragraphs:
    print(p.text)

# Fermer le navigateur
driver.quit()
