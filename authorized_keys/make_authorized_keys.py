#!/usr/bin/env python
import os
DEST_DIR = '/Users/arobel/repos/ansible-aiml/authorized_keys'

authorized_keys = ""
for filename in os.listdir(DEST_DIR):
    if not ".txt" in filename:
        continue
    with open(f"{DEST_DIR}/{filename}", 'r') as f:
        for line in f.readlines():
            authorized_keys += line
with open(f'{DEST_DIR}/authorized_keys', 'w') as f:
    f.write(authorized_keys)