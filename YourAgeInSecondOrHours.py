yourAge = int(input("Input your age --> "))
hourOrSec = input("Do you want to know how many seconds you live or how many hours? (print seconds or minuts) --> ")
if hourOrSec == "seconds":
    print(f"Your age in seconds - {yourAge*365*24*60*60}")
else:
    print(f"Your age in minuts - {yourAge*365*24}")
