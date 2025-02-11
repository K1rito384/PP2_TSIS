from datetime import datetime

current_datetime = datetime.now().replace(microsecond=0)
print("Current datetime without microseconds:", current_datetime)
