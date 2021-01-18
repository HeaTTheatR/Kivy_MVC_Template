from kivymd.app import MDApp

from Controller.myscreen import MyScreenController
from Model.myscreen import MyScreenModel


class TextMVC(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = MyScreenModel()
        self.controller = MyScreenController(self.model)

    def build(self):
        return self.controller.get_screen()


TextMVC().run()
