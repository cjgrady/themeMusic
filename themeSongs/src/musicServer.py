"""
@summary: Module containing music server class.
"""
from pylms.server import Server
from pylms.player import Player

SERVER = "192.168.1.3"

class MusicServer(object):
   """
   @summary: Music server class that provides function to interrupt with new song
   """

   def __init__(self):
      self.server = Server(hostname=SERVER, port=9090)
      self.server.connect()
   
   def interrupt(self, filename):
      players = self.server.get_players()
      for player in players:
         player.playlist_play(filename)
         