import time

def countdown_timer(seconds):
    """Counts down from the specified number of seconds to zero."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02}:{secs:02}'
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("00:00\nTime's up!")

seconds = input("Enter the time in seconds: ")

countdown_timer(int(seconds))