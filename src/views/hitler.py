from utils.media_sender import UrlPrintSender, AudioFileSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class HitlerView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.audio_file_sender = AudioFileSender(self.interface_layer)
        self.routes = [
            ("^!heil", self.heil),
            ("^!sieg", self.sieg),
            ("^!jaofnee", self.jaofnee)
        ]

    def heil(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("HITLER!!!", to=message.getFrom())
    def sieg(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("HEIL!!!", to=message.getFrom())
    def jaofnee(self, message=None, match=None, to=None):
        num = random.randint(1, 10)
        if (num % 2):
            self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/jawohl.mp3")
        else:
            self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/nein.wav")
