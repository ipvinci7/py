print("Simple calculator program\n")

print("Choose operation\n")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("1. Addition \n 2. Subtraction \n 3. Multiplication  \n 4. Division")

operation = int(input())

match operation:
    case 1:
        result = add(9,16)
        print(result)
    case 2:
        result = sub(19,10)
        print(result)
    case 3:
        result = mul(9,17)
        print(result)
    case 4:
        result = div(7,3)
        print(result)


  