#/usr/bin/env python3.8
#Debes abrir el enviroment, obvio. Esto abre una pagina en chronium/chrome (who knows)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from secrets import email, psw
from time import sleep

#might use later: window1 = driver.window_handles[0] ubica las multiples ventanas

class dopeBot():
    actions_list = list
    def __init__(self):
        self.browse = webdriver.Chrome(PATH)
        self.browse.get('https://discord.com/login')
        self.login()
        sleep(6)
        self.close_pops()

    def login(self):
        #Getting elements
        while True:
            try:
                email_textbox = self.browse.find_element_by_name('email')
                pasw_textbox = self.browse.find_element_by_name('password')
                login_button = self.browse.find_elements_by_tag_name('button')
                break
            except:
                pass
        #Set and click
        email_textbox.send_keys(email)
        pasw_textbox.send_keys(psw)
        login_button[1].click()
    
    def close_pops(self):
        for i in range(2):
            try:
                self.browse.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[1]/div').click()
            except:
                sleep(4)

    def actions(self, to_do, type_):
        if type_ == 0:
            click = self.browse.find_element_by_xpath(to_do[0]).click()
            sleep(1.5)
            try: 
                self.browse.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[4]/div/div[4]/div/div[2]').click()
            except:
                sleep(1)
            self.browse.find_element_by_xpath(to_do[1]).send_keys(to_do[2] + Keys.ENTER)
            

def desicion(do):
    if do == 1:
        #Mensaje a un amigo
        mensaje = input('Mensaje: ')
        friend = int(input('0. Alguien | 1. Alguien mas | 2. You know it'))
        if friend < 3 and friend > -1:
            list_do = (friends_xpath[friend], main_textbar, mensaje)
            bot.actions(to_do = list_do, type_ = 0)
        else: 
            print('Numero ingresado no valido')
        del friend, mensaje
    elif do > 2:
        print('Numero no valido')


        

def new_action():
    while True:
        print('ACCIONES:')
        print('1. Mensaje a un Amigo')
        print('2. Spamear chat con Alejo')
        print('3. Salir')
        action = int(input('¿Qué deseas hacer?: '))
        if action == 3: 
            break
        desicion(action)


if __name__ == '__main__':
    #Aquí en PATH ingresar la ubicación del archivo ".../chromedriver.exe"
    PATH = ''
    bot = dopeBot()
    print('Llegamos aca')
    main_textbar = '/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[3]/div[2]'
    #ES NECESARIO ACTUALIZAR ESTE XPATH
    friends_xpath = ('/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/a[4]/div', '/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/a[8]/div', '/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/a[7]/div')
    new_action()