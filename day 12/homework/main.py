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