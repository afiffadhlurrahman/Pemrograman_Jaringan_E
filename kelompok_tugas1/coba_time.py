import time

named_tuple = time.localtime()
time_string = time.strftime("%H:%M", named_tuple)

print(time_string)
