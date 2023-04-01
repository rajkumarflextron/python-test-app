import ctypes
import io
import pdb
import sys
import time
import os
import vlc
from mutagen.mp3 import MP3

loc="C:\\NIMHANS_PCASD\\AV_FILES"
loc="D:\\Official_2023\\V1_P_CAST\\audio_files"
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
current_song=play_location[count]
MediaOpenCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
MediaReadCb = ctypes.CFUNCTYPE(ctypes.c_ssize_t, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_size_t)
MediaSeekCb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint64)
MediaCloseCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)


def media_open_cb(opaque, data_pointer, size_pointer):
    data_pointer.contents.value = opaque
    size_pointer.contents.value = sys.maxsize
    return 0


def media_read_cb(opaque, buffer, length):
    stream=ctypes.cast(opaque,ctypes.POINTER(ctypes.py_object)).contents.value
    new_data = stream.read(length)
    for i in range(len(new_data)):
        buffer[i]=new_data[i]
    return len(new_data)


def media_seek_cb(opaque, offset):
    stream=ctypes.cast(opaque,ctypes.POINTER(ctypes.py_object)).contents.value
    stream.seek(offset)
    return 0


def media_close_cb(opaque):
    stream=ctypes.cast(opaque,ctypes.POINTER(ctypes.py_object)).contents.value
    stream.close()


callbacks = {
    'open': MediaOpenCb(media_open_cb),
    'read': MediaReadCb(media_read_cb),
    'seek': MediaSeekCb(media_seek_cb),
    'close': MediaCloseCb(media_close_cb)
}


class Player():
    def __init__(self,) -> None:
        self.count=0
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.load()

    def get_current_song(self):
        print(play_location[self.count])
        return play_location[self.count]

    def load(self):
        stream=open(play_location[self.count], 'rb')
        current_song=play_location[self.count]
        media = self.instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(ctypes.pointer(ctypes.py_object(stream)), ctypes.c_void_p))
        self.player.set_media(media)
    
    def current(self):
        print("entered play vlc!!")
        self.load()
        self.player.play()
        
        if str(play_location[self.count]).endswith(".mp3"):
            audio = MP3(play_location[self.count])
            value=int(audio.info.length)
        else:
            value = self.player.get_length()
            value=int(round(value)/1000)
        time.sleep(2)
        # value = self.player.get_length()
        # value=int(round(value)/1000)
        print(value)
        time.sleep(value-2)
        self.player.stop()
        #self.count+=1
        #self.current()
        

    def stop(self):
        self.player.stop()
    
    def next(self):
        self.stop()
        
        self.count+=1
        print("count : ",self.count)
        if self.count >= len(play_location):
            self.count=0
        self.load()
        self.current()    
        time.sleep(1)

    def previous(self):
        self.stop()
        
        self.count-=1
        print("count : ",self.count)
        if self.count < 0:
            self.count=len(play_location)-1
        self.load()
        self.current()    
        time.sleep(1)  

def main():
    stream = open(play_location[0], 'rb')
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new_callbacks(callbacks['open'], callbacks['read'], callbacks['seek'], callbacks['close'], ctypes.cast(ctypes.pointer(ctypes.py_object(stream)), ctypes.c_void_p))
    player.set_media(media)
    player.play()
    time.sleep(5)

    value = player.get_length()
    value=int(round(value)/1000)
    print(value)
    player.pause()
    time.sleep(2)
    player.play()
    time.sleep(2)
    #time.sleep(value-2)
    player.stop()
#main()

# ss=Player()
# pdb.set_trace()