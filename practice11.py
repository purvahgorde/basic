def calculator():
    print("select option")
    print("1 :addition")
    print("2 :substraction")
    print("3 :multipliction")
    print("4 :division")

    choice = input("entre choice 1,2,3,4 : ")
    if choice in ("1","2","3","4"):
        num1= int(input("entre the num1 "))
        num2 = int(input("entre the num2"))

        if choice == "1":
            print(num1 + num2)
        elif choice == "2":
            print(num1 - num2)
        elif choice=="3":
            print(num1 * num2)
        elif choice=="4":
            print(num1/num2)  


calculator()  