import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import urllib.parse
#It is nessesary that you have chrome already installed
url = "http://data.phishtank.com/data/0ddf0d53ab0561d772c99f95439fb9af535e795e5fba5985d57f800ed7e5f11b/online-valid.json.bz2"


urls = ['https://thepiratebay.org/', 'https://yts.mx/', 'https://1337x.to/', 'https://rarbg.to/', 'https://nyaa.si/', 'https://torrentz2.is/', 'https://eztv.io/', 'https://www.limetorrents.info/', 'http://fitgirl-repacks.site/', 'http://tamilrockers.ws/', 'https://www.utorrent.com/']




chrome_options = Options()
chrome_options.add_experimental_option( "prefs", {'safebrowsing.enabled':1})
driver = webdriver.Chrome("path of chromedriver.exe", chrome_options=chrome_options)
driver.get('https://www.bing.com/')
##print(myvar)
while True:
    
      
      url = driver.current_url
      
      url1 = str(url)
     
      burls0 = "https://www.youtube.com/results?search_query=hitesh+ks"
      burls1 = "https://www.youtube.com/results?search_query=technical+guys+gaming"
      
      


 
   
      if urls[0] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[1] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[2] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[3] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[4] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[5] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[6] == url1:
          print ("after if burls == url:")
          driver.get('file:///C:/Users/bassi/source/repos/Block%20URL/Block%20URL/WebPage1.html')

      elif urls[7] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[8] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[9] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')

      elif urls[10] == url1:
          print ("after if burls == url:")
          driver.get('https://www.bing.com/')
      
      
          

      elif url1.startswith("http:"):
          print(url1)
          driver.get("https://www.bing.com/")
      
      

      
         
         
          
          
         
             


          
  



    
