name = "iuri"
print(name[1], name[0], name[3])


#strings are mutable and lists are immutable---thats false becouse when string is created we cant change that string and lists are mutable becouse you can change the words in the list <3

info = []
while True:
  you =  input("enter the info about you: ")
  info.append(you)
  choice = input("enter another information? (y / n): ")
  if choice.casefold() == 'n':
    break
  for element in info:
    print(element)