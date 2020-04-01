# import pandas as pd
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime
from selenium import webdriver


# from selenium.webself.driver.common.keys import Keys

class InfoJob:

    print("entrei!")
    
    def __init__(self, email, senha, vaga):

        print ("\nBem-vinda! Vamos começar?! \n")
        dirpath = os.getcwd()
        print ("current directory is : " + dirpath)
        chromepath = dirpath + '/assets/chromedriver.exe'

        # it will disable any unexpected noification
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option ("prefs", prefs)
        self.driver = webdriver.Chrome (executable_path=chromepath, chrome_options=chrome_options)

        self.driver.get ('https://www.infojobs.com.br/login.aspx?vurl=%2fcandidate%2f')

        self.vaga = vaga

        try:
            # enter username and password
            self.username = self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtLogin"]')
            self.username.send_keys (email)
            self.password = self.driver.find_element_by_xpath ('//*[@id="ControlLogin_txtPwd"]')
            self.password.send_keys (senha)
            self.entry_button = self.driver.find_element_by_xpath ('//*[@id="ControlLogin_btnValidar"]')
            self.entry_button.click ()
        except:
            print ('Não foi possível fazer o longin!')

    # unexpected notifications

    def vacancy_search(self):

        print('Vamos encontrar uma vaga')

        try:
            # type the vacancy ------------> either user enter or a GUI could be used
            self.vacancy = self.driver.find_element_by_xpath(
                '//*[@id="aspnetForm"]/div[3]/div[6]/section[1]/div/div/ol/li[1]/input')

            self.vacancy.send_keys(self.vaga)
            self.search = self.driver.find_element_by_xpath(
                '//*[@id="aspnetForm"]/div[3]/div[6]/section[1]/div/div/ol/li[3]/button')
            self.search.click()
        except:
            print ('Não consegui procurar emprego!')

    # filter by cities, level and salary ---> it shouldn't be here. A GUI might be a better option

    def filtering(self):
        # filtering by State
        self.state = self.driver.find_element_by_link_text ('Santa Catarina')
        self.state.click ()
        # PROBLEM: I can't click on the one that came by default

        # filtering by salary rate
        self.salary = self.driver.find_element_by_partial_link_text ('5.000,00')
        self.salary.click ()
        # list the ones in the current page

        # job_list = self.driver.find_elements_by_class_name('vagas').find_elements_by_partial_link_text('https')

        # job_list = self.driver.find_elements_by_class_name('vagas').find_elements_by_xpath("//a[@href]")

        # sleep to make sure everything loads, add random to make us look human.

        time.sleep (random.uniform (2.5, 3.5))

    def apply(self):

        self.job_list = self.driver.find_elements_by_class_name ('location2')
        jobs_applied = 0

        for link in self.job_list:
            button = self.driver.find_element_by_link_text ('Assine aqui!')

            if button is not False:
                next
            else:
                self.apply_button = self.driver.find_element_by_xpath (
                    '//*[@id="ctl00_phMasterPage_cHeader_lnkCandidatar"]')
                self.apply_button.click ()
                time.sleep (random.uniform (2, 3.5))
                jobs_applied += 1

email = input("Seu email: ")
senha = input("Sua senha: ")
vaga = input("Vaga: ")
teste = InfoJob(email, senha, vaga)

# PROBLEMA: PODE HAVER MAIS UMA PÁGINA PEDINDO TEMPO DE EXPERIENCIA
# NESTE CASO VALE A PENA VOLTAR E IR PARA A PROXIMA VAGA

# save the ones we applied in a csv file--> SCRAPPY data here
# id, vaga, dia que aplicamos, empresa, onde

# go to the next page
# list and apply
# save it




# primeira urls (77,74,70 são filtros que colocamos no site paranao temos que filtrar aqui, por enquanto)
# url_infojobs_1pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Campo=griddate&Orden=desc&isr=4"
# url_infojobs_2pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Page=2&Campo=griddate&Orden=desc&isr=4"
# url_infojobs_3pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Page=3&Campo=griddate&Orden=desc&isr=4"
#
# #list_urls = pd.read_table("ignore.txt")
# list_urls = [url_infojobs_1pg, url_infojobs_2pg, url_infojobs_3pg]
#
# # csv
# filename = "vagas.csv"
# f = open(filename, "w")
# # os titulos
#
# headers = "vaga,empresa,area,data,cidade,estado,fonte,link\n"  # csv sao definidos pelo \n
# f.write(headers)
#
# for job in list_urls:
#     # pagina 2 :
#
#     # opening upconnection, grabbing the page
#     uClient = uReq(job)
#     page_html = uClient.read()
#     uClient.close()  # fecha o pedido anterior qndo eu terminar
#
#     # html parsing
#     page_soup = soup(page_html, "html.parser")
#
#     # grabs each vacancy
#     containers = page_soup.findAll("div", {"class": "element-vaga"})
#
#     for container in containers:
#         # VAGA
#         vaga_container = container.findAll("div", {"class": "vaga"})
#         vaga = vaga_container[0].text.strip()
#
#         # EMPRESA
#         empresa_container = container.findAll("div", {"class": "vaga-company"})
#         empresa = empresa_container[0].text.strip()
#
#         # AREA
#         area_container = container.findAll("p", {"class": "area"})
#         area = area_container[0].text.strip()
#
#         # DATA
#         data_container = container.findAll("span", {"class": "data"})
#         data = data_container[0].text.strip()
#         data = data[0:5]
#
#         # CIDADE
#         cidade_container = container.findAll("p", {"class": "location2"})
#         cidade = cidade_container[0].text.strip()
#         cidade = cidade.replace("\n", "")
#         cidade = cidade[-24:-6]
#
#         # ESTADO
#         estado_container = container.findAll("p", {"class": "location2"})
#         estado = estado_container[0].text.strip()
#         estado = estado.replace("\n", "")
#         estado = estado[-3:-1]
#
#         #  DESCRIÇÃO
#         atividade_container = container.findAll("div", {"class": "vagaDesc"})
#         atividade = atividade_container[0].text.strip()
#         atividade = atividade.replace("\n", "")
#         # list(set(atividade.split()))  #Isto gera uma lista com as unique words mas  nesse csv não vale a pena
#
#         # LINK
#         link_container = container.findAll("div", {"class": "vagaDesc"})
#         link = link_container[0].a["href"]
#
#         fonte = "INFOJOBS"
#
#         print("Vaga: " + vaga)
#         print("Empresa:" + empresa)
#         print("Area: " + area)
#         print("Data: " + data)
#         print("Cidade: " + cidade)
#         print("Estado: " + estado)
#         print("Atividade: " + atividade)
#         print("Link: " + link)
#
#         f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",", "|") +
#                 "," + data + "," + cidade + "," + estado + "," + fonte + "," + link + "\n")
#         # f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",","|") + "," + data + "," + local.replace("-",",") + "," + atividade.replace(",", "|") + "," + link + "\n")
# f.close()
#
# # PARA RODAR: abra um cmd faça o path usando cd PycharmProjects e depois escreva
# # python real.py quando chegar na pasta
