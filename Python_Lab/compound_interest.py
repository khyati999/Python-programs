P=int(input('Enter Principal(Rs.):'))
R=int(input('Enter Rate of Interest:'))
t=int(input('Enter Time(yrs.):'))
print('Amount Interest:')
A=P*(1+(R/100))**t
print(A)
print('Compound Interest:')
I=A-P
print(I)
print('Principal(Rs.):',P,'\nRate of Interest(%):',R,'\nTime(yrs.)',t)