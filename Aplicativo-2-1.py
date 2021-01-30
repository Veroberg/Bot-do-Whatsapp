from selenium import webdriver
from time import sleep



wp_link = "https://web.whatsapp.com/"
driver.get(wp_link)
new_msg_button = '//*[@id="side"]/header/div[2]/div/span/div[2]'
contact_field = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
first_contact = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]'

chrome_driver_path = "C:/Users/Verô/Downloads/chromedriver_win32/chromedriver.exe"
msg_type = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
send_messge_button = '//*[@id="main"]/footer/div[1]/div[3]'
driver = webdriver.Chrome(chrome_driver_path)

def procurar_contato(contato):
    new_msg = driver.find_element_by_xpath(new_msg_button)
    new_msg.click()
    sleep(1)
    find_contact = driver.find_element_by_xpath(contact_field)
    find_contact.click()
    find_contact.send_keys(contato)
    sleep(2)
    primeiro_contato = driver.find_element_by_xpath(first_contact)
    primeiro_contato.click()
    sleep(1)
   
def enviar_mensagem(mensagem):    
    digitar_msg = driver.find_element_by_xpath(msg_type)
    digitar_msg.click()
    digitar_msg.send_keys(mensagem)
    sleep(1)
    send_msg = driver.find_element_by_xpath(send_messge_button)
    send_msg.click()
    sleep(2)
    
lista_de_contatos = ['Grup 1','Grup 2','Grup 3','Grup 4']   
lista_de_codigos = ['130','260','940','100'] 
