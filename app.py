from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import chromedriver_binary
import boto3
import time 
from datetime import datetime,timedelta
import sys
from flask import Flask, request
import utils

app = Flask(__name__)

@app.route('/ss/chrome')
def test_chrome_screenshot(): 
    url = request.args.get('url')
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    outputUrl=utils.takeSS(driver,url,"chrome")    
    return outputUrl

@app.route('/ss/firefox')
def test_firefox_screenshot():  
    url = request.args.get('url')
    firefox_options=FireOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox") 
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument('--start-maximized')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options)
    outputUrl=utils.takeSS(driver,url,"firefox") 
    return outputUrl

@app.route('/')
def homePage():    
    return "home page"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
    