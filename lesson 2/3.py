with open("skade", "w", encoding="utf-8") as file:
    file.write("""Понедельник
    Понедельник
            Физика (лекц)
            Физика(лаб)
            Алгебра (практ)""")

lst_skade = [x for x in open("skade", encoding="utf-8")]

lec = lab = pract = 0
for i in lst_skade:
    if "лекц" in i:
        lec += 1
    elif "лаб" in i:
        lab += 1
    elif "практ" in i:
        pract += 1
    else:
        print("Проверьте расписание!")
print(f"Лекций: {lec}\nПрактических: {pract}\n")