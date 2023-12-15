# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separater = ','):
    first_group = first_group.split(separater)
    second_group = second_group.split(separater)
    return sorted(list(set(first_group).intersection(set(second_group))))


participants_first_group = "Иванов|Петров|Cидоров"
participants_second_group = "Петров|Cидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))
