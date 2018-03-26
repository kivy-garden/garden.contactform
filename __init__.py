#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ContactForm
===========

:class: `ContactForm` provides a Kivy widget for sending e-mail to specified addresses from a form on app.

Dependencies
------------

a. ``datetime``
b. ``email``
c. ``smtplib``

Usage
-----

from kivy.garden.contactform import ContactForm
myContactForm = ContactForm(host="smtp.gmail.com", tls_port=587,
                            username="myapp@gmail.com", password="123456",
                            receivers=["me@gmail.com", "pr@gmail.com"],
                            size=(750, 600), pos=(0, 0), text_color=(1, 0, 0, 1))
"""

import smtplib
from datetime import datetime
from email.mime.text import MIMEText

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

__author__ = "Muhammed Yasin Yıldırım"
__credits__ = ["Ali Emre Öz", "Fatih Çağatay Gülmez"]

Builder.load_string('''
<ContactForm>
    FloatLayout:
        id: layout_form
        size_hint: None, None
    
        canvas.before:
            Rectangle:
                source: "bg_gray.png"
                size: self.size
                pos: self.pos
                
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
            source: "ico_warning.png"
            opacity: 0
            size_hint_x: .075
            pos_hint: {"center_x": .8, "center_y": .1}
''')


class ContactForm(FloatLayout):
    """
    Provides a widget for sending e-mail to specified addresses from a form on app.
    """

    def __init__(self, host, tls_port, username, password, receivers, size, pos, text_color=None, **kwargs):
        """
        Assigns given inputs to the self parameter and then calls the update method.
        :param host: SMTP server of the account used for sending e-mails.
        :param tls_port: SMTP port of the account used for sending e-mails.
        :param username: E-mail address of the account used for sending e-mails.
        :param password: Password of the account used for sending e-mails.
        :param receivers: List of e-mail addresses that will receive e-mails.
        :param size: Size of the contact form.
        :param pos: Position of the contact form on app.
        :param text_color: Text color of the labels used on the contact form.
        """

        super(ContactForm, self).__init__(**kwargs)
        self.host = host
        self.tls_port = tls_port
        self.username = username
        self.password = password
        self.receivers = receivers
        self.size = size
        self.pos = pos
        self.text_color = text_color
        self.update()

    def update(self):
        """
        Updates size and position of the form as well as text color of the labels if specified.
        Otherwise, text color is set to (0, 0, 0, 1) as default.
        """

        self.ids["layout_form"].size = self.size
        self.ids["layout_form"].pos = self.pos

        if self.text_color is not None:
            labels = [
                self.ids["txt_name"],
                self.ids["txt_email"],
                self.ids["txt_subject"],
                self.ids["txt_message"]
            ]

            for i in labels:
                i.color = self.text_color

    def send(self):
        """
        Sends user's message with given information to specified addresses
        through provided e-mail account when the send button is clicked.
        """

        self.ids["img_status"].opacity = 0

        if not (self.ids["input_email"].text.strip() and self.ids["input_message"].text.strip()):
            self.ids["img_status"].source = "ico_warning.png"
            self.ids["img_status"].opacity = 1
        else:
            try:
                server = smtplib.SMTP(self.host, self.tls_port)
                server.starttls()
                server.login(self.username, self.password)

                time = datetime.now().strftime("%I:%M%p on %B %d, %Y")

                inputs = [
                    self.ids["input_name"],
                    self.ids["input_email"],
                    self.ids["input_subject"],
                    self.ids["input_message"]
                ]

                message = MIMEText("%s (%s) sent a message via ContactForm (%s):\n\n%s" % (inputs[1].text,
                                                                                           inputs[0].text,
                                                                                           time,
                                                                                           inputs[3].text))
                message["Subject"] = "via ContactForm: %s" % inputs[2].text

                server.sendmail(self.username, self.receivers, message.as_string())
                server.quit()

                for i in inputs:
                    i.text = ""

                self.ids["img_status"].source = "ico_success.png"
                self.ids["img_status"].opacity = 1
            except smtplib.SMTPException:
                self.ids["img_status"].source = "ico_error.png"
                self.ids["img_status"].opacity = 1


class myApp(App):
    def build(self):
        return ContactForm(host="smtp.gmail.com", tls_port=587,
                           username="myapp@gmail.com", password="123456",
                           receivers=["me@gmail.com", "pr@gmail.com"],
                           size=(750, 600), pos=(0, 0), text_color=(1, 1, 1, 1))


if __name__ == "__main__":
    myApp().run()
