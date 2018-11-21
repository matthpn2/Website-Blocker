import time 
from datetime import datetime as dt

# store hosts file path, IP address to redirect browser and list of websites to be blocked
hostsPath = r"/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com"]

while True:
    currentDT = dt.now()

    # check if the current time is within the working hours of 8AM to 5PM
    if dt(currentDT.year, currentDT.month, currentDT.day, 8) < currentDT < dt(currentDT.year, currentDT.month, currentDT.day, 17):
        print("Working hours...")

        # open host file in read and append method
        with open(hostsPath, "r+") as file:
            content = file.read()

            #if website is in host file, don't do anything. otherwise, add it to the host file
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    # if current time is out of working hours window, check and remove websites from host file
    else:
        # open host file in read and append method
        with open(hostsPath, "r+") as file:
            # store lines in content list and seek beginning of file
            content = file.readlines()
            file.seek(0)

            # check if any websites are not the content line and write that line
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)

            # trunate everything below rewritten lines
            file.truncate()

        print("Sleeping hours...")

    # sleep for 5 minutes before continuing the while loop
    time.sleep(300)