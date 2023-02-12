import random

with open("16.txt", "w") as file:
    file.write(str(random.randint(123123123213231231,
                              99999999999999999999999)))
lst = [x for x in open("16.txt")]
print(lst)
answer = set()
for i in range(len(lst[0])):
    print(lst[0][i])