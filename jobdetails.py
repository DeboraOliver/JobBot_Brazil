"""This script intended to scrape for jobs in a few specific job pages in Brazil.
    It was my very first scrape projects and I had the chance to learn quite a lot"""

# title: Web scrapping for job. Created: February/2020. São Paulo - Brazil


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime


class WebScrapJob:
    def __init__(self, url):
        print (url)
        self.url = url
		# url = "https://www.infojobs.com.br/vaga-de-desenvolvedor-python-junior-em-sao-paulo__6805056.aspx"
        self.uClient = uReq (self.url)
        self.page_html = self.uClient.read ()
        self.uClient.close ()  # fecha o pedido anterior qndo eu terminar

        # html parsing
        self.page_soup = soup (self.page_html, "html.parser")

        # grabs each vacancy
        #self.containers = self.page_soup.findAll ("div", {"class": "element-vaga"}) #NÃO EXISTE
        self.save ()

    def save(self):
        # csv
        self.filename = 'jobs.csv'
        self.f = open (self.filename, "w")

        headers = "vaga,empresa,salário,data,cidade,estado,link\n"  # csv sao definidos pelo \n
        self.f.write (headers)
        self.jobs ()


    def jobs(self):
        #for container in self.containers:
		# VAGA
		self.vaga_page = page_soup.findAll ("span", {"id": "ctl00_phMasterPage_cVacancySummary_litVacancyTitle"})
		self.vaga = self.vaga_page[0].text.strip ()

		# EMPRESA
		self.empresa_page = page_soup.findAll ("a", {"id": "ctl00_phMasterPage_cVacancySummary_aCompany"})
		self.empresa = self.empresa_page[0].text.strip ()

		# Salário
		self.salario_page = page_soup.findAll ("span", {"id": "ctl00_phMasterPage_cVacancySummary_litSalary"}) 
		self.salario = self.salario_page[0].text.strip ()

		# CIDADE
		self.cidade_page = page_soup.findAll ("span", {"id": "ctl00_phMasterPage_cVacancySummary_litLocation"})
		self.cidade = self.cidade_page[0].text.strip () 
		
		# ESTADO
		self.estado_page = page_soup.findAll ("span", {"id": "ctl00_phMasterPage_cVacancySummary_litLocation"})
		self.estado = self.estado_page[0].text.strip ()
		self.estado = self.estado[-3:-1]
		
		# self.estado = self.estado.replace ("\n", "")

		# LINK
		self.link = url

		
		print ("Vaga: " + self.vaga)
		print ("Empresa:" + self.empresa)
		print ("Area: " + self.salario)
		print ("Data: " + self.data)
		print ("Cidade: " + self.cidade)
		print ("Estado: " + self.estado)
		print ("Link: " + self.link)

		self.f.write (self.vaga + "," + self.empresa.replace (",", "|") + "," +  self.salario.replace (",", "|") + "," +  self.data + "," + self.cidade.replace (",", "|") + "," + self.estado + "," +self.link + "\n")
		# f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",","|") + "," + data + "," + local.replace("-",",") + "," + atividade.replace(",", "|") + "," + link + "\n")

	self.f.close ()




