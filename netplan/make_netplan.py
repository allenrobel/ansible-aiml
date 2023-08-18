#!/usr/bin/env python
DEST_DIR = '/Users/arobel/repos/ansible-aiml/netplan'

def make_netplan(host):
    return f"""
# This is the network config written by 'subiquity'
network:
    version: 2
    ethernets:
        eno1:
            critical: true
            dhcp-identifier: mac
            dhcp4: true
            nameservers:
                addresses:
                -   171.70.168.183
        eno2:
            dhcp4: true
        ens1f0np0:
            dhcp4: false
        ens1f1np1:
            dhcp4: false
    vlans:
        vlan{host}:
            id: {host}
            link: ens1f0np0
            addresses:
            -   192.168.{host}.11/24
            routes:
            -   to: 192.168.0.0/16
                via: 192.168.{host}.1
                metric: 100
        vlan{host+100}:
            id: {host+100}
            link: ens1f1np1
            addresses:
            -   172.16.{host}.11/24
            routes:
            -   to: 172.16.0.0/16
                via: 172.16.{host}.1
                metric: 100
"""
for host in range(101,149):
    with open(f'{DEST_DIR}/{host}.00-installer-config.yaml', 'w') as f:
        f.write(make_netplan(host))
