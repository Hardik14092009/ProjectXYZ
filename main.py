import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import urllib.parse




urls = ['https://thepiratebay.org/', 'https://yts.mx/', 'https://1337x.to/', 'https://rarbg.to/', 'https://nyaa.si/', 'https://torrentz2.is/', 'https://eztv.io/', 'https://www.limetorrents.info/', 'http://fitgirl-repacks.site/', 'http://tamilrockers.ws/', 'https://www.utorrent.com/']



chrome_options = Options()
chrome_options.add_experimental_option( "prefs", {'safebrowsing.enabled':1})
driver = webdriver.Chrome("path of chromedriver", chrome_options=chrome_options)
driver.get('https://www.bing.com/')
print(driver.current_window_handle) 

##print(myvar)
while True:
      tabs = driver.window_handles
      
      
      url = driver.current_url
      driver.switch_to_window(tabs[0])
      
      url1 = str(url)
     
      burls0 = "https://www.youtube.com/results?search_query=hitesh+ks"
      burls1 = "https://www.youtube.com/results?search_query=technical+guys+gaming"
      
      


 
   
      if url1.startswith(urls[0]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[1]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[2]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[3]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[4]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[5]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[6]):
         print ("after if burls == url:")
         driver.get('file:///C:/Users/bassi/source/repos/Block%20URL/Block%20URL/WebPage1.html')

      elif url1.startswith(urls[7]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[8]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[9]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')

      elif url1.startswith(urls[10]):
         print ("after if burls == url:")
         driver.get('https://www.bing.com/')
      
      
          

      elif url1.startswith("http:"):
          print(url1)
          driver.get("https://www.bing.com/")
      
      

      
         
         
          
          
         
             


          
  



    
