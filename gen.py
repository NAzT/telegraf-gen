import glob
import os

# import pandas as pd
files = sorted(glob.glob('lifetime/*.conf'))


def get(filename):
    filename = os.path.basename(file).split(".")[0]
    tpl = f'''
  telegraf_{filename}:
    image: telegraf
    volumes:
      - ./{file}:/etc/telegraf/telegraf.conf:ro
    environment:
      - TZ=Asia/Bangkok
    restart: always
    network_mode: "host"
'''
    return tpl


content = ""
for file in files:
    tpl = f'''version: '3.5'
services:'''
    content += get(file)


print(tpl)
print(content)
