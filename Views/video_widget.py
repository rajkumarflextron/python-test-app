import flet as ft
import Views.vp as vp

class VideoController(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.player=vp.Player()

    def play_click(self,e):
        print("play")
        self.player.current()
    
    def next_click(self,e):
        print("next")
        self.player.next()
    
    def stop_click(self,e):
        print("stop")
        self.player.stop()
    


    def build(self):
        play_button=ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,icon_color=ft.colors.RED,on_click=self.play_click)
        next_button=ft.IconButton(icon=ft.icons.SKIP_NEXT,icon_color=ft.colors.RED,on_click=self.next_click)
        stop_button=ft.IconButton(icon=ft.icons.STOP_CIRCLE_ROUNDED,icon_color=ft.colors.RED,on_click=self.stop_click)
        view=ft.Row(controls=[play_button,next_button,stop_button],alignment=ft.MainAxisAlignment.END)
        return view