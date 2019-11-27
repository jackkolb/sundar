#!/bin/sh
# scans the network for raspberry pis

IP_LOW=$1
IP_HIGH=$2

for ip in $(seq $IP_LOW $IP_HIGH); do
  echo 10.28.${ip}.0/24
  nmap -sP 10.28.${ip}.0/24 | grep 'ucr.edu'
done
