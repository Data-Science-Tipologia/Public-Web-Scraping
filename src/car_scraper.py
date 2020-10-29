import urllib.request
import time
from joblib import Parallel, delayed
from bs4 import BeautifulSoup
import pandas as pd
import requests
import builtwith
import whois
import csv
import re
import concurrent.futures
import validators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_data(cars_in_page):
    """
    Input / Output Operations.
    :param cars_in_page:
    :return:
    """
    # I/O Section
    df = pd.DataFrame.from_records(
        [elem.to_dict() for elem in cars_in_page])
    with open('data.csv', 'a') as f:
        df.to_csv(f, header=False, index=False, line_terminator='\n')
        f.close()


class Car:
    def __init__(self, update=None, model=None, class_=None, price=None,
                 cant_km=None, fuel=None, cv=None, location=None, year=None):
        self.update = str(update)
        self.model = str(model)
        self.class_ = str(class_)
        self.price = str(price)
        self.cant_km = str(cant_km)
        self.fuel = str(fuel)
        self.cv = str(cv)
        self.location = str(location)
        self.year = str(year)

    def to_dict(self):
        return {
            'update': self.update,
            'model': self.model,
            'class_': self.class_,
            'price': self.price,
            'cant_km': self.cant_km,
            'fuel': self.fuel,
            'cv': self.cv,
            'location': self.location,
            'year': self.year
        }

class CarsScraper:

    def __init__(self, url):
        self.url = url
        self.user_agent = 'Chrome/86.0.4240.111'
        self.headers = {'User-Agent': self.user_agent
                        }
        self.news = 'Nuevos'
        self.km0 = 'Km 0'
        self.second = 'Segunda mano '

    def din_scraper(self, url):
        """Return the Browser Driver"""

        opts = Options()
        opts.add_argument(self.user_agent)

        browser = webdriver.Chrome(options=opts)


        try:
            browser.get(url)
            time.sleep(3)

            cookies_button = WebDriverWait(browser,
                                           20).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="CybotCookiebotDialogBodyButtonAccept"]')))

            cookies_button.click()

        except :
            print("Error in link : {}".format(url))
            return browser

        return browser

