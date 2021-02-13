from bs4 import BeautifulSoup
import pandas as pd
data=pd.read_excel('/home/bharat/Downloads/data_refined.xlsx')
def soup1(browser,i):
    
        try :
            browser.cookies.delete()
            browser.reload()
        except:
            print('sleeping for 60 seconds')
            time.sleep(15)
            print('reloading browser')    
            soup1(browser,i)
        browser.find_by_id('baidu_translate_input').fill( i)
        time.sleep(12)
        # Find and click the 'search' button
        #a=browser.find_by_css('div[class="ordinary-output target-output clearfix"]:nth-child(1)')
        # Interact with elements
    #     button.click()
    #     if browser.is_text_present('splinter.readthedocs.io'):
    #         print("Yes, the official website was found!")
    #     else:
    #         print("No, it wasn't found... We need to improve our SEO techniques")
    #     find_h=browser.find_by_css('div[class="ordinary-output target-output clearfix"]:nth-child(1) > div:nth-child(1) > p')
    #     for i in find_h: print(i.outerText)
        a=browser.html
        s=BeautifulSoup(a)
        return [s.findAll("p", {"class": "ordinary-output target-output clearfix"}),browser]
import time 
from splinter import Browser
browser=Browser('firefox',retry_count=3) 
# Visit URL
url = "https://fanyi.baidu.com/"
 # Visit URL
browser.visit(url)
list1=[]
for i in  data.Description:
#     with Browser('firefox') as browser:

#         # Visit URL
# #         url = "https://fanyi.baidu.com/#en/zh/"
# #         browser.visit(url)
# #         browser.find_by_id('baidu_translate_input').fill( i)
#         time.sleep(10)
        # Find and click the 'search' button
        #a=browser.find_by_css('div[class="ordinary-output target-output clearfix"]:nth-child(1)')
        # Interact with elements
    #     button.click()
    #     if browser.is_text_present('splinter.readthedocs.io'):
    #         print("Yes, the official website was found!")
    #     else:
    #         print("No, it wasn't found... We need to improve our SEO techniques")
    #     find_h=browser.find_by_css('div[class="ordinary-output target-output clearfix"]:nth-child(1) > div:nth-child(1) > p')
    #     for i in find_h: print(i.outerText)
        t=soup1(browser,i)
        browser=t[1]
        t=t[0]
        while(t==[]):
            time.sleep(15)
            
            print('reconsidering',t)
            t=soup1(browser,i)[0]
#         a=browser.html
#         s=BeautifulSoup(a)
        text=t[0].text
        list1.append(text)
data=pd.DataFrame(list1,columns=['Translated'])
data.to_excel('translated.xlx')
