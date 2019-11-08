#!/usr/bin/env bash
# the script deploys the web_static to web server
apt-get update
apt-get install -y nginx
ufw allow "nginx HTTP"
if [ ! -d "/data/web_static/releases/test/" ]
then
    mkdir -p /data/web_static/releases/test/
fi
if [ ! -d "/data/web_static/shared/" ]
then
    mkdir /data/web_static/shared/
fi
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a\location /bh_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default
service nginx restart
