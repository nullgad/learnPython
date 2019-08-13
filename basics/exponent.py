
def exp(num1,num2):
    res=1
    for index in range(num2):
        res = res * num1
        return res
#base=int(input("input the base  "))
#power=int(input("input the power  "))
#print("the value of the "+ str(base)+ "to the power of "+ str(power)+" is "+ str(exp(base,power)))
print(exp(5,4))