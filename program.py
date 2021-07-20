def addition ():
    num = float(input("Enter the number: "))
    a = 0
    ans = 0
    while num != 0:
        ans = ans + num
        a+=1
        num = float(input("Enter another number (enter 0 to stop): "))
    return [ans,a]

def subtraction ():
    num = float(input("Enter the number: "))
    a = 0
    ans = 0
    while num != 0:
        ans = ans - num
        a+=1
        num = float(input("Enter another number (enter 0 to stop): "))
    return [ans,a]

def multiplication ():
    num = float(input("Enter the number: "))
    a = 0
    ans = 1
    while num != 0:
        ans = ans * num
        a+=1
        num = float(input("Enter another number (enter 0 to stop): "))
    return [ans,a]

def average():
    an = []
    an = addition()
    a = an[1]
    b = an[0]
    ans = b / a
    return [ans,a]

while True:
    list = []
    print(" Enter 1 for addition")
    print(" Enter 2 for substraction")
    print(" Enter 3 for multiplication")
    print(" Enter 4 for average")
    print(" Enter 5 for quit")
    c = int(input(" "))
    if c != 5:
        if c == 1:
            print("Addition")
            list = addition()
            print("The sum of inputs is = ", list[0])
        elif c == 2:
            print("Subtraction")
            list = subtraction()
            print("The difference of inputs is= ", list[0])
        elif c == 3:
            print("Multiplication")
            list = multiplication()
            print("The product of inputs is = ", list[0])
        elif c == 4:
            print("Average")
            list = average()
            print(" The average of inputs is = ", list[0])
        else:
            print ("invalid input")
    else:
        break

