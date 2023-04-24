from  src.utils import filter_sort, load_data, format_data, mask_card, formatted_data


def test_load_data():
    list_ = [
              {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }
            ]

    assert load_data('test.json') == list_


def test_filter_sort():
    list_ = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2019-06-30T02:08:58.425572'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-06-30T02:08:58.425572'
        }
    ]

    sorted_list = [
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-06-30T02:08:58.425572'
        },
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572'
        }
    ]

    assert filter_sort(list_) == sorted_list


def test_format_date():
    assert format_data('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert format_data('2018-04-04T17:33:34.701093') == '04.04.2018'


def test_mask_card():
    assert mask_card('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'
    assert mask_card('MasterCard 3152479541115065') == 'MasterCard 3152 47** **** 5065'
    assert mask_card('Счет 48894435694657014368') == 'Счет **4368'


def test_formatted_data():
    dict_ = {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }

    str_ = f'''
26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.\n'''

    assert formatted_data(dict_) == str_
