name = input('What is your name?')
password = input('Enter password: ')
length = len(password)
hidden_pass='*' * length
print(f'Youe name {name} Password  {hidden_pass} is {length} long')