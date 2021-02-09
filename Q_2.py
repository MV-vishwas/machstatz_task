from convert_time import change_time_str_to_obj,convert_input_time
import json
from datetime import datetime

def convert_seconds(seconds):
	seconds = seconds % (24 * 3600) 
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	
	return f'{hour}h:{minutes}m:{seconds}s'
	


def question_2_solution(start_time,end_time):
    start_time =convert_input_time(start_time)
    end_time = convert_input_time(end_time)
    # print(start_time,end_time)


    total_runtime=0
    total_downtime=0
    with open("./static/Q2_data.json",'r') as f:
        data=json.load(f)
        for item in data:
            str_datetime=item['time']
            item_date=change_time_str_to_obj(str_datetime)
            if start_time<=item_date<=end_time:
                item_runtime=item['runtime']
                item_downtime=item['downtime']
                if item_runtime>1021:
                    # print(item_runtime)
                    # print(item_downtime)
                    item_downtime=(item_runtime-1021)+item_downtime
                    # print((item_runtime-1021)//60)
                    item_runtime=1021
                
                total_runtime=total_runtime+item_runtime
                total_downtime=total_downtime+item_downtime
    
    # utilisation = (total runtime)/(total runtime + total downtime) * 100
    utilisation=(total_runtime)/(total_runtime+total_downtime)*100

    ans_data={
	"runtime" : convert_seconds(total_runtime),
	"downtime": convert_seconds(total_downtime),
	"utilisation": round(utilisation,2)
    }

    return ans_data

if __name__ == "__main__":
    ans=question_2_solution("2021-01-28T08:30:00Z","2021-01-28T10:30:00Z")
    print(ans)


