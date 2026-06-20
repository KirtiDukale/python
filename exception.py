
# try:    
#     num1 = int(input("Enter first number: "))
#     result=100 /num1
# except ZeroDivisionError:
#         print("cannot divide by zero!")
# except valueError:
#      print("invaild input")
# else:
#       print("result:",result)
# finally:
#      print("Execution completed.")
                    

# file=open('cred.txt', 'r')
# data=file.read()
# print(data)
# file.close()

# file=open('student.txt', 'r+')
# file.write("Name: John Doe\n")
# file.write("Age: 20\n")
# file.write("Name:kirti")
# content=file.read()
# print(content)
# file.close()
with open('cred.txt','w')as file:
    file.write("name:kirti")    



with open ('cred.txt','r') as file:
    content=file.read()
    print(content)
