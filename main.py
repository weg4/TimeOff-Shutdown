import datetime 
import os
import time

def welcome():
    print("                  Welcome in TimeOff!\nThis application helps you quickly configure your PC's shutdown.")
    print("What do you need?\n1.Schedule pc shutdown 2.Disable shutdown ")
    while True:
        try:
            setting = int(input())
            if setting == 1:
                hour, minute = get_shutdown_time()
                schedule_shutdown(hour, minute)
                break
            elif setting == 2:
                print("GoodBye")
                os.system("shutdown /a")
                time.sleep(0.5)
                break
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input:( Plesae enter a number.")
            
            

def get_shutdown_time():
    while True:
        try:
            hour = int(input("Hour (0-23): "))
            if hour >= 23 or hour < 0:
                print("Invalid hour. Please enter a value between 0 and 23.")
                continue
            minute = int(input("Minute (0-60): "))
            if minute >= 60 or minute < 0:
                print("Invalid hour. Please enter a value between 0 and 60.")
                continue
            return hour, minute
        except ValueError:
            print("Invalid input:( Plesae enter a number.")

def schedule_shutdown(hour, minute):
    current_datetime = datetime.datetime.now()
    time_delta = datetime.timedelta(hours=hour, minutes=minute)
    shutdown_time = current_datetime + time_delta
    print(f"Your PC will shut down at {shutdown_time.strftime('%H:%M')}.\nIs this correct? (y/n)")
    while True:
        setting = input().lower()
        if setting == "y":
            seconds = (hour * 3600) + (minute * 60)
            os.system(f"shutdown /s /t {seconds}")
            print("Goodbye!")
            time.sleep(0.5)
            break
        elif setting == "n":
            print("Okey, restarting...")
            hour, minute = get_shutdown_time()
            schedule_shutdown(hour, minute)
        else:
            print("Please enter 'y' or 'n'.")
            

if __name__== "__main__":
    welcome()