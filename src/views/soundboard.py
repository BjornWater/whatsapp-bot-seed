from utils.media_sender import UrlPrintSender, AudioFileSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SoundboardView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.audio_file_sender = AudioFileSender(self.interface_layer)
        self.routes = [
            ("^!gratis", self.gratis),
            ("^!wauw", self.wauw),
            ("^!mand", self.mand),
            ("^!rug", self.rug),
            ("^!bier", self.bier),
            ("^!hiep", self.hiep),
            ("^!waar", self.waar),
            ("^!koekkoek", self.koekkoek)

        ]

    def gratis(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/gratis.wav")

    def wauw(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/wauw.mp3")

    def mand(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/mand.mp3")

    def rug(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/rug.mp3")

    def bier(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/bier.mp3")

    def hiep(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/hiep.mp3")

    def waar(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/babylon.mp3")

    def koekkoek(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/bjorn/whatsapp-bot-seed/src/views/sound/babylon.mp3")
