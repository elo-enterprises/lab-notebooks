#!/usr/bin/env python
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import pandas as pd
import regex as re

# This section traverses the 35USC source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.
f = open('21_MPEP_Source_HTML/AppendixL.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

df = pd.DataFrame(
    {
        "Part": [],
        "Chapter": [],
        "Section": [],
        "Paragraph": [],
        "Update Status": [],
        "Title": []
    }
)

textPart = ''
textChapter = ''
textSection = ''
textUpdateStatus = ''

array_of_div = soup.find_all('div') #, class_="annotate-ok")
for div in array_of_div:
    h1SectionPlusH2 = ''
    title = ''
    
    array_of_h1 = div.find_all('h1', recursive=False)
    for h1 in array_of_h1:
        if h1.contents:
            # sometimes the contents of an html header does not match the note-title
            prettyH1NoteTitle = " ".join(h1.contents[0].split())
            prettyH1 = " ".join(h1.contents[0].split())
            h1Split = int(prettyH1NoteTitle.find('-'))
            roman = ''
            if h1Split == -1:
                h1Split = len(prettyH1)
                h1Title = ''
            else: 
                h1Title = prettyH1[h1Split:].strip()
            h1Section = prettyH1NoteTitle[0:h1Split].rstrip(' -')
            h1SectionPlusH2 = h1Section
            title = h1Title.lstrip('- ')
            
            if 'PART' in h1Section[0:4]:
                textPart = h1Section[5:]
                textChapter = ''
            if 'CHAPTER' in h1Section[0:9]:
                textChapter = h1Section[8:]
                textSection = ''
                
            if "page-title" not in h1.get('class'):
            #if 'Appendix L' not in h1Section:
                dfH1 = pd.DataFrame(
                    {
                        "Part": [textPart],
                        "Chapter": [textChapter],
                        "Section": [h1Section],
                        "Paragraph": [''],
                        "Update Status": [''],
                        "Title": [title]
                    }
                )
                df = pd.concat([df, dfH1], ignore_index=True)
    array_of_h2 = div.find_all('h2', recursive=False)
    for h2 in array_of_h2:
        if h2: 
            if h2.contents[0]:
                #prettyH2 = "".join(h2.contents[0].split()).replace('.','').replace('(','').replace(')','')
                #prettyH2 = "".join(h2.get_text().split()).replace('.','').replace('(','').replace(')','').lstrip('- ')
                array_of_i = h2.find_all('i')
                for i in array_of_i:
                    prettyi = i.get_text().replace('<i>','').replace('</i>','').replace('\t','')[10:].strip()
                    textUpdateStatus = ''
                    if '(pre‑AIA)' in prettyi:
                        prettyi = prettyi.replace('(pre‑AIA)','')
                        textUpdateStatus = '(pre-AIA)'
                    if '(pre-PLT (AIA))' in prettyi:
                        prettyi = prettyi.replace('(pre-PLT (AIA))','')
                        textUpdateStatus = '(pre-PLT (AIA))'
                    if '(transitional)' in prettyi:
                        prettyi = prettyi.replace('(transitional)','')
                        textUpdateStatus = '(transitional)'
                    
                    textSection = ''
                    title = ''
                    #print(prettyi)
                    searchResult = re.search(r'\d+\s', prettyi)
                    if searchResult:
                        textSection = searchResult.group().strip()
                        title = prettyi.replace(textSection,'').strip()
                        dfB = pd.DataFrame(
                            {
                                "Part": [textPart],
                                "Chapter": [textChapter],
                                "Section": [textSection],
                                "Paragraph": [''],
                                "Update Status": [textUpdateStatus],
                                "Title": [title]
                            }
                        )
                        df = pd.concat([df, dfB], ignore_index=True)
    
    nextul = div.find_next_sibling()
    if nextul:
        x = nextul.name
        if x == 'ul':
            array_of_li = nextul.find_all('li', recursive=False)
            for li in array_of_li:
                bulkText = li.get_text().strip()
                #endOfTitle = int(bulkText.find('.—'))
                #title = bulkText[:endOfTitle]    
                parg = 'p'
                if bulkText[2] == ')':
                    parg = bulkText[0:3]
                litextUpdateStatus = textUpdateStatus
                if '(pre‑AIA)' in bulkText[0:15]:
                    litextUpdateStatus = '(pre-AIA)'
                dfli = pd.DataFrame(
                    {
                        "Part": [textPart],
                        "Chapter": [textChapter],
                        "Section": [textSection],
                        "Paragraph": [parg],
                        "Update Status": [litextUpdateStatus],
                        "Title": [bulkText[0:100]]
                    }
                )
                df = pd.concat([df, dfli], ignore_index=True)

print(df)
df.to_csv (r'21_MPEP_AppIndex/MPEP_AppendixL_TOCData.csv', index = False, header=True)


# In[3]:


import pandas as pd
import numpy as np

# Makes a txt file of Cypher nodes from 35 USC table of contents objects previously harvested from the html source.
df = pd.read_csv('21_MPEP_AppIndex/MPEP_AppendixL_TOCData.csv')

# brute force method of removing duplicate rows, replace with better logic
df.drop_duplicates(subset=['Part', 'Chapter', 'Section', 'Paragraph'], inplace = True)

x = 0
cypherString = 'CREATE \n'
for index, row in df.iterrows():
    part = str(row['Part']).strip()
    if part == 'nan':
        part = ''
    chapter = str(row['Chapter']).strip()
    if chapter == 'nan':
        chapter = ''
    section = str(row['Section']).strip()
    if section == 'nan':
        section = ''
    paragraph = str(row['Paragraph']).strip()
    if paragraph == 'nan':
        paragraph = ''
    uscsName = section + paragraph
    if uscsName[-1] != 'p':
        cypherString += '(uscs' + str(x) + ':USC_Section { ' 
        cypherString += 'name: \'' + section + paragraph + '\', '
        cypherString += 'part: \'' + part + '\', '
        cypherString += 'chapter: \'' + chapter + '\', '
        cypherString += 'section: \'' + section + '\', '
        cypherString += 'paragraph: \'' + paragraph + '\''
        #cypherString += 'updateStatus: \'' + str(row['Update Status']).strip() + '\', '
        #cypherString += 'title: \'' + str(row['Title']).strip() + '\''
        cypherString += ' }),\n'
        x = x + 1
cypherString = cypherString[:-2]

text_file = open("21_MPEP_AppIndex/Cypher_Create_Nodes_35USC.txt", "w")
text_file.write(cypherString)
text_file.close()


# In[24]:


from bs4 import BeautifulSoup
import pandas as pd
import regex as re

# This section traverses the 35USC source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.
f = open('21_MPEP_Source_HTML/AppendixR.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

df = pd.DataFrame(
    {
        "Chapter": [],
        "Part": [],
        "Section": [],
        "Paragraph": [],
        "Update Status": [],
        "Title": []
    }
)

textChapter = ''
textSubChapter = ''
textPart = ''
textSubPart = ''
textSection = ''
textUpdateStatus = ''

array_of_div = soup.find_all('div') #, class_="annotate-ok")
for div in array_of_div:
    
    array_of_h1 = div.find_all('h1', recursive=False)
    for h1 in array_of_h1:
        if h1.contents:
            # sometimes the contents of an html header does not match the note-title
            prettyH1 = " ".join(h1.contents[0].split())
            #print(h1Section)
            textUpdateStatus = ''
            #y = 0
            
            if 'CHAPTER' in prettyH1[0:9]:
                h1Split = int(prettyH1.find(' -'))
                h1Section = prettyH1[:h1Split]
                textChapter = h1Section[8:]
                textSubChapter = textChapter
                textPart = ''
                textSection = ''
                h1Title = prettyH1[h1Split:].lstrip('- ').strip()
            elif 'SUBCHAPTER' in prettyH1[0:12]:
                h1Split = int(prettyH1.find(' -'))
                h1Section = prettyH1[:h1Split]
                textSubChapter = textChapter + h1Section[11:]
                textPart = ''
                textSection = ''
                h1Title = prettyH1[h1Split:].lstrip('- ').strip()
            elif 'PART' in prettyH1[0:4]:
                h1Split = int(prettyH1.find(' -'))
                h1Section = prettyH1[:h1Split]
                textPart = h1Section[5:]
                textSubPart = textPart
                textSection = ''
                h1Title = prettyH1[h1Split:].lstrip('- ').strip()
            elif '-' in prettyH1[0:4]:
                h1Split = int(prettyH1.find(' -'))
                h1Section = prettyH1[:h1Split]
                textSubPart = textPart + h1Section[:3].strip()
                textSection = ''
                h1Title = prettyH1[h1Split:].lstrip('- ').strip()
            elif '.' not in prettyH1[0:4]:
                #y = y + 1
                #textSubPart = textSubPart[0:2] + '-' + str(y)
                textSection = ''
                h1Title = prettyH1.strip()
            else:
                h1Split = int(prettyH1.find(' '))
                textSection = prettyH1[:h1Split]
                h1Title = prettyH1[h1Split:].strip()
                if '(pre‑AIA)' in h1Title:
                    h1Title = h1Title.replace('(pre‑AIA)','').strip()
                    textUpdateStatus = '(pre-AIA)'
                if '(pre‑PLT)' in h1Title:
                    h1Title = h1Title.replace('(pre‑PLT)','').strip()
                    textUpdateStatus = '(pre-PLT)'
                if '(pre‑PLT (AIA))' in h1Title:
                    h1Title = h1Title.replace('(pre‑PLT (AIA))','').strip()
                    textUpdateStatus = '(pre-PLT (AIA))'
                if '(pre‑2013‑03‑16)' in h1Title:
                    h1Title = h1Title.replace('(pre‑2013‑03‑16)','').strip()
                    textUpdateStatus = '(pre-2013-03-16)'
                if '(pre‑2013‑04‑01)' in h1Title:
                    h1Title = h1Title.replace('(pre‑2013‑04‑01)','').strip()
                    textUpdateStatus = '(pre-2013-04-01)'
                if '(2012‑09‑17 thru 2013‑03‑31)' in h1Title:
                    h1Title = h1Title.replace('(2012‑09‑17 thru 2013‑03‑31)','').strip()
                    textUpdateStatus = '(2012-09-17 thru 2013-03-31)'
                if '(pre‑2012‑09‑17)' in h1Title:
                    h1Title = h1Title.replace('(pre‑2012‑09‑17)','').strip()
                    textUpdateStatus = '(pre-2012-09-17)'
                if '(2013‑12‑18 thru 2015‑03‑09)' in h1Title:
                    h1Title = h1Title.replace('(2013‑12‑18 thru 2015‑03‑09)','').strip()
                    textUpdateStatus = '(2013-12-18 thru 2015-03-09)'
                if '(2012‑09‑17 thru 2013‑12‑17)' in h1Title:
                    h1Title = h1Title.replace('(2012‑09‑17 thru 2013‑12‑17)','').strip()
                    textUpdateStatus = '(2012-09-17 thru 2013-12-17)'
                if '(pre‑2013‑03‑31)' in h1Title:
                    h1Title = h1Title.replace('(pre‑2013‑03‑31)','').strip()
                    textUpdateStatus = '(pre-2013-03-31)'
                if '(2012‑09‑16 thru 2013‑12‑17)' in h1Title:
                    h1Title = h1Title.replace('(2012‑09‑16 thru 2013‑12‑17)','').strip()
                    textUpdateStatus = '(2012-09-16 thru 2013-12-17)'
            
            #if "page-title" not in h1.get('class'):
            if 'Appendix R' not in h1Section:
                dfH1 = pd.DataFrame(
                    {
                        "Chapter": [textSubChapter],
                        "Part": [textSubPart],
                        "Section": [textSection],
                        "Paragraph": [''],
                        "Update Status": [textUpdateStatus],
                        "Title": [h1Title]
                    }
                )
                df = pd.concat([df, dfH1], ignore_index=True)
#     array_of_h2 = div.find_all('h2', recursive=False)
#     for h2 in array_of_h2:
#         if h2: 
#             if h2.contents[0]:
#                 #prettyH2 = "".join(h2.contents[0].split()).replace('.','').replace('(','').replace(')','')
#                 #prettyH2 = "".join(h2.get_text().split()).replace('.','').replace('(','').replace(')','').lstrip('- ')
#                 array_of_i = h2.find_all('i')
#                 for i in array_of_i:
#                     prettyi = i.get_text().replace('<i>','').replace('</i>','').replace('\t','')[10:].strip()
#                     textUpdateStatus = ''
#                     if '(pre‑AIA)' in prettyi:
#                         prettyi = prettyi.replace('(pre‑AIA)','')
#                         textUpdateStatus = '(pre-AIA)'
#                     if '(pre-PLT (AIA))' in prettyi:
#                         prettyi = prettyi.replace('(pre-PLT (AIA))','')
#                         textUpdateStatus = '(pre-PLT (AIA))'
#                     if '(transitional)' in prettyi:
#                         prettyi = prettyi.replace('(transitional)','')
#                         textUpdateStatus = '(transitional)'
                    
#                     textSection = ''
#                     title = ''
#                     #print(prettyi)
#                     searchResult = re.search(r'\d+\s', prettyi)
#                     if searchResult:
#                         textSection = searchResult.group().strip()
#                         title = prettyi.replace(textSection,'').strip()
#                         dfB = pd.DataFrame(
#                             {
#                                 "Part": [textPart],
#                                 "Chapter": [textChapter],
#                                 "Section": [textSection],
#                                 "Paragraph": [''],
#                                 "Update Status": [textUpdateStatus],
#                                 "Title": [title]
#                             }
#                         )
#                         df = pd.concat([df, dfB], ignore_index=True)
    
#     nextul = div.find_next_sibling()
#     if nextul:
#         x = nextul.name
#         if x == 'ul':
#             array_of_li = nextul.find_all('li', recursive=False)
#             for li in array_of_li:
#                 bulkText = li.get_text().strip()
#                 #endOfTitle = int(bulkText.find('.—'))
#                 #title = bulkText[:endOfTitle]    
#                 parg = 'p'
#                 if bulkText[2] == ')':
#                     parg = bulkText[0:3]
#                 litextUpdateStatus = textUpdateStatus
#                 if '(pre‑AIA)' in bulkText[0:15]:
#                     litextUpdateStatus = '(pre-AIA)'
#                 dfli = pd.DataFrame(
#                     {
#                         "Part": [textPart],
#                         "Chapter": [textChapter],
#                         "Section": [textSection],
#                         "Paragraph": [parg],
#                         "Update Status": [litextUpdateStatus],
#                         "Title": [bulkText[0:100]]
#                     }
#                 )
#                 df = pd.concat([df, dfli], ignore_index=True)

print(df)
df.to_csv (r'21_MPEP_AppIndex/MPEP_AppendixR_TOCData.csv', index = False, header=True)


# In[8]:


from bs4 import BeautifulSoup
import pandas as pd

# Makes a list of references 1:1 CaseOrAction:mpep_reference by processing the "List of Decisions Cited," not the MPEP.
f = open('21_MPEP_Source_HTML/ListOfDecisionsCited.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

df = pd.DataFrame(
    {
        "CaseOrAction": [],
        "MPEPLink": []
    }
)

array_of_p = soup.find_all('p')
for p in array_of_p:
    if 's Note: Opinions of the ' not in p.getText():
        prettyCaseOrActionLink = p.contents[0].strip()
        
        array_of_b = p.find_all('b')
        for b in array_of_b:
            array_of_a = b.find_all('a')
            for a in array_of_a:
                dfA = pd.DataFrame(
                    {
                        "CaseOrAction": [prettyCaseOrActionLink],
                        "MPEPLink": [a.get_text()]
                    }
                )
                df = pd.concat([df, dfA], ignore_index=True)
                
df.to_csv (r'21_MPEP_AppIndex/MPEP_CasesAndActions.csv', index = False, header=True)
df


# In[20]:


from bs4 import BeautifulSoup
import pandas as pd

# Makes a list of references 1:1 subject_matter_name:mpep_reference.
f = open('21_MPEP_Source_HTML/IndexA.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

df = pd.DataFrame(
    {
        "Topic": [],
        "Subtopic1": [],
        "Subtopic2": [],
        "Subtopic3": [],
        "Subtopic4": [],
        "SeeAlso": [],
        "MPEPLink": []
    }
)

array_of_li = soup.find_all('li')
startedYet = 0
finishedYet = 0
for li in array_of_li:
    if startedYet == 0:
        if "Subject Matter Index  A" in li.contents:
            startedYet = 1
    elif finishedYet == 1:
        finishedYet = 1
    else:
        if "Avoiding double patenting rejection" in li.get_text():
            finishedYet = 1
        if len(li.contents[0]) > 0:
            prettySubjectName = " ".join(str(li.contents[0]).split()).replace('(','').replace(')','').rstrip().rstrip('—')
        prettySubjectNameLayer0 = prettySubjectName
        prettySubjectNameLayer1 = ''
        prettySubjectNameLayer2 = ''
        prettySubjectNameLayer3 = ''
        prettySubjectNameLayer4 = ''
        
        pa = li.parent
        if pa.name == 'ul':
            gp = pa.parent
            if gp.name == 'li':
                prettyGPName = " ".join(str(gp.contents[0]).split()).replace('(','').replace(')','').rstrip().rstrip('—')
                prettySubjectNameLayer0 = prettyGPName
                prettySubjectNameLayer1 = prettySubjectName
                ggp = gp.parent
                if ggp.name == 'ul':
                    g3p = ggp.parent
                    if g3p.name == 'li':
                        prettyG3PName = " ".join(str(g3p.contents[0]).split()).replace('(','').replace(')','').rstrip().rstrip('—')
                        prettySubjectNameLayer0 = prettyG3PName
                        prettySubjectNameLayer1 = prettyGPName
                        prettySubjectNameLayer2 = prettySubjectName
                        g4p = g3p.parent
                        if g4p.name == 'ul':
                            g5p = g4p.parent
                            if g5p.name == 'li':
                                prettyG5PName = " ".join(str(g5p.contents[0]).split()).replace('(','').replace(')','').rstrip().rstrip('—')
                                prettySubjectNameLayer0 = prettyG5PName
                                prettySubjectNameLayer1 = prettyG3PName
                                prettySubjectNameLayer2 = prettyGPName
                                prettySubjectNameLayer3 = prettySubjectName
                                g6p = g5p.parent
                                if g6p.name == 'ul':
                                    g7p = g6p.parent
                                    if g7p.name == 'li':
                                        prettyG7PName = " ".join(str(g7p.contents[0]).split()).replace('(','').replace(')','').rstrip().rstrip('—')
                                        prettySubjectNameLayer0 = prettyG7PName
                                        prettySubjectNameLayer1 = prettyG5PName
                                        prettySubjectNameLayer2 = prettyG3PName
                                        prettySubjectNameLayer3 = prettyGPName
                                        prettySubjectNameLayer4 = prettySubjectName
        
        seeAlso = ''
        array_of_seeAlso_a = li.find_all('a', recursive=False)
        for seeAlso_a in array_of_seeAlso_a:
            seeAlso = seeAlso + seeAlso_a.get_text() + '; '
            
        #first_b = subject_name.find(lambda t: t.name != 'div'):
        #array_of_b = subject_name.find_children('b', recursive=False)
        printedThisLi = 0
        array_of_b = li.find_all('b', recursive=False)
        for b in array_of_b:
            array_of_a = b.find_all('a')
            for a in array_of_a:
                #print(a.get_text())
                dfA = pd.DataFrame(
                    {
                        "Topic": [prettySubjectNameLayer0],
                        "Subtopic1": [prettySubjectNameLayer1],
                        "Subtopic2": [prettySubjectNameLayer2],
                        "Subtopic3": [prettySubjectNameLayer3],
                        "Subtopic4": [prettySubjectNameLayer4],
                        "SeeAlso": [seeAlso],
                        "MPEPLink": [a.get_text()]
                    }
                )
                df = pd.concat([df, dfA], ignore_index=True)
                printedThisLi = 1
        if printedThisLi == 0:
            dfA = pd.DataFrame(
                {
                    "Topic": [prettySubjectNameLayer0],
                    "Subtopic1": [prettySubjectNameLayer1],
                    "Subtopic2": [prettySubjectNameLayer2],
                    "Subtopic3": [prettySubjectNameLayer3],
                    "Subtopic4": [prettySubjectNameLayer4],
                    "SeeAlso": [seeAlso],
                    "MPEPLink": ['']
                }
            )
            df = pd.concat([df, dfA], ignore_index=True)
                
                
df.to_csv (r'21_MPEP_AppIndex/MPEP_IndexA.csv', index = False, header=True)
df


# In[ ]:




