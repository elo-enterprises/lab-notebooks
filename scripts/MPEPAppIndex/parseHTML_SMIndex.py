from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

# This section traverses an MPEP source html file and builds a table of contents. 
# It does not always get the paragraphs right. Keep error-checking.
# It formats the headers successfully, but with brute force that should be replaced by regular expressions.

chapterNames = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#chapterNames = ['A','B']
for chapterText in chapterNames:
    f = open('data/external/MPEPAppIndex/Index' + chapterText + '.html','rb')
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
            if "Subject Matter Index  " + chapterText in li.contents:
                startedYet = 1
        else:
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
                if seeAlso_a.get_text() == 'A':
                    finishedYet = 1
            if finishedYet != 1:
                mpepLinksText = ''
                array_of_b = li.find_all('b', recursive=False)
                for b in array_of_b:
                    array_of_a = b.find_all('a')
                    for a in array_of_a:
                        mpepLinksText += a.get_text() + '; '
                dfA = pd.DataFrame(
                    {
                        "Topic": [prettySubjectNameLayer0],
                        "Subtopic1": [prettySubjectNameLayer1],
                        "Subtopic2": [prettySubjectNameLayer2],
                        "Subtopic3": [prettySubjectNameLayer3],
                        "Subtopic4": [prettySubjectNameLayer4],
                        "SeeAlso": [seeAlso],
                        "MPEPLink": [mpepLinksText]
                    }
                )
                df = pd.concat([df, dfA], ignore_index=True)
                    
    df.to_csv (r'data/interim/MPEPAppIndex/SMIndex' + chapterText + '.csv', index = False, header=True)