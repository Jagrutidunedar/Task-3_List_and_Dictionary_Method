# Python Dictionary Method

# 1) CLEAR()

student = {
    "name" : "pooja",
    "age" : 22,
    "branch" : "ARTs"
}
print(student)
print('---')
print('---')
student.clear()
print(student)

# 2) COPY()

student = {
    "name" : "pooja",
    "age" : 22,
    "branch" : "ARTs"
}
print(student)
print('---')
print('---')
student.copy()
print(student)

# 3) fromkeys()

student = ['name','age','gender',]
value = 'unknown'
print('---')
print('---')
my_dict = dict.fromkeys(student,value)
print(my_dict)

# 4) get()

Employee = {
    "name" : "Alice",
    "age" : 25,
    "branch" : "Accounts Department",
    "city" : "pune",
}
salary = Employee.get('salary',95000)
print('---')
print('---')
print(salary)
print()

# 5) items()

Fees = {
    "john" : 45000,
    "raj" : 20000,
    "jagruti" : 98000,
}
print('---')
print('---')
print('dictionry items are :')
Fees_view = Fees.items()
print(Fees_view)

# 6) pop()

Fruites = {
    "apple" : 23,
    "banana" : 56,
    "mango" : 100,
    "orange" : 2
}
print('---')
print('---')
Exctract_fruites = Fruites.pop("apple")
print(Exctract_fruites)

# 7) popitem()

Fruites = {
    "apple" : 23,
    "banana" : 56,
    "mango" : 100,
    "orange" : 290
}
print('---')
print('---')
X = Fruites.popitem()
print(X)

# 8) setdefault()

Fruites = {
    "apple" : "Red",
    "banana" : "Yellow",
    "mango" : "yellow",
    "orange" : "orange",
}    
print('---')
print('---')
X = Fruites.setdefault("mango","pink")
print(X)


# 9) update()

car =  {
    "brand" : "BMW",
    "Model" : "Mustang",
    "Year" : 2023
}
print('---')
print('---')
car.update({"colour" : "Black"})  
print(car)

# 10) values()

student_scores = {
    "john" : 85,
    "Pooja" : 99,
    "jagruti" : 100
}
print('---')
print('---')
print(student_scores)
print('---')
print('---')
print(student_scores.values())


    
