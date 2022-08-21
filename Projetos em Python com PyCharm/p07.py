n1=int(input('Um valor:'))
n2=int(input('Outro valor:'))
#print('a soma vale:{}'.format(n1+n2))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1**n2
e= n1^n2
print('a soma é {}, produto é {}, e a divisão é {:.2f}'.format(s,m,d), end=' >>> ')
print('divisão inteira {}','e potência {}'.format(di,e))