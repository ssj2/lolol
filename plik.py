import json

links = (("Jhon","Rob"),("Rick","Henry"),("Jack","Mark"),("Poul","Chris"),("Nick","George"),("Bob","Sam"),("Theon","Jay"),("Tom","Ronald"))

name_to_node = {}
root = {'name': 'Root', 'children': []}

for parent, child in links:

    parent_node = name_to_node.get(parent)

    if not parent_node:
        name_to_node[parent] = parent_node = {'name': parent}
        root['children'].append(parent_node)
    name_to_node[child] = child_node = {'name': child}
    parent_node.setdefault('children', []).append(child_node)

print json.dumps(root, indent=4)
with open('flare.json', 'w') as f:
     json.dump(root, f)
