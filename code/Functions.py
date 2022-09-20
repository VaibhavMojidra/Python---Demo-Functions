#Functions

def greetHello(name):
    print("Hello "+name)


greetHello("Vaibhav")
greetHello("Shreyas")
greetHello("Rohan")


def calculateAgeIn2022Birthday(birthYear):
    return 2022-birthYear

print("Vaibhav age "+str(calculateAgeIn2022Birthday(1999)))
print("Shreyas age "+str(calculateAgeIn2022Birthday(2000)))

def calculateTimeFromSeconds(seconds):
    hours=seconds//3600
    minutes=(seconds-(hours*3600))//60
    seconds=seconds-(hours*3600)-(minutes*60)
    return hours,minutes,seconds


h,m,s=calculateTimeFromSeconds(3728)

print(h)
print(m)
print(s)

#print(calculateTimeFromSeconds(3728))
