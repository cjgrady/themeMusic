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

songs = {
         "+17859798181" : "C:\\Users\\CJ\\Music\\iTunes\\iTunes Media\\Music\\Vanilla Ice\\To the Extreme\\01 Ice Ice Baby.m4a",
         "+17853934228" : "C:\\Users\\CJ\\Music\\iTunes\\iTunes Media\\Music\\Waka Flocka Flame\\No Hands (feat. Roscoe Dash & Wale) - Si\\01 No Hands (feat. Roscoe Dash & Wal.m4a",
        }

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
            if songs.has_key(i):
               song = songs[i]
            else:
               song = fn
            s.interrupt(song)
         print "wait"
         time.sleep(30)
         continue
   except Exception, e:
      print str(e)
