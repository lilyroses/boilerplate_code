# recursion.py

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

non_lists = []

def parse(data):
  for item in data:
    if isinstance(item, list):
      parse(item)
    elif isinstance(item, dict):
      parsed(item)
    else:
      non_lists.append(item)

def parsed(data):
  for k, v in data.items():
    if isinstance(v, list):
      parse(v)
    elif isinstance(v, dict):
      parsed(v)
    else:
print(parse(names))
print(non_lists)
