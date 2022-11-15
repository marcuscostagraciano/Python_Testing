import datetime
import os
from csv import writer
from getTemperature import getTemp

folderPathing = "C:\\Users\\user\\Desktop"
os.chdir(folderPathing)

filesPathing = "Daily_temp"
if (not os.path.exists(filesPathing)):
    os.makedirs(filesPathing)

os.chdir(filesPathing)
currentDay = datetime.date.today().isoformat()
if (not os.path.exists(currentDay)):
    os.makedirs(currentDay)

csvName = "temperatures.csv"
os.chdir(currentDay)
if (not os.path.isfile(csvName)):
    csv_header = ["hours", "temperature"]
    with open(csvName, 'w', encoding="UTF8") as file:
        writer(file).writerow(csv_header)

now = datetime.datetime.now()
currentInfo = [now.hour, getTemp()]

with open(csvName, 'a') as file:
    writer(file, lineterminator="\n").writerow(currentInfo)

if (now.hour == 23):
    import pandas as pd
    from matplotlib import pyplot as plt

    csvDataset = pd.read_csv(csvName)
    hours = csvDataset["hours"]
    temps = csvDataset["temperature"]

    plt.plot(hours, temps, marker="o", ls="--")

    plt.title("Temperature per hour")
    plt.xlabel("Hours")
    plt.ylabel("Temperatures")
    plt.grid()

    plt.savefig("temps.png")
