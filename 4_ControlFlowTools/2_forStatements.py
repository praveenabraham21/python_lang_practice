"""Python's for statement iterate over the items of any sequence - list, string in the order that they appear
in the sequence"""

# iterating a list
words = ['cats', 'dogs', 'rats', 'pigs']

for word in words:
    print(word, len(word))

# iterating a string
for word in 'String':
    print(word)

# iterating a collection
users = {'praveen': 'active', 'abraham': 'inactive', 'keren': 'active'}

# generating a copy of the collections to iterate.
for key, value in users.copy().items():
    print(key, value)
    if value == 'inactive':
        del users[key]

# creating a new list and copying the items.
active_users = {}
for key, value in users.items():
    if value == 'active':
        active_users[key] = value

print(active_users)
