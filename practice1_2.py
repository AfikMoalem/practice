
#1
print ('abc' + 'def')

print ((5+5/3))

print((5+5)/3)

#2a
while True:
    try:
        num = float(input('Please enter a number: '))
        break
    except ValueError:
        print('I only accept integers')


while True:
    try:
        txt = str(input('Please enter a message: '))
        if txt.strip():
            break
        else:
            print("cannot be empty")
    except ValueError:
        print('I only accept strings')

print ("number:", num, "text:", txt)
print ("text:", txt, ", number:", num)



#2b
def calculations (num1, num2):
    try:
        print (num1 + num2)         #sum
        print(num1 - num2)          #diff
        print(num1 * num2)          #multiplication
        print(num1 // num2)         #int div
        print(int(num1 % num2))     #int modulus
        print(num1 / num2)          #float div
        print(num1 ** num2)         #power
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")




calculations(1, 1)



#2c
import random
guess1 = random.randint(1, 100)
guess2 = random.randint(1, 100)
guess3 = random.randint(1, 100)

print(guess1, guess3, guess2)


g1 = random.uniform(0,1)
g2 = random.uniform(0,1)
g3 = random.uniform(0,1)

print(g1, g2, g3)


#2d

txt = input('Please enter a message:')
txt_rev = txt[::-1]

if txt == txt_rev:
    print('result for palindrome test: True')
else:
    print ('this is not a palindrome text')


