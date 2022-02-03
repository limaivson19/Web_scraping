import time
import serial
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

ser = serial.Serial('COM9', 9600, timeout=1)

url = 'https://ge.globo.com/futebol/times/palmeiras/'

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="glb-main-home"]/div[2]/div/div/div/div/div/div/a/ul/li[1]').click()
placar_atual = 0
while True:
    time.sleep(2)
    mandante = driver.find_element(By.XPATH,
                                   '//*[@id="transmissao"]/div/div/section[1]/article/article[1]/header/h1').text
    placar_mandante = driver.find_element(By.XPATH,
                                          '//*[@id="transmissao"]/div/div/section[1]/article/article[1]/div[1]/strong').text

    visitante = driver.find_element(By.XPATH,
                                    '//*[@id="transmissao"]/div/div/section[1]/article/article[2]/header/h1').text
    placar_visitante = driver.find_element(By.XPATH,
                                           '//*[@id="transmissao"]/div/div/section[1]/article/article[2]/div[1]/strong').text

    if mandante == 'PALMEIRAS':
        print(placar_mandante)
        placar = int(placar_mandante)

        if placar > placar_atual:

            placar_atual += 1
            cont = 0
            while cont < 3:
                ser.write(b'p')
                ser.readlines()
                cont += 1

            ser.write(b'0')
            ser.readlines()

    if visitante == 'PALMEIRAS':
        print(placar_visitante)
        placar = int(placar_visitante)
        if placar > placar_atual:
            placar_atual += 1
            cont = 0
            while cont < 3:
                ser.write(b'p')
                ser.readlines()
                cont += 1

            ser.write(b'0')
            ser.readlines()

driver.quit()
