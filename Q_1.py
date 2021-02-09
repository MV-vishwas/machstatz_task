import json
from convert_time import change_time_str_to_obj,convert_input_time
from datetime import datetime

def shift_time_change(date_time_str):
    date_time_obj = datetime.strptime(date_time_str, "%H:%M:%S").time()
    return date_time_obj


def question_1_solution(start_time,end_time):
    start_time =convert_input_time(start_time)
    end_time = convert_input_time(end_time)
    # print(start_time,end_time)

    shift_A_start=shift_time_change("00:30:00")
    shift_B_start=shift_time_change("08:30:00")
    shift_C_start=shift_time_change("14:30:00")
    shift_A_end=shift_time_change("08:30:00")
    shift_B_end=shift_time_change("14:30:00")
    shift_C_end=shift_time_change("00:30:00")

    

    AA_c=0
    AB_c=0
    BA_c=0
    BB_c=0
    CA_c=0
    CB_c=0
    with open("./static/Q1_data.json",'r') as f:
        data=json.load(f)
        for item in data:
            str_date_time=item['time']    
            item_date=change_time_str_to_obj(str_date_time)
            # print(type(start_time),type(item_date),type(end_time))
            if start_time<=item_date<=end_time:
                # print(item_date)
                if shift_A_start<item_date.time()<=shift_A_end:
                    if item['production_A']==True:
                        AA_c+=1
                    if item['production_B']==True:
                       AB_c+=1
                if shift_B_start<item_date.time()<=shift_B_end:
                    if item['production_A']==True:
                        BA_c+=1
                    if item['production_B']==True:
                       BB_c+=1  

                if shift_C_start<item_date.time()<=shift_C_end:
                    if item['production_A']==True:
                        CA_c+=1
                    if item['production_B']==True:
                       CB_c+=1    
    
    ans_data={
                "shiftA":{"production_A_count" :AA_c, "production_B_count" :AB_c},
                "shiftB":{"production_A_count" :BA_c, "production_B_count" :BB_c},
                "shiftC":{"production_A_count" :CA_c, "production_B_count" :CB_c}
            }
    return ans_data

if __name__ == "__main__":
    ans=question_1_solution("2021-01-28T07:30:00Z","2021-01-28T13:30:00Z")
    print(ans)