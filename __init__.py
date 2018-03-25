"""
ContactForm
===========

:class:`ContactForm` is a Kivy widget that allows users to send e-mails to specified addresses within apps.

Dependencies
------------

a. ``datetime``
b. ``email``
c. ``smtplib``

Usage
-----

TODO
"""

import datetime
import smtplib
from email.mime.text import MIMEText

from kivy.app import App
from kivy.lang import Builder
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
            halign: "right"
            valign: "middle"
            text_size: self.width / 10, self.height / 10
            size: self.texture_size
            pos_hint: {"center_x": .1, "center_y": .9}

        TextInput:
            id: input_name
            write_tab: False
            multiline: False
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .9}
            
        Label:
            id: txt_email
            text: "* E-mail:"
            halign: "right"
            valign: "middle"
            text_size: self.width / 10, self.height / 10
            size: self.texture_size
            pos_hint: {"center_x": .1, "center_y": .75}

        TextInput:
            id: input_email
            write_tab: False
            multiline: False
            input_type: "mail"
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .75}
            
        Label:
            id: txt_subject
            text: "Subject:"
            halign: "right"
            valign: "middle"
            text_size: self.width / 10, self.height / 10
            size: self.texture_size
            pos_hint: {"center_x": .1, "center_y": .6}

        TextInput:
            id: input_subject
            write_tab: False
            multiline: False
            padding_y: [self.height / 3, 0]
            size_hint: .7, .1
            pos_hint: {"center_x": .6, "center_y": .6}
            
        Label:
            id: txt_message
            text: "* Message:"
            halign: "right"
            valign: "middle"
            text_size: self.width / 10, self.height / 10
            size: self.texture_size
            pos_hint: {"center_x": .1, "center_y": .45}

        TextInput:
            id: input_message
            padding_y: [self.height / 9, 0]
            size_hint: .7, .3
            pos_hint: {"center_x": .6, "y": .2}
            
        Button:
            id: btn_send
            text: "SEND"
            size_hint: .3, .1
            pos_hint: {"center_x": .6, "center_y": .1}
            on_release: root.send()
            
        Image:
            id: img_status
            source: "img/ico_warning.png"
            opacity: 0
            size_hint_x: .075
            pos_hint: {"center_x": .8, "center_y": .1}
''')


class ContactForm(FloatLayout):
    """TODO"""

    def __init__(self, host, tls_port, username, password, receivers, pos=None, text_color=None, **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.host = host
        self.tls_port = tls_port
        self.username = username
        self.password = password
        self.receivers = receivers
        self.pos = pos
        self.text_color = text_color
        self.update()

    def update(self):
        if self.pos is not None:
            self.ids["layout_form"].pos = self.pos

        if self.text_color is not None:
            for i in [self.ids.txt_name, self.ids.txt_email, self.ids.txt_subject, self.ids.txt_message]:
                i.color = self.text_color

    def send(self):
        self.ids["img_status"].opacity = 0

        if (self.ids["input_email"] and self.ids["input_message"]).text.replace(" ", "") == "":
            self.ids["img_status"].source = "img/ico_warning.png"
            self.ids["img_status"].opacity = 1
        else:
            try:
                server = smtplib.SMTP(self.host, self.tls_port)
                server.starttls()
                server.login(self.username, self.password)

                message = MIMEText("%s sent a message via ContactForm (%s):\n\n%s" % (self.ids["input_name"].text, datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"), self.ids["input_message"].text))
                message["Subject"] = "via ContactForm: %s" % self.ids["input_subject"].text

                server.sendmail(self.username, self.receivers, message.as_string())
                server.quit()

                self.ids["img_status"].source = "img/ico_success.png"
                self.ids["img_status"].opacity = 1
            except:
                self.ids["img_status"].source = "img/ico_error.png"
                self.ids["img_status"].opacity = 1


class myApp(App):
    """TODO"""

    def build(self):
        return ContactForm(host="smtp.gmail.com", tls_port=587, username="myapp@gmail.com", password="123456", receivers=["me@gmail.com", "pr@gmail.com"], pos=(10, 10), text_color=(1, 1, 1, 1))


if __name__ == "__main__":
    myApp().run()
