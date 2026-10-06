from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.08, 1)


class AmountCalculator(App):

    def build(self):
        self.last_result = ""

        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        title = Label(
            text="Amount Splitter",
            font_size=28,
            size_hint=(1, 0.12)
        )

        self.input_box = TextInput(
            hint_text="Amount Enter Koro",
            multiline=False,
            input_filter="int",
            font_size=24,
            size_hint=(1, 0.12)
        )

        calc_btn = Button(
            text="Calculate",
            font_size=22,
            size_hint=(1, 0.12)
        )
        calc_btn.bind(on_press=self.calculate)

        copy_btn = Button(
            text="Copy Result",
            font_size=18,
            size_hint=(1, 0.1)
        )
        copy_btn.bind(on_press=self.copy_result)

        self.result = Label(
            text="Result Ekhane Dekhabe",
            font_size=20,
            text_size=(Window.width - 50, None)
        )

        layout.add_widget(title)
        layout.add_widget(self.input_box)
        layout.add_widget(calc_btn)
        layout.add_widget(copy_btn)
        layout.add_widget(self.result)

        return layout

    def calculate(self, instance):
        try:
            amount = int(self.input_box.text)

            nums = []
            remaining = amount

            for n in range(50, 0, -1):
                if remaining >= n:
                    nums.append(n)
                    remaining -= n

            if remaining == 0:
                text = " + ".join(map(str, nums))
                text += f" = {amount}"

                self.result.text = text
                self.last_result = text

            else:
                self.result.text = "Valid Combination Pawa Jai Nai"
                self.last_result = ""

            self.input_box.text = ""

        except:
            self.result.text = "Sudhu Number Dao"

    def copy_result(self, instance):
        if self.last_result:
            Clipboard.copy(self.last_result)
            self.result.text += "\n\n✓ Copied"


AmountCalculator().run()