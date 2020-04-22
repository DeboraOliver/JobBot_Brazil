# import pandas as pd
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import jobdetails
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class InfoJob:
    print ("entrei!")

    def __init__(self, email, senha, vaga):
        print ("\nBem-vinda! Vamos começar?! \n")
        dirpath = os.getcwd ()
        print ("current directory is : " + dirpath)
        chromepath = dirpath + '/assets/chromedriver.exe'

        # it will disable any unexpected noification
        chrome_options = webdriver.ChromeOptions ()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option ("prefs", prefs)
        self.driver = webdriver.Chrome (executable_path=chromepath, options=chrome_options)

        self.driver.get ('https://www.infojobs.com.br/login.aspx?vurl=%2fcandidate%2f')

        # self.vaga = vaga  # enter username and password
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtLogin"]').send_keys (email)
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtPwd"]').send_keys (senha)
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_btnValidar"]').click ()

        self.vacancy_search(vaga)

    # CLIENT MIGHT WANT TO APPLY USING A RANGE OF JOB TITLES ----> Loop over a list

    def vacancy_search(self, vaga):
        print ('Vamos encontrar uma vaga')

        # type the vacancy ------------> either user enter or a GUI could be used
        self.driver.find_element_by_xpath ('//*[@id="aspnetForm"]/div[4]/div[6]/section[1]/div/div/ol/li[1]/input').send_keys(vaga)
        #//*[@id="aspnetForm"]/div[4]/div[6]/section[1]/div/div/ol/li[1]/input
        self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/div[6]/section[1]/div/div/ol/li[3]/button').click ()
        self.filtering ()

        # filter by cities, level and salary ---> it shouldn't be here. A GUI might be a better option

    def filtering(self):
        try:
            # filtering by State ----> state should be a variable 
            self.driver.find_element_by_link_text ('Santa Catarina').click ()
            # we don't wanna work in SP right?!
            self.driver.find_element_by_link_text ('São Paulo').click ()
            # PROBLEM: I can't click on the one that came by default
            time.sleep (random.uniform (1.5, 3.5))
            # filtering by salary rate ---> it should be asked
            self.driver.find_element_by_partial_link_text ('5.000,00').click ()
            print ("Filtros online")

        except:
            print ("Não deu para colocar os filtros!")  # message in case of failure

        time.sleep (random.uniform (2.5, 3.5))
        self.apply ()

    # criar uma outra função que puxa a lista de url anteriores e bate com as que temos

    def apply(self):
        # mudar a lista a seguir para que elapegue apenas as vagas que 1 - não foram listadas antes; 2 - que não exijam assinatura

        # lista de vagas na primeira pagina
        elems = self.driver.find_elements_by_css_selector (".vaga [href]")
        self.links_job = [elem.get_attribute ('href') for elem in elems]

        jobs_with_futher_questions = 0
        jobs_applied = 0

        for x in self.links_job:
            print(x)
            x.click()#CHANGE IT

            try:
                url = self.driver.current_url
                print (url)
                time.sleep (random.uniform (1, 2.5))
                # entrar na classe que salva tudo
                app = jobdetails.WebScrapJob (url)
                candidatar = self.driver.find_element_by_id ("ctl00_phMasterPage_cHeader_lnkCandidatar")
                candidatar.click ()
                # HÁ UMA EXCEÇÃO AQUI
                if self.driver.find_element_by_xpath ('//*[@id="ctl00_phMasterPage_btnInsertMatch"]'):
                    print ("Desta vez não deu")
                    jobs_with_futher_questions += 1
                    time.sleep (random.uniform (1.5, 2.5))
                    pass
                else:
                    print ("Candidatura realizada!")
                    jobs_applied += 1
                    print (jobs_applied)
                    time.sleep (random.uniform (2.5, 3.5))

            except:
                self.driver.find_element_by_link_text ('Assine aqui!')
                time.sleep (random.uniform (2, 3))
                print ("Vaga só para assinantes!")
                pass

# TALVEZ SEJA PRECISO CRIAR UMA NOVA CLASSE PARA LIDAR COM OUTRAS EXCESSOES


email = input ("Seu email: ")
senha = input ("Sua senha: ")
# estado = input("Estado: ")
# A list of cities:
# cidade1 = input("Cidades (separedas vírgulas: ")
# cidade = cidade1.split(',')
# A list of job positions you might fit in
vaga = input ("Vaga: ")
# vaga1 = input ("Vagas (separe com vírgula): ")
# vaga = vaga1.split(',')
# print("Suas cidades: ", vaga)
teste = InfoJob (email, senha, vaga)

"""para iniciar no cmd  use 
pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
"""
