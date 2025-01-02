from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time

# Configura o driver do Chrome (garanta que o chromedriver esteja no PATH ou forneça o caminho correto)
driver_path = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Lista de URLs do Rickroll (vídeo no YouTube)
rickroll_url = "https://youtu.be/xvFZjo5PgG0?si=XWSkMjKNEUMXs6hP"

# Abre 5 abas tocando Rickroll
for i in range(5):

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1]) 
    driver.get(rickroll_url)  


    try:
        play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-play-button")
        play_button.click()  
    except Exception as e:
        print(f"Erro ao tentar clicar no botão play: {e}")


    time.sleep(2)

# Aguarda 10 segundos antes de fechar todas as abas
time.sleep(7)


driver.quit()
