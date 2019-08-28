#!/usr/bin/python

import os
import random

strToSearch="Deployment Group: Production, Server Number: 10"
strToReplace="Deployment Group: " + os.environ['DEPLOYMENT_GROUP_NAME'] + ", Server Number: " + str(random.randrange(10))

fp=open("/var/www/html/index.html","r")
buffer=fp.read()
fp.close()

fp=open("/var/www/html/index.html","w")
fp.write(buffer.replace(strToSearch,strToReplace))
fp.close()
