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

def make_hosts_all():
    hosts = f"""
all:
    children:"""
    return hosts

def make_hosts_ubuntu():
    hosts = f"""
        ubuntu:
            hosts:"""
    for host in range(1,49):
        hosts += f"""
                u{host+100}:
                    host_id: {host}
                    ansible_host: 172.26.251.{host+100}"""
    return hosts
def make_hosts_test_ubuntu():
    hosts = f"""
        ubuntu_test:
            hosts:"""
    for host in range(40,42):
        hosts += f"""
                u{host+100}:
                    host_id: {host}
                    ansible_host: 172.26.251.{host+100}"""
    return hosts

hosts = make_hosts_all() + make_hosts_ubuntu() + make_hosts_test_ubuntu()
print(hosts)