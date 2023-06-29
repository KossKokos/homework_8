from datetime import datetime, timedelta
lst = [{'Kostia':datetime(2005, 6, 29)}, 
       {'Nastia': datetime(2005, 6, 30)}, 
       {'Vasia': datetime(2005, 7, 3)}, 
       {'Daniel': datetime(2005, 7, 7)}, 
       {'Obama': datetime(2005, 7, 2 )}, 
       {'Volodia': datetime(2000, 7, 6)},
       {'Donald': datetime(2006, 7, 5)}]
def get_birthdays_per_week(list_of_workers):
    lst_names = []
    current_date = datetime.now()
    weeekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for dct in list_of_workers:
        for key, value in dct.items():
            birthday = datetime(year=current_date.year, month=value.month, day=value.day)
            less_than_7 = birthday - current_date

            if less_than_7.days >= 0 and less_than_7.days < 7:
                dict_of_dates = {key:datetime(year=current_date.year,month=value.month, day=value.day )}
                lst_names.append(dict_of_dates)
            else:
                continue
    str_lst = []
    final_dict = {}
    for i in weeekdays:
        final_dict.update({i: []})
    for dicts in lst_names:
        for name, week in dicts.items():
            weekday = week.strftime('%A')
            
            if weekday == 'Saturday' or weekday == 'Sunday':
                final_dict['Monday'].append(name)
            else:
                final_dict[weekday].append(name)

    for day, names in final_dict.items():
        if names == []:
            str_result = ' '
            str_lst.append(str_result)
        else:
            str_result = f'{day}: {", ".join(names)}'
            str_lst.append(str_result)

    count_day = current_date.weekday()      

    for _ in str_lst:
        from_day_lst = str_lst[count_day+1:]
        to_day_lst = str_lst[0:count_day+1]

    for i in from_day_lst:
        if i != ' ':
            print(i)

    for k in to_day_lst:
        if k != ' ':
            print(k)

get_birthdays_per_week(lst)
