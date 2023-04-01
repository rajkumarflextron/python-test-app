# importing the vlc module  
import vlc
import os 
import pdb
import time
import pygame

path="..\\assets"
#path="C:\\V1_P_CAST\\assets"
ls=os.listdir(path)
res=[]
out={}
mediapath_list=[]
for f in ls:
    out[f]=os.path.join(path,f)
    res.append(out)
    mediapath_list.append(out[f])
vlc.MediaPlayer(ls[0])
file=ls[0]
print(file)
# creating the vlc media player object  
my_media = vlc.MediaPlayer(res[0][file])  
time.sleep(1)  
# playing video  
my_media.play() 
time.sleep(5)
my_media.stop() 


def plays():
    Instance = vlc.Instance('--loop')

    medialist = Instance.media_list_new()
    
    print(mediapath_list)

    for pl_list in mediapath_list :
        print(pl_list)
        medialist.add_media(Instance.media_new(pl_list))

    # print(medialist)
    # medialist.add_media('./Audio_Video_File.mp4')
    
    listPlayer = Instance.media_list_player_new()
    listPlayer.set_media_list(medialist)
    listPlayer.play()
    time.sleep(10)

