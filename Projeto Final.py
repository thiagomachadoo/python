#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as r


# In[2]:


url = 'https://api.covid19'


# In[3]:


url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)


# In[4]:


resp.status_code


# In[5]:


raw_data = resp.json()


# In[6]:


raw_data[0]


# In[9]:


final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])


# In[11]:


final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
final_data


# In[12]:


CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4


# In[13]:


for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]


# In[14]:


final_data


# In[15]:


import datetime as dt


# In[16]:


import csv


# In[17]:


with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)


# In[20]:


for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')


# In[21]:


final_data


# In[22]:


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
            return datasets
        else:
            return[
                {
                    'label': labels[0],
                    'data': y
                }
            ]


# In[23]:


def set_title(title= ''):
    if title != '':
        display= 'true'
    else:
        display = 'false'
    return{
        'title': title,
        'display': display
    }


# In[38]:


def create_chart(x, y, labels, kind = 'bar', title = '')

    datasets = get_datasets(y, labels),
    options = set_title(title):
    
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart


# In[28]:


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content


# In[29]:


def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


# In[40]:


from PIL import Image
from IPython.display import display


# In[ ]:


def display_image(path): 
    img_pil = Image.open(path)
    display(img_pil)


# In[41]:


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
y_data_1 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d%m%Y'))
    
chart = create_chart(x, [y_data_1, y_data_2], labels, title = 'Grafico confirmados e recuperados')
chart_content = get.api_chart(chart)
save_image('Meu primeiro grafico', chart_content)
display_image('meu-p-g.png')


# In[44]:


def get_api_qrcode(link):
    text = quote(link)
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content


# In[43]:


from urllib.parse import quote


# In[46]:


url_base = 'https://quickchart.io/chart'
link = (f'{url_base}?c={str(chart)}')
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')


# In[ ]:




