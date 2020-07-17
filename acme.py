#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from smtplib import SMTP
def main():
    from_address = "acme.eestn4@gmail.com"
    to_address = "correo del usuario@gmail.com"
    message = "Hola,usted se a registrado exitosamente!"
    
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
    
    smtp = SMTP("smtp.ejemplo.com")
    smtp.login(from_address, "clave")
    
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
if __name__ == "__main__":
    main()
