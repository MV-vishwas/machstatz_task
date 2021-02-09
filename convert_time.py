from datetime import datetime
# from pytz import timezone

def change_time_str_to_obj(date_time_str):
    date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    return date_time_obj


def convert_input_time(time):
    
    date_time_str = time[0:-1]
    date_time_str=date_time_str.replace('T',' ')
    
    date_time_obj = change_time_str_to_obj(date_time_str)

    return date_time_obj


