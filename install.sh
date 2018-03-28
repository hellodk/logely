#/bin/bash

yum install -y epel-release python-pip
pip install --upgrade pip
pip install requests envoy
mkdir /var/log/logely
touch /var/log/logely/logely.log