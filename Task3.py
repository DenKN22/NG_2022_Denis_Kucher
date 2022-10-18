from datetime import datetime
seconds = int(input("Write count of seconds"))
date = datetime.fromtimestamp(seconds)
print(date)

