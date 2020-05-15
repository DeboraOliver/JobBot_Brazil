# JobBot_Brazil

A bot to automatize job application.


## Overview

Why should we spend time applying to a hundreds of vacancies  instead of enjoying time with our relatives? This bot save your time!

It is designed for a speficic website. This bot has two main part: real.py, controls bot actions and, jobdetails.py that collects details of each job our bot applyed for.

This script and some comments are in the client's native language.

## 1. Requirements

### 1.1 real.py

To this script you need the following packages:

```
import time, random, os, csv, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import jobdetails
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
```

### 1.2 jobdetails.py

To run this project you need the following packages:

```
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime
```

