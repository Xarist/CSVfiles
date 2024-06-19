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
