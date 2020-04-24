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

        # it will disable any unexpected notification
        chrome_options = webdriver.ChromeOptions ()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option ("prefs", prefs)
        self.driver = webdriver.Chrome (executable_path=chromepath, options=chrome_options)

        self.driver.get ('https://www.infojobs.com.br/login.aspx?vurl=%2fcandidate%2f')

        # username and password
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtLogin"]').send_keys (email)
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtPwd"]').send_keys (senha)
        self.driver.find_element_by_xpath ('//*[@id="ControlLogin_btnValidar"]').click ()

        self.vacancy_search(vaga)

    # CLIENT MIGHT WANT TO APPLY USING A RANGE OF JOB TITLES ----> Loop over a list

    def vacancy_search(self, vaga):
        print ('Vamos encontrar uma vaga')

        # type the vacancy ------------> either user enter or a GUI could be used
        self.driver.find_element_by_xpath ('//*[@id="aspnetForm"]/div[3]/div[6]/section[1]/div/div/ol/li[1]/input').send_keys(vaga)

        self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/div[6]/section[1]/div/div/ol/li[3]/button').click ()
        self.filtering (Estado)

        # filter by cities, level and salary ---> it shouldn't be here. A GUI might be a better option

    def filtering(self,Estado):
        try:
            # filtering by State ----> state should be a variable 
            self.driver.find_element_by_link_text (Estado).click ()
            # we don't wanna work in SP right?!
            #self.driver.find_element_by_link_text ('São Paulo').click ()
            # PROBLEM: I can't click on the one that came by default
            time.sleep (random.uniform (2.5, 4.5))
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

        jobs_attempts = 0
        jobs_applied = 0

        for url in self.links_job:
            print(url)
            self.driver.get(url)

            try:
                self.driver.find_element_by_class_name ('Limited')
                print ("Vaga só para assinantes!")
                jobs_attempts += 1
                time.sleep (random.uniform (2, 3))
                pass
            except:
                self.driver.find_element_by_xpath ('//*[@id="ctl00_phMasterPage_cHeader_lnkCandidatar"]').click ()
                time.sleep (random.uniform (1, 2.5))

                try:
                    self.driver.find_element_by_xpath ('//*[@id="ctl00_phMasterPage_btnInsertMatch"]')
                    print ("Desta vez não deu")
                    jobs_attempts += 1
                    time.sleep (random.uniform (1.5, 2.5))
                    pass
                except:
                    app = jobdetails.WebScrapJob (url)
                    print ("Candidatura realizada!")
                    jobs_applied += 1
                    time.sleep (random.uniform (2.5, 3.5))

        print("Deram certo: " + str(jobs_applied))
        print("Nao deu certo: " + str(jobs_attempts))


email = input ("Seu email: ")
senha = input ("Sua senha: ")
estado = input("Estado: ")
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
