#assignment
#1.print patricia, faith, phiona and anitah
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']

print(student_names[1:5])


#2.add masha at the forth position
student_names.insert(4, 'Marsha')
print(student_names)


#3.update the name phiona to Phiona Aladina
student_names[3]= 'Phionah Aladinah'
print(student_names)


#4.display the length of the student list
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
print(len(student_names))


#5.print all the student names having updated using a for loop
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
for x in student_names:
    print (x)


#6.calculate the total marks for the student marks variable ans = 304
student_marks = [80,56,78,90]
total_marks = sum(student_marks)
print(f"The sum for student_marks is {total_marks}.")
