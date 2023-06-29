    _1 = ''
    _2 = ''
    _3 = ''
    _4 = ''
    _5 = ''
    for key in dict_of_days.keys():
        if key == 'Monday':
            _1 = key
        elif key == 'Tuesday':
            _2 = key
        elif key == 'Wednesday':
            _3 = key
        elif key == 'Thursday':
            _4 = key
        elif key == 'Friday':
            _5 = key

    if _1 == 'Monday':
        print(f'{_1}: {dict_of_days[_1]}')
    if _2 == 'Tuesday':
        print(f'{_2}: {dict_of_days[_2]}')
    if _3 == 'Wednesday':
        print(f'{_3}: {dict_of_days[_3]}')
    if _4 == 'Thursday':
        print(f'{_4}: {dict_of_days[_4]}')
    if _5 == 'Friday':
        print(f'{_5}: {dict_of_days[_5]}')