from random import *


a=randint(-100,200)
if a%2==0:
    print("Juhuslik arv on",a)
    print(a,"-paaris arv")

if a>0:
    print(a,"suurem kui 0")
else:
    print(a,"väiksem kui 0 või võrdne 0-ga")

#<0,>100 ei soobi, 0-59-"2",60-75-"3",76-90-"4",91-100-"5"
if a<0 or a>100:
    print("Viga tulemustega!")
elif a>= and a<60:
    print("Hinne 2")
elif a>=60 and a<76:
    print("Hinna 3")
elif a>=76 and a<91:
    print("Hinna 4")
else:
    print("Hinna 5")
