s1 = input("Enter your exercise time 1: ")
s2 = input("Enter your exercise time 2: ")
s = int(s1)+int(s2)
h = int(s/3600)
s = s-(h*3600)
m = int(s/60)
s = s-(m*60)
print("It is "+str(h)+" hours "+str(m)+" minutes and "+str(s)+" seconds.")