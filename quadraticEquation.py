#How to find the root of a quadratic equation
#the equation is (-b+sqrt((sqr(b)-4*a*c)))/2a and (-b-sqrt((sqr(b)-4*a*c)))/2a
# 
import math
print("imple Calculatr to find the Root of a Quadatic Eqution!..")
print("he Quadratic equation is (ax^2)+bx+c where a not= 0")

a=int(input("Enter the value of a :  "))
b=int(input("Enter the value of b :  "))
c=int(input("Enter the value of c :  "))

if a!= 0:
    print("our Quadratic Equation is :" "("+str(a)+ "x^2)+"+str(b)+"x+"+str(c))
else:
    print("uadratic equation cannot have value of a = 0")

# equation (-b+sqrt((sqr(b)-4*a*c)))/2a

def sqr(num2):
    return num2*num2
bsqr=int(sqr(b))
print(bsqr)
#finding determinant = (b^2)-4ac
def base(num1,num3):
    return bsqr-(4*num1*num3)
det=base(a,b)
print(det)
#if det == 0 :
    #root1=-b/(2*a)
   # print(root1)
    

#elif det <= 0:


