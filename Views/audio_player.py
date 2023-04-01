import flet as ft

class AudioPlayer(ft.UserControl):
    def volume_down(_):
        self.audio1.volume -= 0.1
        self.audio1.update()

    def volume_up(_):
        self.audio1.volume += 0.1
        self.audio1.update()

    def balance_left(_):
        self.audio1.balance -= 0.1
        self.audio1.update()

    def balance_right(_):
        self.audio1.balance += 0.1
        self.audio1.update()

    def build(self):
        self.audio1 = ft.Container(ft.Audio(
            src="C:\V1_P_CAST\assets\aaa.mp3", autoplay=False,
            on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
        ),
        width=500,
        height=500)
        return self.audio1
