from convert_time import change_time_str_to_obj,convert_input_time
import json
from datetime import datetime


def question_3_solution(start_time,end_time):
    start_time =convert_input_time(start_time)
    end_time = convert_input_time(end_time)
    # print(start_time,end_time)


    all_id_list=[]
    with open("./static/Q3_data.json",'r') as f:
        data=json.load(f)
        for item in data:
            str_datetime=item['time']
            item_date=change_time_str_to_obj(str_datetime)
            if start_time<=item_date<=end_time:
                
                id=int(item['id'][2:])
                # print(id)

                belt1=item['belt1']
                belt2=item['belt2']
            
                # belt1 value is to be considered 0 when the state is True and
                # belt2 value is to be considered 0 when the state is False.
                    
                if item['state']==True:
                    belt1=0
                if item['state']==False:    
                    belt2=0
                # print(item['state'])
                temp={'id':id,'belt1':belt1,'belt2':belt2}

                all_id_list.append(temp) 

    # 8:{'avg_l1':[],'avg_l2':[]}

    ans={}
    for item in all_id_list:
        id=item['id']
        if id not in ans.keys():
            l1=[item['belt1']]
            l2=[item['belt2']]
            temp={'avg_l1':l1,'avg_l2':l2}
            ans[id]=temp
        else:
            l1=ans[id]['avg_l1']
            l2=ans[id]['avg_l2']
            l1.append(item['belt1'])
            l2.append(item['belt2'])
            temp={'avg_l1':l1,'avg_l2':l2}
            ans[id]=temp


    final_ans=[]
    for key in ans.keys():
        # print(ans[key])
        avg_belt1=sum(ans[key]["avg_l1"])//len(ans[key]["avg_l1"])
        avg_belt2=sum(ans[key]["avg_l2"])//len(ans[key]["avg_l2"])
        # print(key,avg_belt1,avg_belt2)
        temp={"id" : key, "avg_belt1" : avg_belt1, "avg_belt2" : avg_belt2}
        final_ans.append(temp)


    final_ans=sorted(final_ans,key=lambda item: item['id'])


    return final_ans
    
if __name__ == "__main__":
    ans=question_3_solution("2021-01-28T18:30:00Z","2021-01-28T20:10:00Z")
    print(ans)


