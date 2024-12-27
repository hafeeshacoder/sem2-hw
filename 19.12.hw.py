'''roman = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

n = int(input("Enter a number: "))
result = ''

for value,numeral in roman:
    while n >= value:
        result += numeral
        n -= value

print(result)
'''
roman = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]
roma_int=input("Enter the roman:")#CXX
number=0
i=0
while i<len(roma_int):#0<3
    for value,letter in roman:
        if roma_int[i:i+len(letter)]==letter:#0+3=3
            number+=value#
            i+=len(letter)
            break
print(number)        
