
import pandas as pd
import csv
import json

df = pd.read_csv(r"Imp.csv", encoding='unicode_escape')
df.head(3)
data = []
My_answers = []
FreeQuestions = []

with open(r"Imp.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        My_answers.append({"A": row[6],
                           "B": row[7],
                           "C": row[8],
                           "D": row[9]})
    f.close()

def My_fun(n):
    return My_answers[n]

with open(r"Imp.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    count = 0
    for row in reader:
        data.append({"SNO": row[0],
                     "USE": row[1],
                     "TYPE": row[2],
                     "IMAGE_ID": row[3],
                     "Question_text": row[4],
                     "Level": row[5],
                     "ANSWER": My_fun(count),
                     "Editorial": row[11],
                     "Correct_answer": row[10]})
        count += 1
        #print(count)
    f.close()

for items in data:
    FreeQuestions.append({"Question": items})

Final_dict = {"FreeQuestions": list(FreeQuestions)}

with open(r"file.json", "w") as f:
    json.dump(Final_dict, f, indent=4)



