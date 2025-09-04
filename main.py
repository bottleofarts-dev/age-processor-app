from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=40)

        self.name_input = MDTextField(
            hint_text="Enter your name",
            size_hint_x=1
        )
        layout.add_widget(self.name_input)

        self.age_input = MDTextField(
            hint_text="Enter your age",
            size_hint_x=1,
            input_filter="int"
        )
        layout.add_widget(self.age_input)

        self.output_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(self.output_label)

        process_btn = MDRaisedButton(
            text="Process",
            pos_hint={"center_x": 0.5}
        )
        process_btn.bind(on_release=self.process_data)
        layout.add_widget(process_btn)

        self.add_widget(layout)

    def process_data(self, instance):
        name = self.name_input.text
        age = self.age_input.text

        if name and age:
            self.output_label.text = f"Hello {name}, you are {age} years old!"
        else:
            self.output_label.text = "Please enter both name and age."


class AgeApp(MDApp):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    AgeApp().run()
  