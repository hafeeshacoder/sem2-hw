class Calculator:
    def operation(self,a,b=0,c=0):
        result=0
        for i in (a,b,c):
            if type(i) not in (int,float):
                raise ValueError("it must be int or float")
        if a!=0 and b==0 and c==0:
            result=a**2
            return result
        elif a!=0 and b!=0 and c==0:
            result=a+b
            return result
        else:
            result=a*b*c
            return result
        
cal=Calculator()
try:
    c=cal.operation(2)
    print(c)
    c1=cal.operation(2,3)
    print(c1)
    c2=cal.operation(2,3,4)
    print(c2)
    c3=cal.operation(2,3,"v")
except ValueError as e:
    print(e)
