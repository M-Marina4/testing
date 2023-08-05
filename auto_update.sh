#!/bin/sh
sudo apt update
sudo apt upgrade -y
#ifndef update.txt
        touch /home/climatenet/Desktop/update.txt
printf >> "/home/climatenet/Desktop/update.txt" "Update is done\n"
