import json


def decode_file(filename):
with open(filename, 'r', encoding='utf-8') as f:
data = f.read()
data = data.replace('@', 'a').replace('?', '')
return json.loads(data)


if __name__ == "__main__":
decoded = decode_file("../clues/changelogs/update_1.json")
print(decoded)
