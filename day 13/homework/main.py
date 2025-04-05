number = int(input("Enter number: "))
count = 0

for divider in range(2, (number // 2) + 1):
    if number % divider == 0:
        count = count + 1
        break

if count == 0:
    print("Number is prime")
else:
    print("NUmber is not prime")


    healthy_products = ["Tomato", "Apple", "Orange", "Alucha", "Cucumber"]

healthy_products.pop(0)
healthy_products.pop()

print(healthy_products)


```numbers = []

for i in range(5):
    number = int(input("Please enter a number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
```