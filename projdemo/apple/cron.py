def my_scheduled_job():
    # pass

    print('---Hello-cron-job---')
    
    # file1 = open("demo_2.txt", "w")  
    # file1.write('Hello')
    # file1.close() 
    
    with open("demo_2.txt", "a") as f:
        f.write("started")


# my_scheduled_job()