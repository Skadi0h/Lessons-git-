import time  # fromAI

seconds = int(input("Write, how long will be your timer: "))


def timer(seconds):
    while seconds > 0:
        print(seconds, "seconds is left")
        time.sleep(1)  # fromAI
        seconds -= 1
    print("Time is over!")


timer(seconds)

# 10/12 cc. A
