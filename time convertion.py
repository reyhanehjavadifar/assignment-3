time=int(input('choose:\n1)conerting hour to seconds\n2)converting seconds to hour\nenter the time:'))
if time==1:
        second=int(input('enter time in second:'))
        minute=int(input('enter time in minute:'))
        hour=int(input('enter time in hour:'))
        seconds=(hour*3600)+(minute*60)+second
        print(seconds,'second')
    
if time==2:
        time = int(input("enter time in seconds: "))

        hour = time // 3600
        time1=(time-3600)*hour
        minutes=time1//60
        seconds=time1-60*minutes

        print('hour:',hour,'minutes:',minutes,'seconde:',seconds)
        'break'

