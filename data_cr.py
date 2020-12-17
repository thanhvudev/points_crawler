#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


pip install pandas requests bs4


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# In[2]:


import requests
import pandas
import bs4
import numpy as np
from datetime import date
from datetime import datetime


# In[3]:


url = 'http://diemthi.hcm.edu.vn/Home/Show/'
def getPageContent(url, id):
  hd = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Accept-Encoding": "gzip", "Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
  sendData = {'SoBaoDanh':id}
  page = requests.post(url, data=sendData, headers=hd)
  return bs4.BeautifulSoup(page.text,"html.parser")
def calculateAge(birthDate): 
  today = date.today() 
  age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  return age 


# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[ ]:





# In[4]:


def fieldCleaner(field):
    for j in range(len(field)):
        if ((field[j]!='\r')&(field[j]!='\n')&(field[j]!=' ')):
            field=(field)[j:]
            break
    for j in range(len(field)-1,0,-1):
        if ((field[j]!='\r')&(field[j]!='\n')&(field[j]!=' ')):
            field=(field)[:j+1]
            break
    return(field)
def removeDup(field):
    field = str(field)
    j=1
    while (j<len(field)):
        if (field[j]==field[j-1]):
            field = field[:(j-1)]+field[j:]
            j=j-1
        j=j+1
    return(field)


# In[ ]:


name = []
birthday = []
math = []
literature = []
fLang = []
phys = []
chem = []
bio = []
his = []
geo = []
civ = []
note = []
khxh = []
khtn = []
student_num = -1
for sbd in range (2000001,2074719):
    idstr = '{0:08d}'.format(sbd)
    content = getPageContent(url, idstr)
    tr = content.find_all('tr')
    if (len(tr)==0): continue
    student_num = student_num+1
	print(student_num)
    main = bs4.BeautifulSoup(str(tr[1]),"html.parser")
    mainFields = main.find_all('td')
    thisStudentPointsList = []
    name.append((bs4.BeautifulSoup(str(mainFields[0]),"html.parser")).find('td').text)
    name[student_num]=fieldCleaner(name[student_num])
    birthday.append((bs4.BeautifulSoup(str(mainFields[1]),"html.parser")).find('td').text)
    birthday[student_num]=fieldCleaner(birthday[student_num])
    rawPoints = (bs4.BeautifulSoup(str(mainFields[2]),"html.parser")).find('td').text
    rawPoints=fieldCleaner(rawPoints)

    rawPoints = removeDup(rawPoints)
    rawPoints=rawPoints.replace('Ngữ văn','Văn')
    rawPoints=rawPoints.replace('Địa lí','Địa')
    rawPoints=rawPoints.replace('Lịch sử','Sử')
    rawPoints=rawPoints.replace('Tiếng ','')
    rawPoints=rawPoints.replace(' học','')
    rawPoints=rawPoints.replace('Vật lí','Lý')
    rawPoints=rawPoints.replace(':','')
    thisStudentPointsList = rawPoints.split(' ')
    check = [0,0,0,0,0,0,0,0,0,0,0]
    for xx in range (11):
        if ('Toán' in str(thisStudentPointsList[0])):
            math.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[0]=1
        if (len(thisStudentPointsList)==0): break
        if ('Văn' in str(thisStudentPointsList[0])):
            literature.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[1]=1
        if (len(thisStudentPointsList)==0): break
        if (('Anh' in str(thisStudentPointsList[0]))|('Pháp' in str(thisStudentPointsList[0]))|('Đức' in str(thisStudentPointsList[0]))|('Nhật' in str(thisStudentPointsList[0]))|('Nga' in str(thisStudentPointsList[0]))|('Trung' in str(thisStudentPointsList[0]))):
            note.append('Tiếng '+str(thisStudentPointsList[0]))
            fLang.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[2]=1
        if (len(thisStudentPointsList)==0): break
        if ('Sử' in str(thisStudentPointsList[0])):
            his.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[3]=1
        if (len(thisStudentPointsList)==0): break
        if ('Địa' in str(thisStudentPointsList[0])):
            geo.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[4]=1
        if (len(thisStudentPointsList)==0): break
        if ('GDCD' in str(thisStudentPointsList[0])):
            civ.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[5]=1
        if (len(thisStudentPointsList)==0): break
        if ('KHXH' in str(thisStudentPointsList[0])):
            khxh.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[6]=1
        if (len(thisStudentPointsList)==0): break
        if ('KHTN' in str(thisStudentPointsList[0])):
            khtn.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[7]=1
        if (len(thisStudentPointsList)==0): break
        if ('Lý' in str(thisStudentPointsList[0])):
            phys.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[8]=1
        if (len(thisStudentPointsList)==0): break
        if ('Hóa' in str(thisStudentPointsList[0])):
            chem.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[9]=1
        if (len(thisStudentPointsList)==0): break
        if ('Sinh' in str(thisStudentPointsList[0])):
            bio.append(float(thisStudentPointsList[1]))
            thisStudentPointsList.remove(thisStudentPointsList[0])
            thisStudentPointsList.remove(thisStudentPointsList[0])
            check[10]=1
        if (len(thisStudentPointsList)==0): break
    if (check[0]==0): math.append(float(np.nan))
    if (check[1]==0): literature.append(float(np.nan))
    if (check[2]==0): 
        fLang.append(float(np.nan))
        note.append(float(np.nan))
    if (check[3]==0): his.append(float(np.nan))
    if (check[4]==0): geo.append(float(np.nan))
    if (check[5]==0): civ.append(float(np.nan))
    if (check[6]==0): khxh.append(float(np.nan))
    if (check[7]==0): khtn.append(float(np.nan))
    if (check[8]==0): phys.append(float(np.nan))
    if (check[9]==0): chem.append(float(np.nan))
    if (check[10]==0): bio.append(float(np.nan))

df = pandas.DataFrame({'name':name,
                  'birthday':birthday,
                  'math':math,
                  'literature':literature,
                  'foreign lang':fLang,
                  'history':his,
                  'geo':geo,   
                  'civ':civ,
                  'SS-Mean':khxh,
                  'phys':phys,
                  'chem':chem,
                  'bio':bio,
                  'NS-Mean':khtn,
                  'Note':note})
df.to_json('data_points.json')


# In[ ]:


print(len(math))


# In[ ]:




