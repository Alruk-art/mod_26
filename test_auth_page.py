#python -m pytest -v --driver Chrome --driver-path c://brodriver/chromedriver
# cd C:\pythonProject\SF_mod_26\un262
import os
from pages1.a_p import AuthPage
import time


def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("email@gmail.com")
   page.enter_pass("pass")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() != '/all_pets', "login error"

def test_auth_page_2(selenium):
   page = AuthPage (selenium)
   page.enter_email ("al66@pf.com")
   page.enter_pass ("1qasw2")
   page.btn_click ()

   assert page.get_relative_link () == '/all_pets', "login valid"

   time.sleep(5) #задержка для учебных целей