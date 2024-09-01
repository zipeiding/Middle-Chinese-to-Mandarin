import json

filename = "middle_chinese_to_mandarin/character_dictionary.json"

with open(filename, "r", encoding="utf-8") as file:
    data = json.load(file)

character = input("Input Character ")
initial = int(input("Input Initial "))
final = int(input ("Input Final "))
tone = int(input("Input Tone "))

data[character] = [initial, final, tone]

with open(filename, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Updated JSON file successfully.")