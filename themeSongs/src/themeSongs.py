"""
@summary: Main module for theme (entry) music.  Sits and waits for signals.
@author: CJ Grady
@version: 1.0
@status: alpha
"""
import time

from musicServer import MusicServer
from poller import Poller

fn = "C:\\Users\\CJ\\Music\\iTunes\\iTunes Media\\Music\\Vanilla Ice\\To the Extreme\\01 Ice Ice Baby.m4a"

if __name__ == '__main__':
   # While not killed
   # Poll texts
   # Once one has been found
   #  pause music
   #  queue up theme song
   s = MusicServer()
   p = Poller()
#   s.interrupt(fn)
   try:
      while True:
         for i in p.poll():
            s.interrupt(fn)
         print "wait"
         time.sleep(30)
         continue
   except Exception, e:
      print str(e)
