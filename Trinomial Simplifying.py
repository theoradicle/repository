def multiply(a,b,c):
    print(str("x^3+"+str((a+b+c)*-1)+"x^2+"+str(a*b+b*c+a*c)+"x+"+str(a*b*c*-1)).replace("+-","-"))
equation=input("Input trinomial: ")
equation=equation.replace("+","--")
equation=equation.replace("(x-","")
equation=equation.split(")")
multiply(int(equation[0]),int(equation[1]),int(equation[2]))
