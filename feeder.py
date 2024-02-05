KV = '''
MDFloatLayout:

    MDLabel:
        text: 'Ingredient Feeder'
        halign: 'center'
        pos_hint: {'top': 1}
        size_hint: (1, 0.10)
        theme_text_color: 'Primary'
        font_size: '20sp'
        bold: True
        font_style: 'H6'
        font_family: 'Inter'
    MDTextField:
        id : ingredient_name
        hint_text: 'Enter Ingredient Name:'
        max_text_length: 20
        helper_text: 'Ingredient Name'
        helper_text_mode: 'on_focus'
        mode: 'round'
        pos_hint: {'center_x': 0.5, 'center_y': 0.80}
        size_hint: (0.75, 0.05)
        font_size: '20sp'
    MDRoundFlatButton:
        id: btn
        text: 'Select Ingredient Type'
        text_color: "black"
        pos_hint: {'center_x': 0.5, 'center_y': 0.69}
        size_hint: (0.75, 0.05)
        on_parent: drop_content.dismiss()
        on_release: drop_content.open(self)

    DropDown:
        id: drop_content
        on_select: btn.text = f'{args[1]}' # see note below
        MDRoundFlatButton:
            id: btn1
            text: 'Type 1 : Meat'
            text_color: "black"
            size_hint: (0.75, 0.05)
            md_bg_color: 'orange'
            on_release: drop_content.select('Type 1 : Meat')
        MDRoundFlatButton:
            id: btn2
            text: 'Type 2 : Fish'
            text_color: "black"
            size_hint: (0.75, 0.05)
            md_bg_color: 'orange'
            on_release: drop_content.select('Type 2 : Fish')
        MDRoundFlatButton:
            id: btn3
            text: 'Type 3 : Vegetable'
            text_color: "black"
            size_hint: (0.75, 0.05)
            md_bg_color: 'orange'
            on_release: drop_content.select('Type 3 : Vegetable')
        MDRoundFlatButton:
            id: btn4
            text: 'Type 4 : Fruit'
            text_color: "black"
            size_hint: (0.75, 0.05)
            md_bg_color: 'orange'
            on_release: drop_content.select('Type 4 : Fruit')
    MDLabel:
        text: 'Ingredient Image:'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.59}
        size_hint: (1, 0.3)
        theme_text_color: 'Primary'
        font_size: '15sp'
        font_style: 'Body1'
        font_family: 'Inter'


    MDRaisedButton:
        text: 'Attach Ingredient Image Here'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint: (0.8, 0.3)
        md_bg_color: 'orange'
        on_release:
            app.file_chooser()  
        Image:
            id: img   

    MDRaisedButton:
        text: 'CONFIRM'
        text_color: "yellow"
        bold: True
        md_bg_color: 'orange'
        font_size: '20sp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.16}
        size_hint: (0.4, 0.07)
        on_release:
            app.confirm_pressed()
'''

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from plyer import filechooser
import shutil


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        Window.size = (400, 800)
        return Builder.load_string(KV)

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        ingredient_name = self.root.ids.ingredient_name.text
        if selection:
            source_path = selection[0]
            destination_folder = "F:\Ailuto\Assistant"  # Replace with your actual destination folder
            destination_path = f"{destination_folder}/"+ingredient_name+".jpg"

            try:
                shutil.copy(source_path, destination_path)
                print(f"Image copied to: {destination_path}")
                self.root.ids.img.source = destination_path
            except Exception as e:
                print(f"Error copying image: {e}")

    def confirm_pressed(self):
        # Get the text from the text fields
        ingredient_name = self.root.ids.ingredient_name.text


        # Do something with the captured text (e.g., print it)
        print(f"Ingredient Name: {ingredient_name}")


if __name__ == "__main__":
    MainApp().run()
