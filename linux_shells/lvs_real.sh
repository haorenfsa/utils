#!/usr/local/bin/bash 
#description : start realserver 
# this is for centos
VIP=61.135.20.16 
case "$1" in 
start) 
echo " start LVS of REALServer" 
/sbin/ifconfig lo0 $VIP    netmask 255.255.255.255 al
ias -arp up 
;; 
stop) 
/sbin/ifconfig lo0 alias down 
echo "close LVS Directorserver" 
/sbin/ifconfig lo0 127.0.0.1 arp up 
;; 
*) 
echo "Usage: $0 {start|stop}" 
exit 1 
esac 