from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from cmath import phase

def paralel(n1, n2):
    return (n1*n2)/(n1+n2)


def Zeq(r1=0, r2=0, rc=0, x1=0, x2=0, xm=0, s=0):
    z1 = r1 + x1
    z2 = r2*((1-s)/s) + r2 + x2 
    if rc == 0:
        zm = xm
    elif xm == 0:
        zm = rc
    else:
        zm = paralel(rc, xm)
    return z1 + paralel(z2, zm)


class ZeqApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text='R1:'))
        self.r1_input = TextInput(multiline=False)
        layout.add_widget(self.r1_input)

        layout.add_widget(Label(text='R2:'))
        self.r2_input = TextInput(multiline=False)
        layout.add_widget(self.r2_input)

        layout.add_widget(Label(text='Rc:'))
        self.rc_input = TextInput(multiline=False)
        layout.add_widget(self.rc_input)

        layout.add_widget(Label(text='X1 (precisa do j no final):'))
        self.x1_input = TextInput(multiline=False)
        layout.add_widget(self.x1_input)

        layout.add_widget(Label(text='X2 (precisa do j no final):'))
        self.x2_input = TextInput(multiline=False)
        layout.add_widget(self.x2_input)

        layout.add_widget(Label(text='Xm (precisa do j no final):'))
        self.xm_input = TextInput(multiline=False)
        layout.add_widget(self.xm_input)

        layout.add_widget(Label(text='S (decimal):'))
        self.s_input = TextInput(multiline=False)
        layout.add_widget(self.s_input)

        calculate_button = Button(text='Calcular', on_press=self.calculate)
        layout.add_widget(calculate_button)

        self.result_label = Label(text='Esperando cálculo')
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        try:
            r1 = float(self.r1_input.text)
            r2 = float(self.r2_input.text)
            rc = float(self.rc_input.text)
            x1 = complex(self.x1_input.text)
            x2 = complex(self.x2_input.text)
            xm = complex(self.xm_input.text)
            s = float(self.s_input.text)

            result = Zeq(r1, r2, rc, x1, x2, xm, s)
            result_polar = f'{abs(result):.3f}/_ {phase(result):.3f}°'
            result_string = f'Complexo: {result:.3f}\nPolar: {result_polar}'
        except:
            result_string = 'Houve algum erro, \nNao utilize VIRGULA, \ncoloque J nos inputs com X'
        self.result_label.text = result_string
        

if __name__ == '__main__':
    ZeqApp().run()
