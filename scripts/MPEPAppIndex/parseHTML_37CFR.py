from bs4 import BeautifulSoup
import pandas as pd
import re

# This section traverses the 35USC source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.
f = open('data/external/MPEPAppIndex/AppendixR.html','rb')
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
            h1Section = ''
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
df.to_csv (r'data/interim/MPEPAppIndex/CFRSections.csv', index = False, header=True)

