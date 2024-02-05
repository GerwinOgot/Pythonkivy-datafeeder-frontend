from kivymd.app import MDApp  # helps us in creating an app by getting the MDApp
from kivymd.uix.label import MDLabel, MDIcon  # importing ui packages that will be used inside the app
from kivymd.uix.button import MDIconButton
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window  # this is for adding the window size


class AiLuto(MDApp):  # making a class then naming the app
    def build(self):  # building the app by this code
        Window.size = (400, 800)  # window size for iphone????

        layout = FloatLayout()

        label = MDLabel(
            text='What is in your Kitchen?',
            halign='center',
            pos_hint={'top': 1},  # Position the label at the top of the layout
            size_hint=(1,0.10),
            size=(Window.width, 20),  # Adjust the label height as needed
            theme_text_color='Primary',
            font_size='20sp',
            bold=True,
            font_style='H6',
            font_family='Inter')  # the text that will be shown on the screen, halign is the alignment of the text

        button = MDIconButton(
            icon='cameras',
            halign='center',  # icons
            pos_hint={'center_x': 0.5, 'center_y': 0.89}, # Position the button at the center
            size_hint=(None,None),
            size=(10,10),# Set button size
        )

        layout.add_widget(label)
        layout.add_widget(button)
        return layout
        # return nothing not showing anything on the screen


AiLuto().run()  # this is how you run the app
