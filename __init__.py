"""
ContactForm
===========

:class:`ContactForm` is a Kivy widget that allows users to send e-mails to specified addresses within apps.

Dependencies
------------

a. ``email``
b. ``smtplib``

Usage
-----

TODO
"""

import smtplib
from kivy.app import App
from kivy.lang import Builder
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kivy.uix.floatlayout import FloatLayout

__author__ = "Muhammed Yasin Yildirim"
__credits__ = ["Ali Emre Oz", "Fatih Cagatay Gulmez"]

Builder.load_string('''
<ContactForm>
    FloatLayout:
        id: layout_form
    
        Label:
            id: txt_name
            text: "Name:"
            multiline: False
            size_hint: .1, .1
            pos_hint: {"center_x": .1, "center_y": .9}

        TextInput:
            id: input_name
            hint_text: "Elon Musk"
            write_tab: False
            multiline: False
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .9}
            
        Label:
            id: txt_email
            text: "E-mail:"
            multiline: False
            size_hint: .1, .1
            pos_hint: {"center_x": .1, "center_y": .75}

        TextInput:
            id: input_email
            hint_text: "elon@spacex.com"
            write_tab: False
            multiline: False
            input_type: "mail"
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .75}
            
        Label:
            id: txt_subject
            text: "Subject:"
            multiline: False
            size_hint: .1, .1
            pos_hint: {"center_x": .1, "center_y": .6}

        TextInput:
            id: input_subject
            hint_text: "About Space"
            write_tab: False
            multiline: False
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .6}
            
        Label:
            id: txt_message
            text: "Message:"
            multiline: False
            size_hint: .1, .1
            pos_hint: {"center_x": .1, "center_y": .45}

        TextInput:
            id: input_message
            hint_text: "Have you ever been in Mars?"
            padding_y: [self.height / 9, 0]
            size_hint: .7, .3
            pos_hint: {"center_x": .6, "y": .2}
''')


class ContactForm(FloatLayout):
    """TODO"""

    def __init__(self, size, text_color, **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.size = size
        self.text_color = text_color
        self.__update__()

    def __update__(self):
        labels = [self.ids.txt_name, self.ids.txt_email, self.ids.txt_subject, self.ids.txt_message]
        for i in labels:
            i.color = self.text_color


class myApp(App):
    """TODO"""

    def build(self):
        return ContactForm(size=(100, 100), text_color=(1, 0, 0, 1))


if __name__ == "__main__":
    myApp().run()
