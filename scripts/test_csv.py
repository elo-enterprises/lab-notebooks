import pandas as pd
import numpy as np

# Practice reading from and writing to a local csv file.
# This csv was created in Google Apps Script. 
# The data came from the MPEP as a pdf, opened in Google Docs, massaged manually and imported to Google Sheets.
df = pd.read_csv('data/external/Patent_Bar_Test_Questions.csv')

# df['Section'] = np.where(df['Section'] == '2103', 
#                      df['Section'] + 'add a string', 
#                      df['Section'])

df.to_csv (r'data/interim/test_csv_Patent_Bar_Test_Questions.csv', index = False, header=True)
