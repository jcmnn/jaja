import json


with open("keyboard_layout.json") as f:
    table = json.load(f)

cntr = 1
for row in table:
    for i, c in enumerate(row):
        if isinstance(c, str):
            row[i] = str(cntr)
            cntr = cntr + 1

with open("numbered_layout.json", "w") as f:
    json.dump(table, f)