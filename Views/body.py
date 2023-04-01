import flet as ft
import pdb
import serial 
import time

# if not ser.isOpen():
#     ser.open()
# time.sleep(1)
class TemperatureControl(ft.UserControl):
    
    def send(self,data):
        ser = serial.Serial('COM3',9600,timeout=0.05)
        if not ser.isOpen():
            ser.open()
        ser.write(data.encode())
        ser.write("\r\n".encode())
        ser.close()
        self.update()

    def add_click(self, e):
        
        self.counter += 1
        if self.counter%2 == 1:
            self.status.value = "AC ON"
            self.button.bgcolor=ft.colors.GREEN
            self.status.color=ft.colors.GREEN
        else:
            self.status.value = "AC OFF"
            self.button.bgcolor=ft.colors.RED
            self.status.color=ft.colors.RED
        #print("counter value : ",self.counter)  
          
        self.update()
        self.ac_info()
        self.update()
        
    def ac_info(self):
        if self.status.value=="AC OFF":
            print("AC is off") 
            
        else:
            print("AC is on")
            
            
    
    def submit_action(self,e):
        ac_code=""
        # if self.timer_options.value=="0":
        #     ac_code="AC0"
        #     print(f"AC0")
        #     self.serial_code.value= f"AC0" 
        # else:
            
        #     self.serial_code.value= f"AC1" 
        #     ac_code="AC1"
        for i in self.slider_content.controls:
            #ac_code+=f" {str(i.content)} {str(i.result)} "
            data=int(i.result)
            data="0"+str(data) if data < 10 else str(data)
            #ac_code=f"ST1{str(i.result)}E"
            ac_code=f"ST1{str(data)}E"
            print(ac_code)
            self.send(ac_code)
            time.sleep(15*60)
        print(ac_code)
        
        self.update()

    def temparature_change(self,e):
        print(e.control.value)
        #self.=f"{int(e.control.value)}\u2103"
        self.update()
    
    def radiogroup_changed(self,e):
        self.timer_text.value = f"Your chosen time interval for AC is:  {e.control.value} mins"
        
        #pdb.set_trace()
        loop_count=int(e.control.value)//15
        print(loop_count)
        ls=[]
        for i in range(0,loop_count):
            content=f"{i*15}-{(i*15)+15} Mins"
            ss=Slider(content=content,flag=False)
            #ss.update_text()
            ls.append(ss)
        
        self.slider_content.controls=ls
        self.update()
        print(ls[len(ls)-1].content, ls[len(ls)-1].result)
    
    def build(self):
        #AC serial code
        self.serial_code=ft.Text(value="")
        
        #AC on off status
        self.counter = 0
        self.status = ft.Text("AC OFF",color=ft.colors.RED)
        self.button=ft.ElevatedButton("Status", color=ft.colors.WHITE,bgcolor=ft.colors.RED,on_click=self.add_click)
        
        
        #AC timer
        
        self.timer_options = ft.RadioGroup(value="0",content=ft.Row([
            ft.Radio(value="0", label="Off",fill_color=ft.colors.WHITE),
            ft.Radio(value="30", label="30",fill_color=ft.colors.WHITE),
            ft.Radio(value="60", label="60",fill_color=ft.colors.WHITE),
            ft.Radio(value="90", label="90",fill_color=ft.colors.WHITE)],alignment=ft.alignment.top_left), on_change=self.radiogroup_changed)
        self.timer_text = ft.Text(value=f"Your chosen time interval for AC is: {self.timer_options.value} mins",color=ft.colors.WHITE)
        
       
        self.slider_content=ft.Column(controls=[])
        #submit action
        self.submit_button=ft.ElevatedButton("Send", color=ft.colors.WHITE,bgcolor=ft.colors.BLUE,on_click=self.submit_action)
        
        # #create room freshner
        # self.room_freshner=Slider(content="Room freshner",flag=True)
        
        # #create actuator
        # self.actuator=Slider(content="Actuator",flag=True)
        
        # self.panel=ft.Container(
        #     content=ft.Row(
        #         controls=[self.room_freshner,self.actuator]
        #     )
        # )
        #create a card for AC monitoring
        
        self.card=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(name=ft.icons.AC_UNIT_ROUNDED,color=ft.colors.LIGHT_BLUE),
                            title=ft.Text("Room - AC Control",color=ft.colors.WHITE),
                            # subtitle=ft.Text(
                            #     "Music by Julie Gable. Lyrics by Sidney Stein."
                            # ),
                        ),
                        # ft.Row(
                        #     [self.button,self.status],
                        #     alignment=ft.MainAxisAlignment.START,
                        # ),
                        ft.Row(
                            [self.timer_text],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [self.timer_options],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                         
                       ft.Row(
                            [self.slider_content],
                            alignment=ft.MainAxisAlignment.START,
                            
                        ),
                        
                        # ft.Row(
                        # [self.panel],
                        #  alignment=ft.MainAxisAlignment.START,
                        # ),
                        ft.Row(
                            [self.submit_button],
                            alignment=ft.MainAxisAlignment.END,
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
    
class Slider(ft.UserControl):
    def __init__(self, content:str, flag:bool):
        super().__init__()
        self.content=content
        self.flag=flag
        self.result=0
        
    
    def get_content(self):
        return f"{self.content} {self.result}\u2103"
            
    def temparature_change(self,e):
        print(e.control.value)
        self.result=int(e.control.value)
        if not self.flag:
            self.slider_text.value=f"{int(e.control.value)}\u2103"
        else:
            self.slider_text.value=f"{int(e.control.value)}"
        self.update()
        print(self.content, self.result)
    
    def check(self,e):
        if e.control.value:
            print(e.control.value)
            self.slider.visible=False
            self.slider_text.visible=False
            self.result=0
        else:
            print(e.control.value)
            self.slider.visible=True
            self.slider_text.visible=True
            self.result=self.slider.value
        self.update()
        
    def build(self):
        
        
        self.time_range=ft.Text(value=self.content,visible=True,color=ft.colors.WHITE)
        self.slider=ft.Slider(value=20.0,min=-20, max=40, divisions=60, label="{value}",on_change=self.temparature_change,visible=True,)
        self.result=int(self.slider.value)   
        if self.flag:
            print("Normal slider")
            self.slider=ft.Slider(value=0.0,min=0, max=99, divisions=100, label="{value}",on_change=self.temparature_change,visible=True,)
            self.slider_text=ft.Text(value=f"{int(self.slider.value)}",visible=True,color=ft.colors.WHITE)
            self.slider_content=ft.Column(controls=[ft.Row(
                                [self.time_range],
                                alignment=ft.MainAxisAlignment.START,
                            ),ft.Row(
                                [self.slider,self.slider_text],
                                alignment=ft.MainAxisAlignment.START,
                            )])
        else:
            #AC slider for values
            self.slider=ft.Slider(value=5,min=5, max=45, divisions=40, label="{value}",on_change=self.temparature_change,visible=True,)
            self.slider_text=ft.Text(value=f"{int(self.slider.value)} \u2103",visible=True,color=ft.colors.WHITE)
            self.cb=ft.Checkbox(label="Off", value=False,on_change=self.check)
            
            
            self.slider_content=ft.Column(controls=[ft.Row(
                                [self.time_range],
                                alignment=ft.MainAxisAlignment.START,
                            ),ft.Row(
                                [self.slider,self.slider_text,self.cb],
                                alignment=ft.MainAxisAlignment.START,
                            )])
        return self.slider_content
    
