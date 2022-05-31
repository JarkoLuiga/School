import psutil
import shutil
import os
import requests
from datetime import datetime

def to_gb(n):
    return n / (1024 ** 3)

def to_gb_round(n):
    return round(n / (1024 ** 3))

def percent(n, pct):
    return (n / 100) * pct

warn = 20 # hoiatusteave protsent

working_dir = os.getcwd()

logfile = open("log.txt", "w")

date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

logfile.write("Programmi kaivitamise aeg: {} \n".format(date))

free_memory = psutil.virtual_memory().percent
print("Vaba malu on {}% ja kokku on {} GB.".format(
    free_memory, to_gb_round(psutil.virtual_memory().total)
))

logfile.write("Vaba malu protsent: {}% \n".format(free_memory))

total_space = to_gb_round(shutil.disk_usage(working_dir).total)
free_space = to_gb_round(shutil.disk_usage(working_dir).free)
print("Vaba salvestusruumi on {} GB ja kokku on salvestusruumi {} GB.".format(
    free_space, total_space
))

free_space_percent = round((shutil.disk_usage(working_dir).free / shutil.disk_usage(working_dir).total) * 100, 1)
logfile.write("Vaba salvestusruumi protsent: {}% \n".format(free_space_percent))

if free_memory > warn:
    text = "Vaba malu on ule {}%.".format(warn)
    print(text)
    logfile.write("{}\n".format(text))

if to_gb(shutil.disk_usage(working_dir).free) > percent(to_gb(shutil.disk_usage(working_dir).total), warn):
    text = "Salvestusruum on ule {}%.".format(warn)
    print(text)
    logfile.write("{}\n".format(text))

json = requests.get("https://goweather.herokuapp.com/weather/tallinn").json()
logfile.write("\n")
logfile.write("Tallinna ilm:\n")
logfile.write("Temperatuur: {}\n".format(json["temperature"]))
logfile.write("Tuule kiirus: {}".format(json["wind"]))


logfile.close()
