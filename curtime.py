import datetime

# Get the current date and time
curr_dt = datetime.datetime.now()

# Format the current date and time with "/"
fr_dt = curr_dt.strftime("log.%Y.%m.%d.%H.%M.%S.txt")

#print(fr_dt)