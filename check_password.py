passwordFile = open('SecretPassword.txt')
SecretPassword = passwordFile.read()
print('Enter your password')

typedPassword = input()
if typedPassword == SecretPassword:
    print('Access granted')
elif typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage')
else:
    print('Access Denied')
