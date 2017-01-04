from __future__ import unicode_literals

from django.db import models
from mongoengine import *
# mongoengin 是mongo的ORM
# from mongoengine import connect
# connect('wbsit', host='127.0.0.1', port=27017)

class ArtiInfo(Document):
    des = StringField()
    title = StringField()
    scores = StringField()
    tags = ListField(StringField())
    meta = {'collection': 'arti_info3'}

# for i in ArtiInfo.objects[:1]:
#     print(i.title,i.des,i.tags)