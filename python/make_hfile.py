#!/usr/bin/env python
from os import environ
DEST_DIR = f"{environ['HOME']}repos/ansible-aiml/hfile"

hfile = ""
for host in range(101,149):
    hfile += f"192.168.{host}.11\n"
with open(f'{DEST_DIR}/hfile', 'w') as f:
    f.write(hfile)
