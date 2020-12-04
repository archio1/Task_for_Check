#2)	Зробити на пітоні код який буде виводити всі рядки лога де буде зустрічатись Android 10 використовуючи regex.
# Дивись прикріплений лог api.parkingwatcher.com.access.log

import re

with open('Resources/api.parkingwatcher.com.access.log', 'r') as f: # уточнить про открытияе файла?? проверки файла?
    logfile = set(f.read().splitlines())
data = []

for line in logfile:
        result = re.findall(r"^(.+Android 10.+)\"$", line)
        if result != []:
            print(result)




#print([int(i) for i in result if int(i) > 999999999])





