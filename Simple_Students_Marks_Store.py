
stud_dict={}
num   =   int(input("\nEnter how many students in the class : "))

for i in range(num):
    name_inp=input(f"Name of Student {i+1} : ")
    name = name_inp.lower()
    marks=input("Marks/Percentage  : ")
    stud_dict.update({name:marks})

print("\n==============     CHECK STUDENTS MARKS    ===================")
while True:
    search_inp  =  input("Student Name to See Marks : ")
    search = search_inp.lower()
    print(stud_dict.get(search," Student Not Registered"))

    choice =input("View More Students? Press Y/N \n")
    if choice.lower()=='n':
        print("Exit Successfully !!!\n ")
        break
