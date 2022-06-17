# empty class means no attribute and no method
class Student:
 pass
# create objects of this class
Std_1=Student()
Std_2=Student()
# how to define instance variable
# Instance variable nothing but they are unique for each and every object
Std_1.first='Neel'
Std_1.last='Verma'
Std_1.email='Neel@School.com'
Std_1.marks=55
Std_2.first='Hement'
Std_2.last='Sharma'
Std_2.email='Hement@School.com'
Std_2.marks=90
#How to accces these instance variables 
#print the email address of both the students
print(Std_1.email)
print(Std_2.email)