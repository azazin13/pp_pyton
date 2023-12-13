users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

my_dict = {'Общее количество':0, 'Уникальные посещения':0}

my_dict['Общее количество'] = len(users)

uniq_users = []

for i in range(0, len(users)):
    if users[i] not in uniq_users:
        uniq_users.append(users[i])

my_dict['Уникальные посещения'] = len(uniq_users)

print(my_dict)