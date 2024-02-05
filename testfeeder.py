from kivymd.app import MDApp  # helps us in creating an app by getting the MDApp
from kivymd.uix.label import MDLabel, MDIcon  # importing ui packages that will be used inside the app
from kivymd.uix.textfield import MDTextField
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window  # this is for adding the window size


class AiLuto(MDApp):  # making a class then naming the app
    def build(self):  # building the app by this code
        self.theme_cls.primary_palette = "Orange"
        Window.size = (400, 800)  # window size for iphone????

        layout = FloatLayout()

        label = MDLabel(
            text='Ingredient Feeder',
            halign='center',
            pos_hint={'top': 1},  # Position the label at the top of the layout
            size_hint=(1, 0.10),
            size=(Window.width, 20),  # Adjust the label height as needed
            theme_text_color='Primary',
            font_size='20sp',
            bold=True,
            font_style='H6',
            font_family='Inter'
        )  # the text that will be shown on the screen, halign is the alignment of the text

        name = MDLabel(
            text='Ingredient Name:',
            halign='left',
            pos_hint={'center_x': 0.63, 'center_y': 0.85},  # Position the label at the top of the layout
            size_hint=(1, 0.3),
            size=(Window.width, 20),  # Adjust the label height as needed
            theme_text_color='Primary',
            font_size='15sp',
            font_style='Body1',
            font_family='Inter'
        )

        iname = MDTextField(
            hint_text="Enter Ingredient Name:",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},  # Position the label at the top of the layout
            size_hint=(0.75, 0.3),
            size=(Window.width, 10),  # Adjust the label height as needed
            font_size='20sp',
        )
        itype = MDTextField(
            hint_text="Enter Ingredient Type:",
            pos_hint={'center_x': 0.5, 'center_y': 0.70},  # Position the label at the top of the layout
            size_hint=(0.75, 0.3),
            size=(Window.width, 10),  # Adjust the label height as needed
            font_size='20sp',
        )
        ingreimg = MDLabel(
            text='Ingredient Image:',
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.59},  # Position the label at the top of the layout
            size_hint=(1, 0.3),
            size=(Window.width, 20),  # Adjust the label height as needed
            theme_text_color='Primary',
            font_size='15sp',
            font_style='Body1',
            font_family='Inter'
        )
        btn1 = Button(
            text='Attach Ingredient Image Here',
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.4},  # Position the label at the top of the layout
            size_hint=(0.8, 0.3),
            color=(8, 5, .2, 99),
            background_color=(2.5, 1, .100, 5),
        )
        btn2 = Button(
            text='CONFIRM',
            bold=True,
            color=(8, 5, .2, 99),
            font_size='20sp',
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.16},  # Position the label at the top of the layout
            size_hint=(0.4, 0.07),
            background_color=(2.5, 1, .100, 5),
        )
        btn1.bind(on_press=self.callbackbtn1)
        btn2.bind(on_press=self.callbackbtn2)

        layout.add_widget(btn2)
        layout.add_widget(btn1)
        layout.add_widget(ingreimg)
        layout.add_widget(itype)
        layout.add_widget(iname)
        layout.add_widget(label)
        return layout
        # return nothing not showing anything on the screen
    def callbackbtn1(self, event):
        print("Attach Image")
    def callbackbtn2(self, event):
        print("SUBMIT CONFIRMED")

root = AiLuto()

root.run()  # this is how you run the app
