world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
country = 'Италия'
# годы которые входят в 21 век 2001 - 2100 включительно 

winner_pattern = f'{country} cтановилась чемпионом мира по футболу в 21 веке!'
no_winner_pattern = f'{country} не выигрывала чемпионат мира по футболу в 21 веке.'

winner = next(filter(lambda i: i[1] == country and 2001 <= i[0] <= 2100, world_champions.items()), None) # регист не игнорируется! None необязательный аргумент вданном случае. 

print(winner_pattern if winner else no_winner_pattern)