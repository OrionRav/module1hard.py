grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_num = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

students_alfavit = sorted(students)
dict_1 = dict(zip(students_alfavit, grades_num))
print(dict_1)


# методом циклов
students_sort = sorted(students)
grades_rot = []
for rot in grades:
     a = sum(rot)/len(rot)
     grades_rot.append(a)

dict_2 = dict(zip(students_sort, grades_rot))
print(dict_2)


# Вам необходимо решить задачу из реальной жизни:
# ("школьные учителя устали подсчитывать вручную средний балл каждого ученика, "
#  "поэтому вам предстоит автоматизировать этот процесс"):
#
# На вход даны следующие даннные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.