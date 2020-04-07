#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<html><head>Hi Im Andres </head></html>" >> /data/web_static/releases/test/index.html
ln -fs /data/web_static/current/ /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu/data

sudo sed -i "/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
sudo ufw allow "Nginx HTTP"
sudo service nginx restart
exit 0
