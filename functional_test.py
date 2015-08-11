from selenium import webdriver

###Connects to the internet browser and travels to Shownoterco

br = webdriver.Safari()
br.get('http://localhost:5000')
