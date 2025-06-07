#program o check character is vowel or consonent .
def chkvc(char1):
    if(char1=="a" or char1=="A" or char1=="e" or char1=="E"or char1=="o" or char1=="O" or char1=="i"or char1=="I"or char1=="u" or char1=="U"):
       return "vowel"
    else:
        return "consonent"
        

def main():
    print("enter the chracter")
    str1=(input())
    res=chkvc(str1)
    print(f"{str1} is a" ,res)
if __name__=="__main__":
    main()