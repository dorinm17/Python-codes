print('Cand vei implini 100 de ani?\n\n')
print('Introdu:')
input('-numele tau: ')
age=int(input('-varsta pe care ai implinit-o/o vei implini anul acesta: '))
if age<0:
    print('Imposibil.')
elif age>=100:
    print('Deja ai implinit 100 de ani. Felicitari!')
else:
    current_year=int(input('-anul curent: '))
    year100=int(current_year)-int(age)+100
    del(age)
    del(current_year)
    print('Vei implini 100 de ani in: '+str(year100)+'\n')
    num=input('Introdu un numar: ')
    print(('Vei implini 100 de ani in: '+str(year100)+'\n')*int(num))


