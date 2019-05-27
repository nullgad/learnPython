#How to find the root of a quadratic equation
#the equation is (-b+sqrt((sqr(b)-4*a*c)))/2a and (-b-sqrt((sqr(b)-4*a*c)))/2a
# 
import math
print("Simple Calculatr to find the Root of a Quadatic Eqution!..\n\n\n")
print("The Quadratic equation is (ax^2)+bx+c where a not= 0\n\n\n")

a=int(input("Enter the value of a :  "))
b=int(input("Enter the value of b :  "))
c=int(input("Enter the value of c :  "))

if a!= 0:
    print("our Quadratic Equation is :" "("+str(a)+ "x^2)+"+str(b)+"x+"+str(c)+"\n")

# equation (-b+sqrt((sqr(b)-4*a*c)))/2a

#finding determinant = (b^2)-4ac
    def base(num1,num3):
     return (b**2)-(4*num1*num3)
    det=base(a,c)
    if det == 0 :
        root1=-b/(2*a)
        print("the root -b/(2a)= " + str(root1))
    

    elif det > 0:
        root2=((-b-(math.sqrt(det)))/(2*a))
        root3=((-b+(math.sqrt(det)))/(2*a))
        print("the root -b+-((b^2)-(4ac))/(2a)= \n\n" + str(root2)+ "\n" + " and "+ "\n" + str(root3))

    else :
        print("The asnwer includes an Imaginary number which at this point am not able to do in python ")


else:
    print("Qadratic equation cannot have value of a = 0 \n")
