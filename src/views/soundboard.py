from utils.media_sender import UrlPrintSender, AudioFileSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SoundboardView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.audio_file_sender = AudioFileSender(self.interface_layer)
        self.routes = [
            ("^.*gratis.*$", self.gratis),
            ("^.*wauw.*$", self.wauw),
            ("^.* mand.*$", self.mand),
            ("^.*rug.*$", self.rug),
            ("^!bier", self.bier),
            ("^!hiep", self.hiep),
            ("^!waar", self.waar),
            ("^!koekkoek", self.koekkoek),
            ("^!nooduitgang", self.nooduitgang),
            ("^!russia", self.russia),
            ("^!efteling", self.efteling),
            ("^.*octo.*$", self.octo)
        ]

    def gratis(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/gratis.wav")

    def wauw(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/wauw.mp3")

    def mand(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/mand.mp3")

    def rug(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/rug.mp3")

    def bier(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/bier.mp3")

    def hiep(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/hiep.mp3")

    def waar(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/babylon.mp3")

    def koekkoek(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/koekkoek.mp3")

    def nooduitgang(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/nooduitgang.mp3")

    def russia(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/russia.mp3")

    def efteling(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/efteling.mp3")

    def octo(self, message=None, match=None, to=None):
        self.audio_file_sender.send(jid=message.getFrom(), text="/home/whatsapp/src/views/sound/octo.mp3")