# import os
# import re
# import ast
# import random
# import time
# import pandas as pd
# from fake_useragent import UserAgent
# #selenium libraries
# from selenium.webdriver.common import keys
# import undetected_chromedriver as uc
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException   
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from selenium.webdriver.chrome.options import Options
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process


# def delay ():
#     time.sleep(random.randint(2,3))

# with open(r'statics\text\proxyscrape_premium_http_proxies.txt', 'r') as p:
#     lister = p.readlines()

# with open(r'statics\text\email_list.txt', 'r') as p:
#     all_cred = p.readlines()
# email_lister = []
# for lin in all_cred:
#     email_lister.append(list(lin.split(", ")))

# cuurent_alias = random.choice(email_lister)[0]

# # account credentials
# username = 'opeyemitester@gmail.com'
# user_alias = f'opeyemitester+{cuurent_alias}@gmail.com'
# password = "Horlaolu"

# def start_driver():
#     global driver
#     try:
#         options = uc.ChromeOptions()
#         # setting profile
#         # another way to set profile is the below (which takes precedence elif both variants are used
#         options.add_argument(f'--user-data-dir={os.getcwd()}\\profiles\\profile1')
#         # just some options passing in to skip annoying popups
#         options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
#         options.add_experimental_option('prefs', {
#         "download.default_directory": f'{os.getcwd()}\\statics\\pdfs', #Change default directory for downloads
#         "download.prompt_for_download": False, #To auto download the file
#         "download.directory_upgrade": True,
#         "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
#         })
#         # options.add_argument('--headless')
#         headless_proxy = "http://127.0.0.1:3128"
#         other_proxy = 'http://'+'38.15.152.4:3128'
#         # other_proxy = "http://" + ip
#         # print(ip)
#         options.add_argument(f'--proxy-server={headless_proxy}')   
#         #create chrome driver
#         # ua = UserAgent()
#         # ua.update()
#         # userAgent = ua.random
#         # print(userAgent)
#         # options.add_argument(f'user-agent={userAgent}')
#         driver = uc.Chrome(options=options)
#         driver.maximize_window()
#         delay()
#         return driver
#     except Exception as chromedriver_error:
#         print(chromedriver_error)
# def main():
#     link1 = 'https://e-services.acceo.com/immosoft/controller/ImmoNetPub/U4051/trouverParAdresse?fourn_seq=47'

#     driver = start_driver()
#     driver.get(link1)
#     try:
#         second_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='Find-3']/a")))
#         second_link.click()
#     except Exception as e:
#         print(e)
#         driver.quit()

#     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'ty_rapport_eval'))).click()
#     search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'NoCadastre')))
#     search.send_keys('4270728')
#     # check if search button clicks
#     # time.sleep(3000)
#     delay()
#     try:
#         search_btn = driver.find_element(By.XPATH,"//button[@id='btnSearch']")
#         search_btn.click()
    
#         delay()
#         driver.find_element_by_xpath('/html/body/form/div[1]/div/div/div[3]/div/div[3]/div/div[2]/fieldset[2]/table/tbody/tr/td[2]/a').click()
#     except NoSuchElementException as e:
#         print(e)
#         driver.quit()
        
#     time.sleep(3000)

# if __name__ == '__main__':
#     main()

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

d = list(set(PRIMES))
print(d)

# t = [9]*10

# def is_prime(n, t):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True, t

# def main():
#     with concurrent.futures.ProcessPoolExecutor(5) as executor:
#         s = executor.map(is_prime, PRIMES, t)
#         for r in s:
#             print(r)
        
#         # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#         #     print('%d is prime: %s' % (number, prime))

# if __name__ == '__main__':
#     main()