# Modulo SMTP para enviar correos electrónicos.

# Importar el modulo:
import smtplib

import os    # Modulo que nos permitirá acceder a una env var.

# Creación de clase:
class Email():
    """Esta clase contiene distintos metodos para enviar mensajes a un determinado e-mail."""

    def __init__(self, yourEmail, destinationEmail, message, subject):

        self.de = yourEmail

        self.para = destinationEmail

        self.message = message

        self.password = os.getenv('MAIL_PASSWORD')

        self.subject = subject

        self.messageLen = len(message)

        self.message = "Subject: {}\n\n{}\n".format(self.subject, self.message)

        self.message += "-" * self.messageLen + "Mensaje enviado utilizando una libreria de Python. author: 'Marcos Ojeda'" + "-" * self.messageLen

    def intentar_envio(self):
        try:
            self.server = smtplib.SMTP(self.server, self.port)

            self.server.starttls()

            self.server.ehlo()

            self.server.login(self.de, self.password)

            self.server.sendmail(self.de, self.para, self.message)

        except SyntaxError:
            print("error de syntaxis.")

        except UnicodeEncodeError:
            print("error de codificacion ascii. (Usualmente es por representar caracteres no presentes en el abc americano.).")

        else:
            print("Mensaje enviado exitosamente.")

        finally:
            self.server.quit()

    def enviar_mensaje(self):
        if self.de.endswith("@gmail.com"):
            self.server = "smtp.gmail.com"

            self.port = 587

            self.intentar_envio()

        elif self.de.endswith("@outlook.com") or self.de.endswith("@hotmail.com") :
            self.server = "smtp.live.com"

            self.port = 465

            self.intentar_envio()

            