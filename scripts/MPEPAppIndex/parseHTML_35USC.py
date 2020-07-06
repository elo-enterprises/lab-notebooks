from bs4 import BeautifulSoup
import pandas as pd
import re

# This section traverses the 35USC source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.
f = open('data/external/MPEPAppIndex/AppendixL.html','rb')
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
                        prettyi = prettyi.replace('(pre‑AIA)','').lstrip()
                        textUpdateStatus = '(pre-AIA)'
                    if '(pre-PLT (AIA))' in prettyi:
                        prettyi = prettyi.replace('(pre-PLT (AIA)) ','')
                        textUpdateStatus = '(pre-PLT (AIA))'
                    if '(transitional)' in prettyi:
                        prettyi = prettyi.replace('(transitional) ','')
                        textUpdateStatus = '(transitional)'
                    
                    textSection = ''
                    title = ''
                    #print(prettyi)
                    prettyi = prettyi.strip()
                    searchResult = re.search(r'^\d+\s', prettyi)
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
            y = 1
            for li in array_of_li:
                bulkText = li.get_text().strip()
                parg = 'p'
                searchResultP = re.search(r'^\(\w\)\s', bulkText)
                if searchResultP:
                    parg = searchResultP.group().strip()
                    bulkText = bulkText.lstrip(parg).lstrip()
                    searchResultPT = re.search(r'\(\w\)', textSection)
                    if searchResultPT:
                        ptarg = searchResultPT.group().strip()
                        textSection = textSection.rstrip(ptarg)
                    textSection = textSection + parg
                    parg = ''
                litextUpdateStatus = textUpdateStatus
                if '(pre‑AIA) ' in bulkText[0:20]:
                    bulkText = bulkText.replace('(pre‑AIA)','').lstrip()
                    litextUpdateStatus = '(pre-AIA)'
                if '(pre-PLT (AIA)) ' in bulkText[0:20]:
                    bulkText = bulkText.replace('(pre-PLT (AIA)) ','')
                    textUpdateStatus = '(pre-PLT (AIA))'
                if '(transitional) ' in bulkText[0:20]:
                    bulkText = bulkText.replace('(transitional) ','')
                    textUpdateStatus = '(transitional)'
                searchResultN = re.search(r'^\d+\s', bulkText)
                if searchResultN:
                    textSection = searchResultN.group().strip()
                    bulkText = bulkText.lstrip(textSection).lstrip()
                if parg == 'p':
                    parg += str(y)
                    y = y + 1
                    #searchResultTS = re.search(r'\s-\sp\d+$', textSection)
                    #if searchResultTS:
                    #    searchResultTSText = searchResultTS.group().strip()
                    #    textSection = textSection.replace(searchResultTSText,'')
                    #textSection += ' - ' + parg
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

#print(df)
df.to_csv (r'data/interim/MPEPAppIndex/USCSections.csv', index = False, header=True)
