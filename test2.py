import sys

POST = sys.argv[1]
LOC = sys.argv[2]

#print("<p class='sdata'>",POST,"@", LOC , "</p>")


# In[1]:


import requests
from bs4 import BeautifulSoup
import csv

def make_url(position, location):
    """Generate url from position and location"""
    template = 'https://in.talent.com/jobs?context=&k={}&l={}&id=98b2c54cce18'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    return url
    #print(url)
    


#make_url("web", "nashik")
url=make_url(POST, LOC)
#print(url)
#print(url)
#print(url)


# In[2]:


r=requests.get(url)
#print(url)
htmlCont=r.content
#print(htmlCont)


# In[3]:


posts=[]
company=[]
details=[]


# In[4]:


soup=BeautifulSoup(htmlCont , 'html.parser')
#print(soup.prettify)
for el in soup.find_all('div', attrs={'class': 'card__job-c'}):
        #print("#",el.get_text())# job details
        details.append(el.get_text())

#print(details)


# In[5]:


for el in soup.find_all('h2', attrs={'class': 'card__job-title card__job-link gojob'}):
        #print("#",el.get_text())
        posts.append(el.get_text())
for el in soup.find_all('div', attrs={'class': 'card__job-empname-label'}):
        #print("#",el.get_text())
        company.append(el.get_text())


# In[6]:


print(len(posts))
print(len(company))


# In[7]:


details= [string[:150] for string in details]
#print(details)
new_string=[]
for i in range(0,len(details)):
    details[i] = details[i].replace("\n", "")

for i in range(0,(len(details))):
    details[i]=details[i]+'...'
    
#print(details)
#print(details)


# In[8]:




for i in range(0,len(posts)):
            if(i%2==0):
                print("<div class='jobcard1'>")
            else:                    
                print("<div class='jobcard2'>")
            print("<a href="+url+">")
            print("<h2 class='post'>"+posts[i]+"</h2>")
            print("<h3 class='company'>"+company[i]+"</h3>")
            print("<p class='details'>"+details[i]+"</p>")
            print("</a>")
            print("</div>")    
