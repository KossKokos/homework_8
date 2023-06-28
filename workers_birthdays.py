from datetime import datetime, timedelta
lst = [{'Kostia':datetime(2005, 6, 28)}, 
       {'Nastia': datetime(2005, 6, 30)}, 
       {'Vasia': datetime(2005, 6, 5)}, 
       {'Daniel': datetime(2005, 6, 28)}, 
       {'Obama': datetime(2005, 7, 2 )}, 
       {'Volodia': datetime(2000, 7, 6)},
       {'Donald': datetime(2006, 7, 5)}]
def get_birthdays_per_week(list_of_workers):
    lst_names = []
    dict_of_days = {}
    current_date = datetime.now()
    for dct in list_of_workers:
        for key, value in dct.items():
            birthday = datetime(year=current_date.year, month=value.month, day=value.day)
            less_than_7 = birthday - current_date
            if less_than_7.days >= -1 and less_than_7.days <= 6:
                dict_of_dates = {key:datetime(year=current_date.year,month=value.month, day=value.day )}
                lst_names.append(dict_of_dates)
            else:
                continue
    
    for dicts in lst_names:
        for name, week in dicts.items():
            weekday = week.strftime('%A')
            if weekday == 'Sunday' or weekday == 'Saturday':
                weekday = 'Monday' 
            if weekday in dict_of_days.keys():
                dict_of_days[weekday] += f', {name}' 
            else:
                dict_of_days.update({weekday: name})
             
    print(dict_of_days)
    _1 = ''
    _4 = ''
    _5 = ''
    _2 = ''
    _3 = ''
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

get_birthdays_per_week(lst)
