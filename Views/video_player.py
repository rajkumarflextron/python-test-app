# importing vlc module
import math
import pdb
import vlc

# importing time module
import time
import os

import sys,ctypes
from PyQt5 import QtCore, QtWidgets


loc="C:\\NIMHANS_PCASD\\AV_FILES"
media_list=[]
play_location=[]
for f in os.listdir(loc):
    file_name=f
    file_location=os.path.join(loc,f)
    print(file_name)
    media_list.append({file_name:file_location})
    play_location.append(file_location)
print(media_list)
count=0


class VLCPlayer(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__()
        self._player = vlc.Instance().media_player_new()

    @staticmethod
    @vlc.CallbackDecorators.MediaOpenCb
    def _open_cb(voidptr, data, size):
        data.contents.value = voidptr
        size.value = sys.maxsize
        return 0

    @staticmethod
    @vlc.CallbackDecorators.MediaReadCb
    def _read_cb(voidptr, buffer, length):
        stream = ctypes.cast(
            voidptr, ctypes.POINTER(ctypes.py_object)).contents.value
        data = stream.read(length)
        for index, char in enumerate(data):
            buffer[index] = char
        return len(data)

    @staticmethod
    @vlc.CallbackDecorators.MediaSeekCb
    def _seek_cb(voidptr, offset):
        stream = ctypes.cast(
            voidptr, ctypes.POINTER(ctypes.py_object)).contents.value
        stream.seek(offset)
        return 0

    @staticmethod
    @vlc.CallbackDecorators.MediaCloseCb
    def _close_cb(voidptr):
        stream = ctypes.cast(
            voidptr, ctypes.POINTER(ctypes.py_object)).contents.value
        stream.close()

    def play(self):
        self._player.play()

    def stop(self):
        self._player.stop()

    def load(self, stream):
        # file = QtCore.QFile(path)
        # file.open(QtCore.QIODevice.ReadOnly)
        voidptr = ctypes.cast(ctypes.pointer(
            ctypes.py_object(stream)), ctypes.c_void_p)
        self._player.set_media(vlc.Instance().media_new_callbacks(
            self._open_cb, self._read_cb,
            self._seek_cb, self._close_cb, voidptr))


class VideoPlayList():
    def __init__(self) -> None:
        self.count=0
        #self.media = vlc.MediaPlayer(play_location[count])
        self.media = VLCPlayer(self)
        time.sleep(1)
    def play(self):
        stream=open(play_location[count],"rb")
        
        self.media.load(stream)
        time.sleep(1)
        self.media.play()
        # time.sleep(2)
        #     # getting length of the current media
        # value = self.media.get_length()
        # value=int(round(value))
        # print(value)
        # time.sleep(value-2)
        # self.media.stop()
        
    def next(self):
        self.count+=1
        if self.count < len(play_location):
            self.media = vlc.MediaPlayer(play_location[count])
            time.sleep(1)
            self.play() 
        else:
            self.media = vlc.MediaPlayer(play_location[0])
            time.sleep(1)
            self.play()

    def stop(self):
        self.media.stop()
    
ss=VideoPlayList()
ss.play()
# #ss.next()
# pdb.set_trace()