from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
          #  ("^/help", self.help),
            ("^!roll", self.roll)
        ]

 
    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 100), to=message.getFrom())

  #  def even_or_odd(self, message=None, match=None, to=None):
   #     is_odd = len(match.group("evenOrOdd")) % 2
   ##     num = random.randint(1, 10)
   #     if (is_odd and num % 2) or (not is_odd and not num % 2):
    #        return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
    #    else:
     #       return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())

  #  def help(self, message=None, match=None, to=None):
   #     return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())
