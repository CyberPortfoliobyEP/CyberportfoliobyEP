import os
for ip in range(1, 255):
    response = os.system('ping -c 1 10.10.1.' + str(ip) + ' > /dev/null 2>&1')
    if response == 0:
        print('10.10.1.' + str(ip) + ' is up')
