# import csv
#
# def write_holiday_cities(first_letter):
#     visited_cities = set()
#     wish_cities = set()
#
#     with open('travel-notes.csv', 'r', newline='') as csv_file:
#         csv_data = csv.reader(csv_file)
#         for line in csv_data:
#             name, visited, wish = line
#             if name.startswith(first_letter.upper()):
#                 visited_cities.update(visited.split(', '))
#                 wish_cities.update(wish.split(', '))
#
#     never_visited = wish_cities - visited_cities
#
#     print(f'Посетили: {sorted(visited_cities)}')
#     print(f'Хотят посетить: {sorted(wish_cities)}')
#     print(f'Не посетили: {sorted(never_visited)}')
#
#
#
#
# fl = input()
# write_holiday_cities(fl)


# import csv
#
#
# def write_holiday_cities(first_letter):
#     visited_cities = set()
#     wish_cities = set()
#
#     # Read the travel_notes.csv file
#     with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#
#         for row in reader:
#             name, visited, wish = row
#             if name.startswith(first_letter.upper()):
#                 # print(visited)
#                 # print(type(visited))
#                 # v_c = visited.split(';')
#                 # print(v_c)
#                 visited_cities.update(visited.split(';'))
#                 wish_cities.update(wish.split(';'))
#
#     # Calculate cities they want to visit but have not been to
#     never_visited = wish_cities - visited_cities
#
#     # Determine the next city they will visit in alphabetical order
#     next_city = sorted(never_visited)[0] if never_visited else 'N/A'
#
#     # Sort all the cities
#     visited_cities = sorted(visited_cities)
#     wish_cities = sorted(wish_cities)
#     never_visited = sorted(never_visited)
#
#     print(f'Посетили: {(visited_cities)}')
#     print(f'Хотят посетить: {(wish_cities)}')
#     print(f'Не посетили: {(never_visited)}')
#     print(f'Следующим городом будет: {next_city}')
#
#     # Write the results to holiday.csv
#     with open('holiday.csv', mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#
#         writer.writerow(['Посетили:' + ', '.join(visited_cities)])
#         writer.writerow(['Хотят посетить:' + ', '.join(wish_cities)])
#         writer.writerow(['Никогда не были в:' + ', '.join(never_visited)])
#         writer.writerow(['Следующим городом будет:' + next_city])
#
#
# # Пример вызова функции
# write_holiday_cities('N')


import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wish_cities = set()

    with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            if name.startswith(first_letter.upper()):
                visited = row[1].split(';')
                wish = row[2].split(';')
                visited_cities.update(visited)
                wish_cities.update(wish)

    never_visited = wish_cities - visited_cities

    next_city = sorted(never_visited)[0] if never_visited else 'N/A'

    visited_cities = sorted(visited_cities)
    wish_cities = sorted(wish_cities)
    never_visited = sorted(never_visited)

    with open('holiday.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Посетили:', ', '.join(visited_cities)])
        writer.writerow(['Хотят посетить:', ', '.join(wish_cities)])
        writer.writerow(['Никогда не были в:', ', '.join(never_visited)])
        writer.writerow(['Следующим городом будет:', next_city])




fl = input('Введите первую букву имени: ')
write_holiday_cities(fl)
