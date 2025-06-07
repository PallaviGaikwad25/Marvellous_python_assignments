#program to find largest among 3 numbers
def main():
    print("enter the number")
    num=int(input())
    num2=int(input())
    num3=int(input())
    if(num>=num2 and num>=num):
        max=num
    elif(num2>=num and num2>=num3):
        max=num2
    else:
        max=num3
    print("maximum number is",max)

if __name__=="__main__":
    main()