
def pharmacy_working_hours(pharmacy):
    return ' '.join(pharmacy.find('div', {'class' : 'apteka_time'}).get_text().split())



def check_working_time(office):
    try:
        working_days = f'пн-пт {office["hoursOfOperation"]["workdays"]["startStr"]} до \
    {office["hoursOfOperation"]["workdays"]["endStr"]}'
        is_working_saturday = office["hoursOfOperation"]["saturday"]["isDayOff"]
        is_working_sunday = office["hoursOfOperation"]["sunday"]["isDayOff"]
        weekend_working_time = f'{office["hoursOfOperation"]["saturday"]["startStr"]}-\
    {office["hoursOfOperation"]["saturday"]["endStr"]}'

        if all([is_working_saturday, is_working_sunday]):
            weekend_days = f'cб-вс {weekend_working_time}'
        elif any([is_working_saturday, is_working_sunday]):
            weekend_days = f'вс {weekend_working_time}'
        else:
            weekend_days = ''
    except:
        return [working_days, 'сб-вс']

    return [working_days, weekend_days]