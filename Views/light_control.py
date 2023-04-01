import flet as ft
from Views.body import Slider
import serial
import vlc
import time


class LightControl(ft.UserControl):
    def send(self,data):
        ser = serial.Serial('COM3',9600,timeout=0.05)
        if not ser.isOpen():
            ser.open()
        ser.write(data.encode())
        ser.write("\r\n".encode())
        ser.close()
        self.update()

    
    def submit_action(self,e):
        lc_code=""
        if self.timer_options.value=="0":
            lc_code="LC0"
            print(f"{lc_code}")
            self.serial_code.value= lc_code
        else:
            lc_code="LC1"
            self.serial_code.value= lc_code 
            
        for i in self.slider_content.controls:
            #lc_code+=f" {str(i.content)} {str(i.result)} "
            lc_code=f"SL{str(i.result)}E"
            self.send(lc_code)
            time.sleep(self.time * 60)
            
        print(lc_code)
        

    def radiogroup_changed(self,e):
        self.timer_text.value = f"Your chosen time interval for light is:  {e.control.value} mins"
        
        #pdb.set_trace()
        frame_count=int(e.control.value)//6
        self.time=frame_count
        print(frame_count)
        ls=[]
        if int(e.control.value) > 0:
            for i in range(0,6):
                content=f"{i*frame_count}-{(i*frame_count)+frame_count} Mins"
                ss=RadioOptions(content=content)
                #ss.update_text()
                ls.append(ss)
        
        self.slider_content.controls=ls
        self.update()
        print(ls[len(ls)-1].content, ls[len(ls)-1].result)

    def get_room_freshner_data(self,e):
        print("ODOUR CONTROL ",self.room_freshner.controls[0].slider_text.value)
        data=int(self.room_freshner.controls[0].slider_text.value)
        data="0"+str(data) if data < 10 else str(data)
        ser_code=f"SO1{data}E"
        self.send(ser_code)

    def get_actuator_data(self,e):
        
        print("ACTUATOR ",self.actuator.controls[0].slider_text.value)
        data=int(self.actuator.controls[0].slider_text.value)
        data="0"+str(data) if data < 10 else str(data)
        ser_code=f"SA1{data}E"
        self.send(ser_code)

    def build(self):
        self.serial_code=ft.Text(value="")
        #LC timer
        self.slider_content=ft.Column(controls=[])
        self.timer_options = ft.RadioGroup(value="0",content=ft.Row([
            ft.Radio(value="0", label="Off",fill_color=ft.colors.WHITE),
            ft.Radio(value="30", label="30",fill_color=ft.colors.WHITE),
            ft.Radio(value="60", label="60",fill_color=ft.colors.WHITE),
            ft.Radio(value="90", label="90",fill_color=ft.colors.WHITE)],alignment=ft.alignment.top_left), on_change=self.radiogroup_changed)
        self.timer_text = ft.Text(value=f"Your chosen time interval for light is: {self.timer_options.value} mins",color=ft.colors.WHITE)
        
        self.submit_button=ft.ElevatedButton("Send", color=ft.colors.WHITE,bgcolor=ft.colors.BLUE,on_click=self.submit_action)

        self.room_freshner=ft.Row([Slider(content="ODOUR CONTROL",flag=True),
                                   ft.ElevatedButton("Send", color=ft.colors.WHITE,bgcolor=ft.colors.BLUE,on_click=self.get_room_freshner_data)])
        self.actuator=ft.Row([Slider(content="TACTILE ACTUATOR",flag=True),
                              ft.ElevatedButton("Send", color=ft.colors.WHITE,bgcolor=ft.colors.BLUE,on_click=self.get_actuator_data)])
        self.card=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
            ft.ListTile(
                            leading=ft.Icon(name=ft.icons.LIGHTBULB,color=ft.colors.YELLOW),
                            title=ft.Text("LIGHT SCHEDULER",color=ft.colors.WHITE),
                            # subtitle=ft.Text(
                            #     "Music by Julie Gable. Lyrics by Sidney Stein."
                            # ),
                        ),
                      ft.Column(
                          controls=[self.timer_text,self.timer_options,self.slider_content,self.submit_button]
                      ),
                        ft.ListTile(
                            leading=ft.Icon(name=ft.icons.LOCAL_HOSPITAL,color=ft.colors.RED),
                            title=ft.Text("EVENT SCHEDULER",color=ft.colors.WHITE),
                            # subtitle=ft.Text(
                            #     "Music by Julie Gable. Lyrics by Sidney Stein."
                            # ),
                        ),
                      ft.Column(
                          controls=[self.room_freshner,self.actuator]
                      )
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

    
class RadioOptions(ft.UserControl):
    def __init__(self, content:str):
        super().__init__()
        self.content=content
        self.label_map={"0":"off",
                        "1":"daylight",
                        "2":"warm",
                        "3":"cool"}
        self.result=0
        
    
    def get_content(self):
        return f"{self.content} {self.result}\u2103"
            
    def light_change(self,e):
        
        print(e.control.value)
        self.result=int(e.control.value)
        self.slider_text.value=f"{self.label_map[e.control.value]}"

        self.update()
        print(self.content, self.result)
    

        
    def build(self):
        
        
        self.time_range=ft.Text(value=self.content,visible=True,color=ft.colors.WHITE)
          
        self.slider=ft.RadioGroup(value="0",content=ft.Row([
            ft.Radio(value="0", label="Off",fill_color=ft.colors.WHITE),
            ft.Radio(value="1", label="Daylight",fill_color=ft.colors.WHITE),
            ft.Radio(value="2", label="Warm",fill_color=ft.colors.WHITE),
            ft.Radio(value="3", label="Cool",fill_color=ft.colors.WHITE)],alignment=ft.alignment.top_left), on_change=self.light_change)
        self.result=int(self.slider.value) 
        self.slider_text=ft.Text(value=f"{self.label_map[self.slider.value]}",visible=True,color=ft.colors.WHITE)   
        self.slider_content=ft.Column(controls=[ft.Row(
                                [self.time_range],
                                alignment=ft.MainAxisAlignment.START,
                            ),ft.Row(
                                [self.slider,
                                #  self.slider_text
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            )])
        return self.slider_content
    
