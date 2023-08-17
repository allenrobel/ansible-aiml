#!/usr/bin/env python
"""
all:
    children:
        ubuntu:
            hosts:
                u140:
                    host_id: 40
                    ansible_host: 172.26.251.140
"""

def make_hosts():
    hosts = f"""
all:
    children:
        ubuntu:
            hosts:"""
    for host in range(1,49):
        hosts += f"""
                u{host+100}:
                    host_id: {host}
                    ansible_host: 172.26.251.{host+100}"""
    return hosts

print(make_hosts())