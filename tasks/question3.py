
import datetime


  
    
def time_delta(t1, t2):
    time_format="%a %d %b %Y %H:%M:%S %z"
    time1=datetime.datetime.strptime(t1,time_format)
    time2=datetime.datetime.strptime(t2,time_format)
    time_difference = abs(int((time2 - time1).total_seconds()))
    #timed=datetime.timedelta(time1,time2)
    print(time_difference)

if  __name__ == '__main__' :
    t=int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        time_delta(t1,t2) 



  