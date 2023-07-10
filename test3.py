import sys

POST = sys.argv[1]
LOC = sys.argv[2]

#print("<p class='sdata'>",POST,"@", LOC , "</p>")

# In[58]:


import requests
from bs4 import BeautifulSoup
import csv


def make_url(position, location):
    #Generate url from position and location
    template = 'https://www.simplyhired.co.in/search?q={}&l={}&job=uPhbJZ8DYOvnMNVtSB_uUmDvvWBaJAkRNnDuiev56yne6FeW3ySSYA'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    return url
    print(url)
    


url=make_url(POST, LOC)
#print(url)
#print(url)
#print(url)


# In[59]:


r=requests.get(url)
#print(url)
htmlCont=r.content
#print(htmlCont)


# In[60]:


soup=BeautifulSoup(htmlCont , 'html.parser')
#print(soup.prettify)


# In[61]:


posts=[]
company=[]
details=[]


# In[62]:


for el in soup.find_all('h3', attrs={'class': 'jobposting-title'}):
        #print("#",el.get_text())# job details
        posts.append(el.get_text())
for el in soup.find_all('div', attrs={'class': 'jobposting-subtitle'}):
        #print("#",el.get_text())# job details
        company.append(el.get_text())
for el in soup.find_all('div', attrs={'class': 'SerpJob-snippetContainer'}):
        #print("#",el.get_text())# job details
        details.append(el.get_text())


# In[63]:


print(len(posts))
print(len(company))
print(len(details))


# In[64]:


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

