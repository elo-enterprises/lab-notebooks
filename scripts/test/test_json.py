import json
import pandas as pd

df = pd.read_csv('data/external/PatentBarTestQuestions.csv')
jsonString = df.to_json(orient='split')

text_file = open("data/interim/test/test_json_PatentBarTestQuestions.txt", "w")
text_file.write(jsonString)
text_file.close()

df2 = pd.read_json(jsonString, orient='split')
df2.to_csv (r'data/interim/test/test_jsoncsv_PatentBarTestQuestions.csv', index = False, header=True)