from google.appengine.ext import ndb


class memeInfo (ndb.Model):
    memeTextTop = ndb.StringProperty(required=True)
    memeUrl = ndb.StringProperty(required=True)
    memeTextBottom = ndb.StringProperty(required=True)



'''
.ORDER(memeInfo.memeTextTop) #orders alphabetical orders
'''
