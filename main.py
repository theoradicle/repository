trinomial=input("Enter trinomial: ")
trinomial=trinomial.replace("-","+-").replace("x^3","").replace("x^2","").replace("x","").split("+")
a=trinomial[0]
b=trinomial[1]
c=trinomial[2]
d=trinomial[3]
if a=="":
    a="1"
elif a=="-":
    a="-1"
if b=="":
    b="1"
elif b=="-":
    b="-1"
if c=="":
    c="1"
elif c=="-":
    c="-1"
a=int(a)
b=int(b)
c=int(c)
d=int(d)
factorsa=[]
factorsd=[]
factored=[]
test=[]
def plugin(x):
    return a*x**3+b*x**2+c*x+d
for i in range(1,abs(a)+1):
    if a%i==0:
        factorsa.append(i)
for i in range(1,abs(d)+1):
    if d % i==0:
        factorsd.append(i)
for num in factorsd:
    for den in factorsa:
        test.append(num/den)
for i in range(len(test)):
    test.append(-test[i])
for i in test:
    if plugin(i)==0:
        factored.append(i)
print(str("(x-"+str(factored[0])+")(x-"+str(factored[1])+")(x-"+str(factored[2])+")").replace("--","+").replace(".0",""))