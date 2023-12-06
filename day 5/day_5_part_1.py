phrase = input("Введіть рядок з 15 символів: ")

if not phrase:
    print("Ви ввели пустий рядок.")
    exit()
while len(phrase) < 15:
    phrase *= 3

phrase_list = list(phrase)
print("Повний список", phrase_list)
print("Останні 5 елементів:", phrase_list[-5:])
print("Список у зворотній послідовності:", phrase_list[::-1])
print("Елементи з парними індексами:", phrase_list[::2])
temp_list = phrase_list[-5:]
print("Перші 5 елементів однакові к кінці та на початку:", temp_list + phrase_list)
print("Список без 2 перших і 2 останніх елементів:", phrase_list[2:-2])