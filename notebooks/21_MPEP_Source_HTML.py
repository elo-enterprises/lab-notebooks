#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

# To be nice to the USPTO servers, scrape a copy of the MPEP page and do your processing on the local copy.
r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e197004.html')
with open('Chapter2100.html', 'wb') as f:
    f.write(r.content)


# In[1]:


from bs4 import BeautifulSoup

# Practice grabbing headers from the source html file.
f = open('MPEP_Source_HTML/Chapter2100.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()

# section_name_list_array = soup.find_all(class_='Section')
# section_name_list_items = []
# for section_name_list in section_name_list_array:
#     section_name_list_items += section_name_list.find_all('h1')
section_name_list_items = soup.find_all('h1')

# artist_name_list = soup.find(class_='BodyText')
# artist_name_list_items = artist_name_list.find_all('a')

for section_name in section_name_list_items:
    # name = section_name.contents[0]
    # name = section_name.prettify()
    name = " ".join(section_name.get('note-title').split())
    # name = " ".join(section_name.contents.split())
    print(name)
    # print(section_name.contents)


# In[ ]:


import requests

# All the subject matter index html files have the same name scheme, just with different letters. 
# I manually changed the letters each time, and this could be replaced by a loop.
# I also took the html directly from the page in the index without finding the printable version.
# r = requests.get('https://www.uspto.gov/web/offices/pac/mpep/mpep-index-z.html')
# with open('IndexZ.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e405.html')
# with open('Chapter0100.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e4510.html')
# with open('Chapter0200.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e17683.html')
# with open('Chapter0300.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e20478.html')
# with open('Chapter0400.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e24253.html')
# with open('Chapter0500.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e34301.html')
# with open('Chapter0600.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e55397.html')
# with open('Chapter0700.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e97826.html')
# with open('Chapter0800.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e110007.html')
# with open('Chapter0900.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e115995.html')
# with open('Chapter1000.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e4051.html')
# with open('Chapter1100.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e122292.html')
# with open('Chapter1200.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e131453.html')
# with open('Chapter1300.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e134581.html')
# with open('Chapter1400.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e150114.html')
# with open('Chapter1500.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e161282.html')
# with open('Chapter1600.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e162379.html')
# with open('Chapter1700.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e163752.html')
# with open('Chapter1800.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e193631.html')
# with open('Chapter1900.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e195418.html')
# with open('Chapter2000.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e197004.html')
# with open('Chapter2100.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e220689.html')
# with open('Chapter2200.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e237627.html')
# with open('Chapter2300.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e240552.html')
# with open('Chapter2400.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e247906.html')
# with open('Chapter2500.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e249708.html')
# with open('Chapter2600.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e271941.html')
# with open('Chapter2700.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=ch2800_d1fea8_279ab_9.html')
# with open('Chapter2800.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=ch2900_d24ad2_2793a_190.html')
# with open('Chapter2900.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e290278.html')
# with open('ListOfDecisionsCited.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e300730.html')
# with open('AppendixL.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e312906.html')
# with open('AppendixR.html', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://mpep.uspto.gov/RDMS/MPEP/print?version=current&href=d0e362842.html')
# with open('AppendixT.html', 'wb') as f:
#     f.write(r.content)

