"""
@summary: Module containing poller class
"""
from googlevoice import Voice

class Poller(object):
   """
   @summary: Polls Google Voice looking for new texts
   """
   
   def __init__(self):
      self.voice = Voice()
      self.voice.login()
      
   def poll(self):
      numbers = []
      inBox = self.voice.sms()
      for msg in inBox.messages:
         if not msg.isRead:
            numbers.append(msg.phoneNumber)
            msg.mark(read=1)
      return numbers
   

