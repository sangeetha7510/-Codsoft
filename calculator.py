while True:
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    c=int(input("Enter the corresponding operation number : "))
    if c==1:
        print("Addition of a and b are :")
        print(a+b)
    elif c==2:
        if(a>b):
            print("Subtraction of a and b are :")
            print(a-b)
        elif(a<b):
            print("Subtraction of b and a are :")
            print(b-a)
    elif c==3:
        print("Multiplication of a and b are :")
        print(a*b)
    elif c==4:
        print("Division of a and b are :")
        print(a/b)
    elif c==5:
        print("exiting the loop")
        break
    else:
        print("enter between existing numbers")
        
