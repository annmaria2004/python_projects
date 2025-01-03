task=[]
def add():
     item = input("Enter the item\n")
     task.append(item)
def remove():
    rtask = input("Enter the task to be removed\n")
    if(rtask in task):
        task.remove(rtask)
    else:
        print("task not in the list")
def dispaly():
    print("TO DO:\n")
    for item in task:
        print(item)


    

while True :

    print("TO DO LIST")
    print("************************************")
    print("1-ADD TO THE LIST")
    print("2-REMOVE FROM THE LIST")
    print("3-DISPLAY THE LIST")
    print("4-EXIT")
    print("************************************")
    option = int(input("Enter the required option\n"))
    if(option==1):
        add()
    elif(option==2):
        remove()
    elif(option==3):
        dispaly()
    else:
        break

