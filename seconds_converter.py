""" 
convert time inputed in seconds to format:
"__ years, __ days, __ hours, __ minutes and __ seconds"
1 year = 365 days
"""

def format_duration(time):
    if time == 0:
        return "now"
        
    year = time//(365*24*3600)
    day = (time - year*(365*24*3600))//(24*3600)
    hour = ((time - year*(365*24*3600)) - day*(24*3600))//3600
    mins = (((time - year*(365*24*3600)) - day*(24*3600)) - hour*3600)//60
    sec = (((time - year*(365*24*3600)) - day*(24*3600)) - hour*3600) - mins*60
    
    if year == 1:
        y = " year"
    else:
        y = " years"
    if day == 1:
        d = " day"
    else:
        d = " days"
    if hour == 1:
        h = " hour"
    else:
        h = " hours"
    if mins == 1:
        m = " minute"
    else:
        m = " minutes"
    if sec == 1:
        s = " second"
    else:
        s = " seconds"
    
    arr = [year, day, hour, mins, sec]
    arr1 = [y, d, h, m, s]
    answer = []
    for i in range(5):
        if arr[i] != 0:
            answer.append(str(arr[i]) + arr1[i])
    
    if len(answer) == 1:
        return "".join(answer)
    elif len(answer) == 2:
        return " and ".join(answer)
    else:
        return ", ".join(answer[:-1]) + " and " + str(answer[-1])
