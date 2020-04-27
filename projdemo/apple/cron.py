from apple.models import DemoA
from datetime import datetime, timedelta


def my_scheduled_job():
    # pass

    print('---Hello-cron-job---')
    
    # file1 = open("demo_2.txt", "w")  
    # file1.write('Hello')
    # file1.close() 
    
    with open("demo_2.txt", "a") as f:
        f.write("started")

    session_expire = int(datetime.timestamp(datetime.now()+timedelta(days=1)))
    # session_expire = int(1234)
    val1, val2 = DemoA.objects.create(name='Aakash', expire_timestamp=session_expire)
    print('---val1---', val1)
    print('---val2---', val2)


# my_scheduled_job()