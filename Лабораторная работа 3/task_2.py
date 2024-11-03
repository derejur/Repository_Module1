def find_common_participants(first_group, second_group, split=','):  # Разделяю строки на списки участников с помощью метода split
    first_participants = first_group.split(split)
    second_participants = second_group.split(split)
    common_participants = set(first_participants).intersection(second_participants)     # Преобразую списки в множества
    return sorted(common_participants)  # Возвращаю отсортированный список всех участников

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)  # Проверяю работу функции
print("Общие участники:", common_participants)