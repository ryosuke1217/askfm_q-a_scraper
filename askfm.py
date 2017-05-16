# coding:utf-8
from __future__ import print_function
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from ast import literal_eval
from time import sleep
from bs4 import BeautifulSoup
import sys
import urllib.request
from http.client import BadStatusLine
from http.client import IncompleteRead
import codecs
import datetime

args = sys.argv
word = args[1]

driver = webdriver.Chrome()

driver.get("https://ask.fm/" + word)

judge = 10000000
while True:
    scroll_h = driver.execute_script("var h = window.pageYOffset; return h")
    if scroll_h != judge:
        judge = driver.execute_script("var m = window.pageYOffset; return m")
        previous_h = driver.execute_script("var h = window.pageYOffset; return h")
        #スクロール
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        after_h = driver.execute_script("var h = window.pageYOffset; return h")
        if previous_h == after_h:
            break
print('load complete')

page_source = driver.page_source

questions = driver.find_elements_by_class_name("streamItemContent-question")
answers = driver.find_elements_by_class_name("answerWrapper")

qas = [(q.find_element_by_tag_name('h2').text, a.find_element_by_tag_name('p').text) for q, a in zip(questions, answers)]

print('find complete')

with codecs.open('data/askfm_data_' + word + '.txt', 'w', 'utf-8') as f:
    for q, a in qas:
        if q == '' or a == '' or 'http' in q or 'http' in a:
            continue
        q = q.replace('\n', '')
        a = a.replace('\n', '')
        f.write(q)
        f.write('\n')
        f.write(a)
        f.write('\n')
        f.write('\n')

driver.quit()
