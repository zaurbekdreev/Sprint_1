types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def delete_duplicates(tickets: dict) -> dict:
    """
    Функция удаляет дубли из списков с тикетами
    :param tickets: словарь формата {str | int: [str, str...], str | int: [str, str...]...}
    """
    result = {} 
    all_tickets = [] # тут аккумулируем уникальные тикеты

    for priority, lst in tickets.items():
        lst = list(filter(lambda i: i not in all_tickets, dict.fromkeys(lst).keys())) # позволяет сохранить порядок элементов в листе
        all_tickets.extend(lst)
        result[priority] = lst
    
    return result


def map_types_and_tickets(types: dict, tickets: dict) -> dict:
    """
    Функция связывает уровень критичности со списком уникальных тикетов.
    :param types: словарь формата {1: 'Блокирующий', 2: 'Критический'...}
    :param tickets: словарь формата  {1: ['API_1', 'API_2'], 2: ['API_1', 'API_2']...}
    :returns: итоговый словарь, где ключи — это значение критичности, а значения — список с тикетами
    """
    return dict(map(lambda i: (i[1], tickets[i[0]]), types.items()))


tickets_by_type = map_types_and_tickets(types, delete_duplicates(tickets))
