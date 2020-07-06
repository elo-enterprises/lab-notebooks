from bs4 import BeautifulSoup
import pandas as pd
import re

# Makes a list of references 1:1 CaseOrAction:mpep_reference by processing the "List of Decisions Cited," not the MPEP.
f = open('data/external/MPEPAppIndex/ListOfDecisionsCited.html','rb')
soup = BeautifulSoup(f.read(), 'html.parser')

df = pd.DataFrame(
    {
        "name": [],
        "year": [],
        "Links to MPEP": []
    }
)

array_of_p = soup.find_all('p')
for p in array_of_p:
    if 's Note: Opinions of the ' not in p.getText():
        prettyCaseOrActionLink = p.contents[0].strip()
        yearText = ''
        patternYear = re.compile(r'\d\d\d\d\)')
        for match in re.finditer(patternYear, prettyCaseOrActionLink):
            s = match.start()
            e = match.end()
            matchTextInt = int(prettyCaseOrActionLink[s:e].rstrip('\)'))
            if matchTextInt > 1900 and matchTextInt < 2020:
                yearText = matchTextInt
        mpepLinks = ''
        array_of_b = p.find_all('b')
        for b in array_of_b:
            array_of_a = b.find_all('a')
            for a in array_of_a:
                mpepLinks += a.get_text() + '; '
                
        dfA = pd.DataFrame(
            {
                "name": [prettyCaseOrActionLink],
                "year": [yearText],
                "Links to MPEP": [mpepLinks]
            }
        )
        df = pd.concat([df, dfA], ignore_index=True)
                
df.to_csv (r'data/interim/MPEPAppIndex/CaseActions.csv', index = False, header=True)