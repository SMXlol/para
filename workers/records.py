import json
import requests

workers = {
    "Россия": "Москва",
    "Беларусь": "Минск",
    "Казахстан": "Нур-Султан"
}

workers_json = json.dumps(workers)
with open("workers.json", "w") as my_file:
    my_file.write(workers_json)
