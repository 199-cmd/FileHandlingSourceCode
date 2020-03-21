#file handling in python
#file is a collection of interralated data and information
#to store data in to a hard disk or secondary device 
#Modes in file
#write,append,read

'''
#Copy file into another
file=open("d:/first.txt","r")
file1=open("d:/first1.txt","w")
for i in file:
    file1.write(i)
file.close()
file1.close()
'''
'''

#Display output as your whole program
file=open("filehandling.py","r")
print(file.read())
file.close()

'''
'''
#Merge the two file
file=open("d:/first.txt","r")
data=file.read()
file.close()
file1=open("d:/first1.txt","a")
file1.write(data)
print(data)
file1.close()
print("Merged Success")
'''
'''
#Record Student data into a file 
new_file=open("d:/StudentRecord.txt","a")
num=int(input("ENter the number of record to insert: "))
for i in range(0,num):
    name=input("Enter the name of the student: ")
    roll=int(input("Enter the roll of student: "))
    course=input("Enter the course: ")
    fee=int(input("Enter the fee: "))
    new_file.write(name)
    new_file.write(str(roll))
    new_file.write(course)
    new_file.write(str(fee))
new_file.close()
'''
