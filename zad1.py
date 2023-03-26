user_input = input("Wprowadź liczby rozdzielone przecinkami: ")

numbers = [int(num) for num in user_input.split(',')]
max = numbers[0]
min =numbers[0]
for num in numbers:
    if num > max:
        max = num

for num in numbers:
    if num < min:
        min = num

print("Największa wartość: "+str(max))
print("Najmniejsza wartość: "+str(min))