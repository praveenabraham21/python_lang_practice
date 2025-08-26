words = ['cats','dogs','rats','pigs']

for word in words:
    print(word, len(word))

users  = {'praveen':'active','abraham':'inactive','keren':'active'}

for key,value in users.copy().items():
    print(key, value)
    if value == 'inactive':
        del users[key]

active_users = {}

for key, value in users.items():
    if value == 'active':
        active_users[key] = value

print(active_users)

for i in range(10):
    print(i)