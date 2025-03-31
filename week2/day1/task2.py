def convertFromMinuteToFunction(minutes, seconds):
 converted_minute =(minutes *60) +seconds

def ConvertToMiles(km):
    return (km *0.621)

def getAverageSpeed(distance, minutes, seconds):
   converted_distance =ConvertToMiles(distance)
   converted_time =convertFromMinuteToFunction(minutes, seconds)

   avg_speed = converted_distance / converted_time

   return avg_speed

result =getAverageSpeed(18,42,42)
print("Average speed in miles per hour: ", result)