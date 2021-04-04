from app import myapp, db, student
import pandas as pd

data = pd.read_csv('db/sample_db.csv')

for index, obj in data.iterrows():
    data = {
        "eno": obj.ENO,
        "name": obj.Name
    }
    student.add(data)