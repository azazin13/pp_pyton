list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

number_of_players = len(list_players)
slice_place = number_of_players//2

command_1 = list_players[:slice_place]
command_2 = list_players[slice_place:]

print(command_1)
print(command_2)
