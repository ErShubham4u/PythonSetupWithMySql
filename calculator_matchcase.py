def add(a, b):
    ans = a + b
    print("add =", ans)

def sub(a, b):
    ans = a - b
    print("sub =", ans)

def mul(a, b):
    ans = a * b
    print("mul =", ans)

def div(a, b):
    ans = a / b
    print("div =", ans)

ch = int(input("ENTER CHOICE:\n1. Add\t2. Sub\n3. Mul\t4. Div: "))
match ch:
    case 1:
        fn = int(input("Enter First Number: "))
        sn = int(input("Enter Second Number: "))
        add(fn, sn)
    case 2:
        fn = int(input("Enter First Number: "))
        sn = int(input("Enter Second Number: "))
        sub(fn, sn)
    case 3:
        fn = int(input("Enter First Number: "))
        sn = int(input("Enter Second Number: "))
        mul(fn, sn)
    case 4:
        fn = int(input("Enter First Number: "))
        sn = int(input("Enter Second Number: "))
        div(fn, sn)
    case _:
        print("Invalid Choice!")
