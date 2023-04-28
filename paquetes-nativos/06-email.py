from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje['From'] = "Salvador German"
mensaje['To'] = "salvadorenriquegb@gmail.com"
mensaje['Subject'] = "Prueba de envío de correo"

cuerpo = MIMEText("Este es el cuerpo del mensaje")

mensaje.attach(cuerpo)

with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
    servidor.ehlo()
    servidor.starttls()

    servidor.login("salvador.german8914@alumnos.udg.mx", "YAANACR1985")
    servidor.send_message(mensaje)
    print("Correo enviado con éxito")
