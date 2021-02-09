
--------------------------------------------------
To run the site on local system basic requirements
--------------------------------------------------

1->Python3 and pip
2->Any OS
3->minimum 512MB Ram




-----------------------------------
The commands to run the application 
-----------------------------------
CMD# pip install -r requirements.txt

CMD# python application.py

  open the link in your system and for better view in browser install json extension
  


----------------------------------
APIs details
----------------------------------
I define 3 APIs as per assignment
The format to given startdate and enddate should be-
<YYYY>-<MM>-<DD>T<hour>:<minutes>:<seconds>Z
Example-2021-01-28T07:30:00Z

1st API->
 
	API- <baseURL>/question_1/<start_time>/<end_time>	
	
	Example- http://machstatztask-env.eba-iec7rddt.ap-southeast-1.elasticbeanstalk.com/question_1/2021-01-28T07:30:00Z/2021-01-28T13:30:00Z 
	
	Method- HTTP GET



2nd API->
 
	API- <baseURL>/question_2/<start_time>/<end_time>	
	
	Example- http://machstatztask-env.eba-iec7rddt.ap-southeast-1.elasticbeanstalk.com/question_2/2021-01-28T08:30:00Z/2021-01-28T10:30:00Z
	
	Method- HTTP GET



3rd API->
 
	API- <baseURL>/question_3/<start_time>/<end_time>	
	
	Example- http://machstatztask-env.eba-iec7rddt.ap-southeast-1.elasticbeanstalk.com/question_3/2021-01-28T18:30:00Z/2021-01-28T20:10:00Z
	
	Method- HTTP GET

