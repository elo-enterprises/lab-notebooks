from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

# This section traverses an MPEP source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.

chapterNumbers = np.arange(1, 30, 1).tolist()
#chapterNumbers = [19, 20, 22, 23, 24, 25, 26, 27, 28, 29]
#chapterNumbers = [18]
for chapterNumber in chapterNumbers:
    chapterText = ('0'+str(chapterNumber*100))[-4:]
    f = open('data/external/MPEP/MPEPChapter'+chapterText+'.html','rb')
    soup = BeautifulSoup(f.read(), 'html.parser')
    
    df = pd.DataFrame(
        {
            "Part": [],
            "Chapter": [],
            "Section": [],
            "Paragraph": [],
            "Update Status": [],
            "Title": [],
            "Links to MPEP": [],
            "Links to 35USC": [],
            "Links to 37CFR": [],
            "Links to Cases and Actions": []
        }
    )
    
    array_of_div = soup.find_all('div', class_="annotate-ok")
    for div in array_of_div:
        h1SectionPlusH2 = ''
        title = ''
    
        array_of_h1 = div.find_all('h1', recursive=False)
        for h1 in array_of_h1:
            # sometimes the contents of an html header does not match the note-title
            if h1.get('note-title'):
                prettyH1NoteTitle = " ".join(h1.get('note-title').split())
            else:
                prettyH1NoteTitle = ''
            prettyH1 = " ".join(h1.contents[0].split())
            h1Split = int(prettyH1NoteTitle.find(' - '))
            roman = ''
            if h1Split == -1:
                h1Split = len(prettyH1)
                h1Title = ''
            else: 
                h1Title = prettyH1[h1Split:].strip()
            h1Section = prettyH1NoteTitle[0:h1Split].rstrip(' -')
            h1SectionPlusH2 = h1Section
            title = h1Title
            h1Uri = h1.get('uri')
            dfH1 = pd.DataFrame(
                {
                    "Part": ['MPEP'],
                    "Chapter": [chapterText],
                    "Section": [h1Section],
                    "Paragraph": [''],
                    "Update Status": [''],
                    "Title": [title],
                    "Links to MPEP": [''],
                    "Links to 35USC": [''],
                    "Links to 37CFR": [''],
                    "Links to Cases and Actions": ['']
                }
            )
            df = pd.concat([df, dfH1], ignore_index=True)
        array_of_h2 = div.find_all('h2', recursive=False)
        for h2 in array_of_h2:
            prettyH2 = "".join(h2.contents[0].split()).replace('.','').replace('(','').replace(')','')
            if prettyH2 in ['I','II','III','IV','V','VI','VII','VIII','IX','X']:
                roman = '(' + prettyH2 + ')'
                h1SectionPlusH2 = h1Section + roman
                capLetter = ''
                num = ''
                lowLetter = ''
            elif prettyH2 in ['A','B','C','D','E','F','G','H'] and prettyH2.isupper():
                capLetter = '(' + prettyH2 + ')'
                h1SectionPlusH2 = h1Section + roman + capLetter
                num = ''
                lowLetter = ''
            elif prettyH2 in ['1','2','3','4','5','6','7','8']:
                num = '(' + prettyH2 + ')'
                h1SectionPlusH2 = h1Section + roman + capLetter + num
                lowLetter = ''
            elif prettyH2 in ['a','b','c','d','e','f','g','h'] and prettyH2.islower():
                lowLetter = '(' + prettyH2 + ')'
                h1SectionPlusH2 = h1Section + roman + capLetter + num + lowLetter
            elif prettyH2 in ['i','ii','iii','iv','v','vi','vii','viii'] and prettyH2.islower():
                lowRoman = '(' + prettyH2 + ')'
                h1SectionPlusH2 = h1Section + roman + capLetter + num + lowLetter + lowRoman
            array_of_b = h2.find_all('b')
            for b in array_of_b:
                prettyB = b.get_text().replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','').replace('"','').strip()
                title = prettyB
                dfB = pd.DataFrame(
                    {
                        "Part": ['MPEP'],
                        "Chapter": [chapterText],
                        "Section": [h1SectionPlusH2],
                        "Paragraph": [''],
                        "Update Status": [''],
                        "Title": [title],
                        "Links to MPEP": [''],
                        "Links to 35USC": [''],
                        "Links to 37CFR": [''],
                        "Links to Cases and Actions": ['']
                    }
                )
                df = pd.concat([df, dfB], ignore_index=True)
    
        pn = div.find_next_sibling()
        if pn:
            x = pn.name
            y = 1
            while x == 'p' or x == 'blockquote':
                ## Create a pattern to match names
                ##pattern35USC = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
                #
                ## Find all occurrences of the pattern
                ##refs35USC = pattern35USC.findall(p.get_text())
    
                #match35USC = pattern35USC.search(bulkText)
                #matches35USC = re.findall(pattern35USC, bulkText, flags=0)
                #match35USC = re.search(r'35\sU\.S\.C\.\s\d\d\d(\(\w\))*', bulkText)
                #matches35USC = re.findall(r'35\sU\.S\.C\.\s\d\d\d(\(\w\))*', bulkText)
                if x == 'p':
                    bulkText = pn.get_text()
                else:
                    psub = pn.find('p')
                    bulkText = psub.get_text()
    
                pattern35USC = re.compile(r'(pre\-AIA\s)*35\sU\.S\.C\.\s\d\d\d(\(\w\))*(\,\sfirst\sparagraph)*') ##, flags = re.M)
                linksTo35USC = ''
                for match in re.finditer(pattern35USC, bulkText):
                    s = match.start()
                    e = match.end()
                    matchText = bulkText[s:e].rstrip().rstrip('.')
                    if matchText not in linksTo35USC: ##removes duplicates in 2103(III)(A)p5 but not in 2105(II)(A)p2
                        linksTo35USC += matchText + '; '
    
                #pattern37CFR = re.compile(r'37\sCFR') ##\s1\.(\d)+(\(\w\))*')
                linksTo37CFR = ''
                for match in re.finditer(r'37\sCFR\s1\.(\d)+(\(\w\))*', bulkText):
                    s = match.start()
                    e = match.end()
                    matchText = bulkText[s:e].rstrip().rstrip('.')
                    if matchText not in linksTo37CFR:
                        linksTo37CFR += matchText + '; '
    
                #pattern37CFR = re.compile(r'37\sCFR') ##\s1\.(\d)+(\(\w\))*')
                linksToCasesAndActions = ''
                for match in re.finditer(r'In\sre\s.{0,75}\)', bulkText):
                    s = match.start()
                    e = match.end()
                    matchText = bulkText[s:e].rstrip().rstrip('.')
                    if matchText not in linksToCasesAndActions:
                        linksToCasesAndActions += matchText + '; '
    
                #if match35USC:
                    #linksTo35USC = match35USC.group() ## works great for a single match after the search function
                    #linksTo35USC = match35USC ##returns <regex.Match object; span=(712, 728), match='35 U.S.C. 112(f)'>
                    #linksTo35USC = matches35USC.groups() ## breaks, list object has no such attribute
                    #i=0
                   # for thisMatch in matches35USC:
                   #     tempLinks = linksTo35USC
                   # #    linksTo35USC = linksTo35USC + str(match35USC[i]) + '; ' ## prints blanks for everything except subsection letters
                   #     linksTo35USC = tempLinks + thisMatch + '; '
                   # #    i=i+1
    
                dfB = pd.DataFrame(
                    {
                        "Part": ['MPEP'],
                        "Chapter": [chapterText],
                        "Section": [h1SectionPlusH2],
                        "Paragraph": ['p'+str(y)],
                        "Update Status": [''],
                        "Title": [''],
                        "Links to MPEP": [''],
                        "Links to 35USC": [linksTo35USC],
                        "Links to 37CFR": [linksTo37CFR],
                        "Links to Cases and Actions": [linksToCasesAndActions]
                    }
                )
                df = pd.concat([df, dfB], ignore_index=True)
                pn = pn.find_next_sibling()
                if pn:
                    x = pn.name
                    y = y + 1
                else:
                    x = 'none'
    # attempted to remove double quotes, but titles that contain commas must keep them within a csv
    # df['Title'] = df['Title'].str.replace('"','')
    
    # brute force method of removing duplicate rows, not needed if find_all is recursive=False
    #df.drop_duplicates(inplace = True)
    #print(df)
    df.to_csv (r'data/interim/MPEP/MPEPChapter'+chapterText+'Sections.csv', index = False, header=True)
