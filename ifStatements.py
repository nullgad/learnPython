name= input("what is your name ? \n")
print("hi "+ name)

age=input("How old are you ? \n ")

if int(age)<13:

    print("you are young ")


elif int(age)>=13 and int(age)<=19:
    print("OOPS !!! Puberty ")

elif int(age)>19 and int(age)<=30: 
    print("Good and confusing time of life")

elif int(age)>30 and int(age)>=60:
    print("Work the Shit out ")

else:
    print("Time to Sit out ")

