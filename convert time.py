second= 3620
time=int(input('choose:\n1)conerting hour to seconds\n2)converting seconds to hour\nenter the time:'))
if time==1:
        second=int(input('enter time in second:'))
        minute=int(input('enter time in minute:'))
        hour=int(input('enter time in hour:'))
        seconds=(hour*3600)+(minute*60)+second
        print(seconds,'second')
        

if time==2:
        second=int(input('enter time in second:'))
        minute=int(input('enter time in minute:'))
        hour=int(input('enter time in hour:'))
        hours= (second // 3600)+(minute// 60)+ hour
        

        print('hour:',hour,'minutes:',minute,'second:',second)
        'break'
