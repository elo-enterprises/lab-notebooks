#!/usr/bin/env python
# coding: utf-8

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




