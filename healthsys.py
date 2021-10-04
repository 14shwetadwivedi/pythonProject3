import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if (k==1):
        c=int(input("Enter 1 for excercise and 2 for food"))
        if (c==1):
            value=input("type here\n")
            with open("Rahul-excer.txt","a") as co:
                co.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif (c==2):
            value = input("type here\n")
            with open("Rahul-food.txt", "a") as co:
                co.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k==2):
        c = int(input("Enter 1 for excercise and 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("Rohan-excer.txt", "a") as co:
                co.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c==2):
            value = input("type here\n")
            with open("Rohan-food.txt", "a") as co:
                co.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k==3):
        c = int(input("Enter 1 for excercise and 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("Rohit-excer.txt", "a") as co:
                co.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c==2):
            value = input("type here\n")
            with open("Rohit-food.txt", "a") as co:
                co.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1 for Rahul,2 for Rohan,3 for Rohit")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excercise and 2 for food"))
        if(c==1):
            with open("Rahul-excer.txt") as co:
                for i in co:
                    print(i,end="")
        elif(c==2):
            with open("Rahul-food.txt") as co:
                for i in co:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for excercise and 2 for food"))
        if (c==1):
            with open("Rohan-excer.txt") as co:
                for i in co:
                    print(i, end="")
        elif (c==2):
            with open("Rohan-food.txt") as co:
                for i in co:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for excercise and 2 for food"))
        if (c == 1):
            with open("Rohit-excer.txt") as co:
                for i in co:
                    print(i, end="")
        elif (c == 2):
            with open("Rohit-food.txt") as co:
                for i in co:
                    print(i, end="")
    else:
        print("Please enter valid input (rahul,rohan,rohit")
print("Health Management System: ")
a=int(input("Press 1 for log the value and 2 for retrieve:"))

if (a==1):
    b = int(input("Press 1 for Rahul 2 for Rohan 3 for Rohit:"))
    take(b)
else:
    b = int(input("Press 1 for Rahul 2 for Rohan 3 for Rohit:"))
    retrieve(b)
