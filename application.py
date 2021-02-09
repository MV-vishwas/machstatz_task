from flask import Flask,jsonify
from Q_1 import question_1_solution
from Q_2 import question_2_solution
from Q_3 import question_3_solution



app = Flask(__name__) 


def check_datetime(string):
    from re import search
    regex='^[0-2][0-9][0-9][0-9]-[0-1][0-9]-[0-9][0-9]T[0-2][0-9]:[0-6][0-9]:[0-6][0-9]Z'
    if(search(regex,string)):  
        return True  
    else:  
        return False


@app.route('/') 
def home():
    response=jsonify({'message':'you can use above APIs and in place of start and end datetime you can put your own datetime in format(<YYYY>-<MM>-<DD>T<hour>:<minutes>:<seconds>Z)','APIs':
    {'/question_1/<start_time>/<end_time>':'/question_1/2021-01-28T07:30:00Z/2021-01-28T13:30:00Z','/question_2/<start_time>/<end_time>':'/question_2/2021-01-28T08:30:00Z/2021-01-28T10:30:00Z','/question_3/<start_time>/<end_time>':'/question_3/2021-01-28T18:30:00Z/2021-01-28T20:10:00Z'}}),200
    return response

@app.route('/question_1/<string:start_time>/<string:end_time>') 
def question_1(start_time,end_time):
    if check_datetime(start_time) and check_datetime(end_time):
        response=question_1_solution(start_time,end_time)
        response={"response":response}
        return response,200
    else:
        return jsonify({'response':'Invalid Datetime'}),400
    # return 'question_1'

@app.route('/question_2/<string:start_time>/<string:end_time>') 
def question_2(start_time,end_time):
    if check_datetime(start_time) and check_datetime(end_time):
        response=question_2_solution(start_time,end_time)
        response={"response":response}
        return response,200
    else:
        return jsonify({'response':'Invalid Datetime'}),400
    return 'question_2'

@app.route('/question_3/<string:start_time>/<string:end_time>') 
def question_3(start_time,end_time):
    if check_datetime(start_time) and check_datetime(end_time):
        response=question_3_solution(start_time,end_time)
        response={'response':response}
        return response,200
    else:
        return jsonify({'response':'Invalid Datetime'}),400
    return 'question_3'



if __name__ =='__main__':  
    app.run(debug = True)  

