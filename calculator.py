print("1-ADD")
print("2-SUB")
print("3-MUL")
print("4-DIV")
option = int(input("enter your option no:\n"))
if(option in [1,2,3,4]):
    num1 = int(input("enter the first no:\n"))
    num2 = int(input("enter the sec no:\n"))
    if(option==1):
         result = num1+num2
    elif(option==2):
         result = num1-num2
    elif(option==3):
         result= num1*num2
    elif(option==4):
        if(num2==0):
            print("divide by zero not possible!\n")
        else:
            result = num1//num2
    print("The result is {}".format(result))         
else:
    print("invalild option!")      


