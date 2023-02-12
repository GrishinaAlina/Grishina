f = open("test.txt", "w", encoding="utf-8")
f.writelines(["a \n a", "\nmother", "\npapa", "\nсобака"])
f.close()

with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())


with open("test1.txt", "x") as f:
   print(f.write("хочу лето!!!!!!!"))
