
class  Numbers:
    def __init__(self):
        self.value=int(input("enter the value==: "))

    def ChkPrime(self):
        for i in range(2,self.value):
            if self.value%i==0:
                return False
        else:
            return True

    def chkperfect(self):
        return self.sumfactors()==self.value
             
    def sumfactors(self):
        ans=0
        digit=0
        if self.value>0:
            for i in range(1,self.value):
                if self.value%i==0:
                        ans=ans+i
            return ans
        
    def factors(self):
        for i in range(1,self.value):
            if self.value%i==0:
                print(i,end=" ")
        print()
def main():
    obj1=Numbers()
    print("isprime number=",obj1.ChkPrime())
    print("Is perfect :",obj1.chkperfect())
    print("sum of factors",obj1.sumfactors())
    obj1.factors()
        

if __name__=="__main__":
    main()

    




