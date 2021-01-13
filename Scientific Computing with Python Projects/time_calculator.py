"""Write a function named add_time that takes in two required parameters and one optional parameter:
a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will
be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the
week of the result. The day of the week in the output should appear after the time and before the number of days later.
"""

def change_zero_for_twelve(hour):
    """If the input is zero changes it to
    twelve, otherwise it makes nothing"""
    if hour == 0:
        hour = 12
    return hour


def add_time(start_time, duration, start_week_day='no day'):
    """takes in two required parameters and one optional parameter:
    a start time in the 12-hour clock format (ending in AM or PM)
    a duration time that indicates the number of hours and minutes
    (optional) a starting day of the week, case insensitive
    and adds the duration time to the start time and returns the result."""
    start_time = start_time.rsplit(':')
    start_hour = start_time[0]
    start_minutes = (start_time[1].rsplit(' '))[0]
    start_am_pm = (start_time[1].rsplit(' '))[1]
    duration = duration.rsplit(':')
    duration_hour = duration[0]
    duration_minutes = duration[1]
    start_week_day = start_week_day.lower() #because we need it to be case insensitive
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if start_week_day == 'no day':
        #first case: the optional parameter is empty
        new_hour = int(start_hour) + int(duration_hour)
        new_min = int(start_minutes) + int(duration_minutes)
        aux = new_min // 60
        new_min = new_min - aux * 60 # we substract the "hours" hidden in the minutes
        new_hour = new_hour + aux # we add the hours that were in the minutes place to the hours place
        aux_2 = new_hour // 12
        if start_am_pm.__contains__('AM'):
            if aux_2 == 0:
                new_time = str(change_zero_for_twelve(new_hour))+':'+'{0:0=2d}'.format(new_min)+' AM'
            elif aux_2 == 1:
                new_hour = new_hour-12
                new_time = str(change_zero_for_twelve(new_hour))+':'+'{0:0=2d}'.format(new_min)+' PM'
            elif aux_2 == 2:
                new_hour = new_hour-2*12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' AM'+' (next day)'
            elif aux_2 == 3:
                new_hour = new_hour-3*12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' PM'+' (next day)'
            else:
                new_hour = new_hour - aux_2 * 12
                if aux_2%2==0:
                    days_passed = str((aux_2//2)+1)
                    new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' AM' + ' ('+ days_passed+' days later)'
                else:
                    days_passed = str((aux_2//2)+1)
                    new_time =str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' PM' + ' (' + days_passed + ' days later)'

        else:
            if aux_2 == 0:
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM'
            elif aux_2 == 1:
                new_hour = new_hour - 12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' AM' + ' (next day)'
            elif aux_2 == 2:
                new_hour = new_hour - 2 * 12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM' + ' (next day)'
            else:
                new_hour = new_hour - aux_2 * 12
                if aux_2 % 2 == 0:
                    days_passed = str(aux_2//2)
                    new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM' + ' (' + days_passed + ' days later)'
                else:
                    days_passed = str((aux_2//2)+1)
                    new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' AM' + ' (' + days_passed + ' days later)'

    else:
        #second case: optional parameter is not empty
        new_hour = int(start_hour) + int(duration_hour)
        new_min = int(start_minutes) + int(duration_minutes)
        aux = new_min // 60
        new_min = new_min - aux * 60
        new_hour = new_hour + aux
        aux_2 = new_hour // 12
        index = week_days.index(start_week_day) # finding the place where is the day given in our "week_days" list
        if start_am_pm.__contains__('AM'):
            if aux_2 == 0:
                new_time = str(change_zero_for_twelve(new_hour))+':'+'{0:0=2d}'.format(new_min)+' AM'+', '+start_week_day.capitalize()
            elif aux_2 == 1:
                new_hour = new_hour-12
                new_time = str(change_zero_for_twelve(new_hour))+':'+'{0:0=2d}'.format(new_min)+' PM'+', '+start_week_day.capitalize()
            elif aux_2 == 2:
                new_hour = new_hour-2*12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' AM'+', '+week_days[index+1].capitalize()+' (next day)'
            elif aux_2 == 3:
                new_hour = new_hour-3*12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' PM'+', '+week_days[index+1].capitalize()+' (next day)'
            else:
                new_hour = new_hour - aux_2 * 12
                if aux_2%2==0:
                    days_passed = str((aux_2//2)+1)
                    new_time = str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' AM' +', '+week_days[(index+int(days_passed))%7].capitalize()+' ('+ days_passed+' days later)'
                else:
                    days_passed = str((aux_2//2)+1)
                    new_time =str(change_zero_for_twelve(new_hour))+ ':' +'{0:0=2d}'.format(new_min)+ ' PM' +', '+week_days[(index+int(days_passed))%7].capitalize()+' (' + days_passed + ' days later)'

        else:
            if aux_2 == 0:
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM'+', '+start_week_day.capitalize()
            elif aux_2 == 1:
                new_hour = new_hour - 12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' AM'+', '+week_days[index+1].capitalize() + ' (next day)'
            elif aux_2 == 2:
                new_hour = new_hour - 2 * 12
                new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM'+', '+week_days[index+1].capitalize() + ' (next day)'
            else:
                new_hour = new_hour - aux_2 * 12
                if aux_2 % 2 == 0:
                    days_passed = str(aux_2//2)
                    new_time = str(change_zero_for_twelve(new_hour))+ ':' + '{0:0=2d}'.format(new_min) + ' PM'+', '+week_days[(index+int(days_passed))%7].capitalize() + ' (' + days_passed + ' days later)'
                else:
                    days_passed = str((aux_2//2)+1)
                    new_time = str(change_zero_for_twelve(new_hour)) + ':' + '{0:0=2d}'.format(new_min) + ' AM'+', '+week_days[(index+int(days_passed))%7].capitalize() + ' (' + days_passed + ' days later)'

    return new_time
