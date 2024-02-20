#read files in the python is a tool that reads the files from the system and displays the content of the file in the output

# to read the file in the python we use the open() function

employee_file =  open("employee.txt","r")
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readlines()[1])
# print(employee_file.readlines()[2])
# print(employee_file.readlines())
# print(employee_file.readline())
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


employee_file =  open("employee.txt","a")
print(employee_file.write("Toby - Human Resources"))
employee_file.close()

employee_file =  open("employee1.txt","w")
print(employee_file.write("Toby - Human Resources"))
employee_file.close()

employee_file =  open("index.html","a")
print(employee_file.write("<p>hello</p>"))
employee_file.close()