# time=5
# # print(input("Enter the time"))
# if(time >= 6 or time < 12):
#     print("Good Morining")
# elif(time == 12):
#     print("Good Afternooned")
# elif(time >= 1 or time <=4):
#     print("Good Afternoon")
# else:
#     print("Good Night")

import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

timestampHour = int(time.strftime("%H"))
print(timestampHour)

timestampMin = int(time.strftime("%M"))
print(timestampMin)

timestampSec = int(time.strftime("%S"))
print(timestampSec)

if timestampHour >=5 and timestampHour < 12:
    print("Good Morning")
elif timestampHour == 9:
    print("Special Day")
elif timestampHour >= 1 and timestampHour <= 18:
    print("Good Afternoon")
else :
    print("Good Night")
