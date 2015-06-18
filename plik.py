import json

names = (("Jhon","Rob"),("Rick","Henry"),("Jack","Mark"),("Poul","Chris"),("Nick","George"),("Bob","Sam"),("Theon","Jay"),("Tom","Ronald"))

name_to_node = {}
lol = {'name': 'Lol', 'children': []}

for parent, child in names:

    parent_node = name_to_node.get(parent)

    if not parent_node:

        name_to_node[parent] = parent_node = {'name': parent}
        lol['children'].append(parent_node)
    name_to_node[child] = child_node = {'name': child}
    parent_node.setdefault('children', []).append(child_node)

print json.dumps(lol, indent=4)
with open('flare.json', 'w') as f:
     json.dump(lol, f)
