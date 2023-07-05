p=int(input('Enter Principal(Rs.):'))
r=int(input('Enter Rate of Interest(%):'))

t=int(input('Enter Time(yrs.):'))

print('Simple Interest :')
si=(p*r*t)/100
print(si)
print('Amount computation:')
a=p+si
print(a)
print('Principal(Rs.):',p,'\nRate of Interest(%):',r,'\nTime(yrs.)',t)