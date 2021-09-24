#!/usr/bin/env python
# coding: utf-8
# email notification 
# case 1 :  ahr999 <=0.45, send email daily
# case 2 : ahr999 indicator weekly
# usage: all in ETH when case 1
# 17 Jul 2021, HangZhou
# In crypto we trust 
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import date,datetime
from pyvirtualdisplay import Display
sender = 'Orochi1972@126.com'
receivers = ['orochi1972@163.com']
def send_email(body_of_email,subject):
    body_of_email = body_of_email
    subject =subject

    msg = MIMEText(body_of_email,'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    s = smtplib.SMTP_SSL(host = 'smtp.126.com', port = 465)
    s.login(user = sender, password = 'TFNSPLCBLDARZYGO')
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
def get_indicator():
    display = Display(visible=0,size=(1366,768))
    display.start()
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://ahr999.com/")
    strhtml = browser.page_source
    browser.quit()
    display.stop()
    try:
        soup=BeautifulSoup(strhtml,'lxml')
        data =str(soup.find_all('tspan')[0])
        number = float(data.split(' ')[1].split('指数')[1])
    except Exception as e:
        send_email('e','it seems somthing wrong with the ahr999.com')
    return number

if __name__ == '__main__':
    weekday = datetime.now().isoweekday()
    ind = get_indicator()
    if weekday ==7 and ind>0.45:
        title= 'weekly ahr999 indicator notification'
        body = 'current ahr999 is '+str(get_indicator())
        send_email(body,title)
    if ind<=0.45:
        title = 'Time to buy the dip of the year'
        body = 'current ahr999 is '+str(get_indicator())
        send_email(body,title)

