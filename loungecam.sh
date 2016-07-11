#!/bin/bash
raspistill -w 640 -h 480 -a 12 -o loungecam.jpg 
echo "image captured"
sleep 2
scp loungecam.jpg root@192.168.1.181:/var/www/images
echo "image sent"
date
