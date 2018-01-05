import requests
import smtplib
from bs4 import BeautifulSoup
import re
def top_trending():
        news=[]
        url='https://in.reuters.com/news/top-news'
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        links=soup.find_all(href=re.compile('/article/'))
        news=[]
        for i in links:
                if(i.text=='Continue Reading'):
                        pass
                else:
                        news.append(i.text)
        return news
news=top_trending()
news.pop()
news.pop()
message=''
for i in news:
        message+=i+'\n'
print message
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("<mail id>", "<pass>")
 
# message to be sent
#message = "Check 1 2 3 !"
 
# sending the mail
s.sendmail("<Sender>", "<Reciever>", str(message))
 
# terminating the session
s.quit()
