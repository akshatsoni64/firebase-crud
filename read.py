from app import student

data = student.get()

for record in data:
    print("Name:", record.get('name'), "-- ENO:", record.get("eno"))