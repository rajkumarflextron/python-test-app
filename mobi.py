import flet as ft
from Views.header import Header
from Views.light_control import LightControl
from Views.body import TemperatureControl
from Views.playlist import PlayList
from Views.audio_player import AudioPlayer
from Views.video_widget import VideoController
import os

path="C:\\V1_P_CAST\\audio_files"
path="D:\\Official_2023\\V1_P_CAST\\audio_files"
#path="C:\\V1_P_CAST\\assets"
ls=os.listdir(path)
res=[]
out={}
mediapath_list=[]
for f in ls:
    out[f]=os.path.join(path,f)
    res.append(out)
    mediapath_list.append(out[f])

def main(page:ft.Page):
    count=0
    header=Header()
    page.appbar=ft.AppBar(leading=ft.IconButton(ft.icons.MENU, tooltip="Menu",icon_color=ft.colors.WHITE),
                          bgcolor="#5B2C6F",
                          title=ft.Text("P-CASD",color=ft.colors.WHITE,size="25"),
                          center_title=True)
    page.title="P-CASD"
    page.theme_mode=ft.ThemeMode.DARK
    page.scroll=ft.ScrollMode.AUTO
    body=ft.Row(controls=[ft.Column(controls=[TemperatureControl()]),
        LightControl(),
        PlayList()
        # ft.Column(controls=[PlayList()])
    ],
    alignment=ft.MainAxisAlignment.START)
    # page.add(TemperatureControl())
    # page.add(LightControl())
    page.add(body)


    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()
    def on_complete(_):
        print("entered !!")
        count=0
        for i in mediapath_list:
            count= count+1
            if i == audio1.src:
                break
        if count >= len(mediapath_list):
            count=0
        
        audio1.src=mediapath_list[count]
        audio1.play()
        page.update()


    audio1 = ft.Audio(
        src=mediapath_list[0],
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=on_complete,
    )
    # page.overlay.append(audio1)
    # page.add(
    #     ft.Row([
    #     ft.ElevatedButton("Play", on_click=lambda _: audio1.play()),
    #     ft.ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
    #     ft.ElevatedButton("Resume", on_click=lambda _: audio1.resume()),
    #     ft.ElevatedButton("Release", on_click=lambda _: audio1.release()),
    #     ft.ElevatedButton("Seek 2s", on_click=lambda _: audio1.seek(2000)),
    #     ft.ElevatedButton("Next", on_click=on_complete),
    #     ])
    # )
    # page.add(VideoController())
    
    

ft.app(target=main)