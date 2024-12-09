import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from config.config import EMAIL, PASSWORD

def enviar_correo(destinatario, asunto, cuerpo, archivo_adj):
    # Configuración del correo
    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar archivo
    with open(archivo_adj, "rb") as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={archivo_adj}')
        mensaje.attach(parte)

    # Enviar correo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(EMAIL, PASSWORD)
        servidor.send_message(mensaje)
