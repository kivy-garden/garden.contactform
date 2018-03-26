# ContactForm
Kivy garden flower providing a widget for sending e-mail from a form on app

Dependencies
------------

1. ``datetime``
2. ``email``
3. ``smtplib``

Params
------

- **host**: SMTP server of the account used for sending e-mails
- **tls_port**: SMTP port of the account used for sending e-mails
- **username**: E-mail address of the account used for sending e-mails
- **password**: Password of the account used for sending e-mails
- **receivers**: List of e-mail addresses that will receive e-mails
- **size**: Size of the contact form
- **pos**: Position of the contact form on app
- **text_color**: Text color of the labels used on the contact form

Usage
-----

```python
from kivy.garden.contactform import ContactForm

myContactForm = ContactForm(host="smtp.gmail.com", tls_port=587,
                            username="myapp@gmail.com", password="123456",
                            receivers=["me@gmail.com", "pr@gmail.com"],
                            size=(750, 600), pos=(0, 0), text_color=(1, 0, 0, 1))
```

Screenshot
----------

![Screenshot](https://github.com/myasiny/garden.contactform/blob/master/screenshot.png "ContactForm")
