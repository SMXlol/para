# Это задание библиотека
import json
def out():
    import json

    with open("dad.json", "r") as my_file:
        capitals_json = my_file.read()
    capitals = json.loads(capitals_json)
    print(capitals)
def write():
    name = str(input())
    date = str(input())
    cout = str(input())
    autor= str(input())
    with open('dad.json', 'r') as dad:
        dad = dad.read()
        data = [json.loads(dad)]
    data.append({
        "book": [
            {
                "Name_of_book": name,
                "Data_of_create": date,
                "Cout_of_pages": cout,
                "Autor": autor
            }
        ]
    })
    with open("dad.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
write()
out()
