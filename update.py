from app import student

eno = int(input("Enter ENO where you want to update name:"))

data = student.where("eno", "==", eno).get()

if len(data) > 0:
    print(data[0].get("name"))
else:
    print("No such ENO found in our database")