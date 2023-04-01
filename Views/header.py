import flet as ft

class Header(ft.UserControl):
    def build(self):
        self.header=ft.Container(
            
            content=ft.Row(
                alignment="spaceBetween",
                controls=[
                    ft.Row(controls=[ft.IconButton(
                        icon=ft.icons.MENU,
                        icon_color=ft.colors.WHITE
                    ),ft.Text(value="PSG",color=ft.colors.WHITE)]),
                    ft.Row(controls=[ft.IconButton(
                        icon=ft.icons.NOTIFICATIONS,
                        icon_color=ft.colors.WHITE
                    ),
                      ft.Stack(
            [
                ft.IconButton(
                    icon=ft.icons.PERSON,
                        icon_color=ft.colors.WHITE
                ),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                    alignment=ft.alignment.top_right,
                ),
            ],
            width=40,
            height=40,
        )
         ]),
                ]
            ),
            bgcolor="#5B2C6F"
        )
        return self.header