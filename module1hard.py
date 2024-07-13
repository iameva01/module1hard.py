grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
students = list(students)
print(type(students))
print(students)
students.sort()
print(students)
grades_1 = grades[0]
grades_2 = grades[1]
grades_3 = grades[2]
grades_4 = grades[3]
grades_5 = grades[4]
grades_1 = sum(grades_1)/len(grades_1)
print(grades_1)
grades_2 = sum(grades_2)/len(grades_2)
grades_3 = sum(grades_3)/len(grades_3)
grades_4 = sum(grades_4)/len(grades_4)
grades_5 = sum(grades_5)/len(grades_5)
print(type(grades_1))
all_grades = [grades_1, grades_2, grades_3, grades_4, grades_5]
print(all_grades)
average = dict(zip(students, all_grades))
print('This is the average score of each student in the class: ', average)



