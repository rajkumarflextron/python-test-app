import flet as ft
import os
from Views.video_widget import VideoController
import Views.vp as vp
class PlayList(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.ls=[]
        print(self.ls)
        self.player=vp.Player()
        self.count=0
    
    def highlight(self,index):
        self.view_list[index].bgcolor=ft.colors.GREEN
        self.update()

    def play_click(self,e):
        print("play")
        self.player.current()
    
    def next_click(self,e):
        self.view_list[self.count].color=ft.colors.WHITE
        self.count+=1
        print("next")
        
        
        if self.count>=len(self.view_list):
            self.count=0
        self.view_list[self.count].color=ft.colors.PINK
        self.update()
        self.player.next()
    
    def stop_click(self,e):
        print("stop")
        self.player.stop()

    def previous_click(self,e):
        print("previous")
        self.view_list[self.count].color=ft.colors.WHITE
        self.count-=1
        
        
        
        if self.count<0:
            self.count=len(self.view_list)-1
        self.view_list[self.count].color=ft.colors.PINK
        self.update()
        self.player.previous()

    def build(self):
        self.view_list=[]
        # self.view_list.append(VideoController())
        loc="C:\\V1_P_CAST\\audio_files"
        loc="D:\\Official_2023\\V1_P_CAST\\audio_files"
        for f in os.listdir(loc):
            print(f)
            file_name=f
            file_location=os.path.join(loc,f)
            self.ls.append({file_name:file_location})
            text_widget=ft.Text(value=file_name, color=ft.colors.WHITE)
            self.view_list.append(text_widget)
        self.view_list[self.count].color=ft.colors.PINK
        previous_button=ft.IconButton(icon=ft.icons.SKIP_PREVIOUS,icon_color=ft.colors.RED,on_click=self.previous_click)
        play_button=ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,icon_color=ft.colors.RED,on_click=self.play_click)
        next_button=ft.IconButton(icon=ft.icons.SKIP_NEXT,icon_color=ft.colors.RED,on_click=self.next_click)
        stop_button=ft.IconButton(icon=ft.icons.STOP_CIRCLE_ROUNDED,icon_color=ft.colors.RED,on_click=self.stop_click)
        view=ft.Row(controls=[previous_button,play_button,next_button,stop_button],alignment=ft.MainAxisAlignment.CENTER)

        self.card=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(name=ft.icons.MY_LIBRARY_MUSIC,color=ft.colors.PINK),
                            title=ft.Text("Playlist Control",color=ft.colors.WHITE),
                            
                        ),
                        
                      ft.Column(
                          controls=[view]
                      ),
                      ft.Column(controls=self.view_list)
                    ],
                   scroll=True 
                ),
                height=700,
                
                width=420,
                padding=20,
                bgcolor="#5B2C6F",
                border_radius=10
            )
        )
        return self.card