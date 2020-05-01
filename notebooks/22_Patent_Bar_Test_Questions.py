#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')
df


# In[2]:


import pandas as pd
import numpy as np

# Makes a txt file of Cypher nodes from the Patent Bar Test Questions
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

x = 0
cypherString = 'CREATE \n'
for index, row in df.iterrows():
    doc = str(row['Doc']).replace('\n',' ').strip()
    q = str(row['Q']).strip().replace('.0','')
    cypherString += '(pbtq' + str(x) + ':PatentBar_TestQuestion { ' 
    cypherString += 'name: \'' + doc + ' - ' + q + '\', '
    cypherString += 'doc: \'' + doc + '\', '
    cypherString += 'q: \'' + q + '\''
    #cypherString += 'Call: \'' + str(row['Call']).strip() + '\', '
    #cypherString += 'Answer_Choices: \'' + str(row['Answer Choices']).strip() + '\', '
    #cypherString += 'Discussion: \'' + str(row['Discussion']).strip() + '\''
    cypherString += ' }),\n'
    x = x + 1
cypherString = cypherString[:-2]

text_file = open("22_PatentBar_TestQuestions/Cypher_Create_Nodes_PatentBar_TestQuestions.txt", "w")
text_file.write(cypherString)
text_file.close()


# In[1]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the 35USC Links column and creates a longer list of 1:1 test_questions:35USC_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to 35USC": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to \n35 USC']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to 35USC": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksTo35USC.csv', index = False, header=True)
dfA


# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksTo35USC.csv')

# Creates a Cypher Relationships list of 1:1 test_questions:35USC_links.
# MATCH (a:Person),(b:Person)
# WHERE a.name = 'A' AND b.name = 'B'
# CREATE (a)-[r:RELTYPE]->(b)

# cypherString = ''
# for index, row in df.iterrows():
#     doc = str(row['Doc']).replace('\n',' ').strip()
#     q = str(row['Q']).strip().replace('.0','')
#     pbtqName = doc + ' - ' + q
#     uscsName = str(row['Link to 35USC']).strip()
#     cypherString += 'MATCH (a:PatentBar_TestQuestion),(b:USC_Section)\n'
#     cypherString += 'WHERE a.name = \'' + pbtqName + '\' AND b.name = \'' + uscsName + '\'\n'
#     cypherString += 'CREATE (a)-[r:PBTQ_USC]->(b)' 
#     cypherString += '\n\n'

cypherMatchString = 'MATCH \n'
cypherCreateString = 'CREATE \n'
x = 0
pbtqX = 0
uscsX = 0
for index, row in df.iterrows():
    doc = str(row['Doc']).replace('\n',' ').strip()
    q = str(row['Q']).strip().replace('.0','')
    pbtqName = doc + ' - ' + q
    uscsName = str(row['Link to 35USC']).strip()
    if x < 10:
        cypherMatchString += '(pbtq' + str(pbtqX) + ':PatentBar_TestQuestion { name: "' + pbtqName + '" }),\n'
        cypherMatchString += '(uscs' + str(uscsX) + ':USC_Section { name: "' + uscsName + '" }),\n'
        cypherCreateString += '(pbtq' + str(pbtqX) + ')-[r' + str(x) + ':PBTQ_USC]->(uscs' + str(uscsX) + '),\n' 
        pbtqX = pbtqX + 1
        uscsX = uscsX + 1
        x = x + 1
cypherMatchString = cypherMatchString[:-2]
cypherMatchString += '\n'
cypherCreateString = cypherCreateString[:-2]

text_file = open("22_PatentBar_TestQuestions/Cypher_Create_Rels_PatentBar_TestQuestions_35USC.txt", "w")
text_file.write(cypherMatchString + cypherCreateString)
text_file.close()


# In[15]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the 37CFR Links column and creates a longer list of 1:1 test_questions:37CFR_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to 37CFR": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to \n37 CFR']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to 37CFR": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksTo37CFR.csv', index = False, header=True)
dfA


# In[16]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the PCT Links column and creates a longer list of 1:1 test_questions:PCT_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to PCT": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to \nPCT']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to PCT": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksToPCT.csv', index = False, header=True)
dfA


# In[17]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the MPEP Links column and creates a longer list of 1:1 test_questions:mpep_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to MPEP": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to MPEP']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to MPEP": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksToMPEP.csv', index = False, header=True)
dfA


# In[18]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the FRN Links column and creates a longer list of 1:1 test_questions:FRN_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to FRN": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to \nFRN']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to FRN": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksToFRN.csv', index = False, header=True)
dfA


# In[19]:


import pandas as pd
import numpy as np

# Read from a csv list of test questions.
df = pd.read_csv('22_PatentBar_TestQuestions/PatentBar_TestQuestions.csv')

# This section processes the CaseOrAction Links column and creates a longer list of 1:1 test_questions:CaseOrAction_links.
dfA = pd.DataFrame(
    {
        "Doc": [],
        "Q": [],
        "Link to CaseOrAction": []
    }
)

for index, row in df.iterrows():
    mpepLinks = row['Links to \nCases & Actions']
    i = -2
    while str(mpepLinks).find(';',i+2) != -1: 
        prevI = int(i+2)
        i = str(mpepLinks).find(';',prevI)
        link = mpepLinks[prevI:i]
        dfB = pd.DataFrame(
            {
                "Doc": [row['Doc'].replace('\n',' ')],
                "Q": [row['Q']],
                "Link to CaseOrAction": [link]
            }
        )
        dfA = pd.concat([dfA, dfB], ignore_index=True)

dfA.to_csv (r'22_PatentBar_TestQuestions/PatentBar_TestQuestions_LinksToCaseOrAction.csv', index = False, header=True)
dfA


# In[ ]:




