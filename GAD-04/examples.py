# def a(nr_1, nr_2):
#     return nr_1 + nr_2

# my_sum = (lambda nr_1, nr_2: nr_1 + nr_2)(5,7)
# print('my_sum', my_sum)

# Particular function which uses memory
# def get_student_grade(student):
#     return student["grade"]

students = [
    {
        "name": "Student 1",
        "grade": 7.20
    },
    {
        "name": "Student 2",
        "grade": 7.90
    },
    {
        "name": "Student 3",
        "grade": 5.40
    },
    {
        "name": "Student 4",
        "grade": 3.20
    },
    {
        "name": "Student 5",
        "grade": 10
    }
]


# students.sort(key=get_student_grade, reverse=True)
# students.sort(key = lambda student_item: student_item["grade"], reverse = True)
# print(students)

# Map - applies a function on an iterable, can be used with lambda
def split_name(student):
    student_name = student["name"].split(" ")
    return {
        "first_name": student_name[0],
        "last_name": student_name[1],
        "grade": student["grade"]
    }


# students = list(map(split_name, students))
# print(students)


# Filter - filters an iterable
# promoted_students = list(filter(lambda student: student["grade"] > 5, students))
# print("Promoted students: ", promoted_students)

# Map and Filter can be combined together
# promoted_students = list(
#     filter(lambda: student: student["grade"] > 5.00), map(split_name, students)
# )
# promoted_students


# Zip
# numbers_1 = (1,2,3,4,5)
# numbers_2 = tuple(map(lambda nr: nr * 2, numbers_1))
# numbers_3 = tuple(map(lambda nr: nr ** 2, numbers_1))
#
# zip_object = zip(numbers_1, numbers_2, numbers_3, [10,20,30,40,50,60,70])
# print(list(zip_object))

# students = [split_name(student) for student in students] # replace map function
# students = [student for student in students if student["grade"] > 5.00] # replace filter function
# students = [split_name(student) for student in students if student["grade"] > 5.00]
# print(students)

dict_keys = ('a', 'b', 'c', 'd', 'e')
numbers = (1, 2, 3, 4, 5)
# Objective: {a:1, b:4, c:9...}
# my_dict = dict(zip(dict_keys, [nr ** 2 for nr in numbers]))
my_dict = {key: value for key, value in zip(dict_keys, [nr ** 2 for nr in numbers])}
print(my_dict)
