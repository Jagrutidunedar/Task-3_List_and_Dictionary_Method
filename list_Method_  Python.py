# LIST METHOD IN PYTHON

# 1) append()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]

student_list.append("raj")
print(student_list)
print('---')
print('---')

# 2) clear()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]

student_list.clear()
print(student_list)
print('---')
print('---')

# 3) copy

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]

student_list.copy()
print(student_list)
print('---')
print('---')

# 4) count()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'sanskruti',
    'sanskruti',
    'sanskruti',
    'pooja'
]

output = student_list.count('sanskruti')
print(output)
print('---')
print('---')

# 5) extend()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]
print(student_list)
student_list.extend(['pihu','nikita','akshay'])
print(student_list)
print('---')
print('---')

# 6) index()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]
output = student_list.index('pooja')
print(output)
print('---')
print('---')

# 7) reverse()

student_list = [
    'jagruti',
    'sejal',
    'sanskruti',
    'pooja'
]
student_list.reverse()
print(student_list)
print('---')
print('---')

# 8) sort()

student_list = [
    'jagruti',
    'sejal',
    'SANSKRUTI',
    'POOJA'
]
student_list.sort()
print(student_list)
print('---')
print('---')












