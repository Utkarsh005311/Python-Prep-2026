def Swap():
    x=int(input("Enter 1st Number to Swap: "))
    y=int(input("Enter 2nd Number to Swap: "))
    print("Num 1 earlier:",x)
    print("Num 2 earlier:",y)
    tmp=x
    x=y
    y=tmp
    print("Num 1 now :",x)
    print("Num 2 now :",y)
def main():
    Swap()
main()
    
