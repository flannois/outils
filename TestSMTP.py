#!/usr/bin/env python3
"""
smtp_tester.py – Teste la connexion à un serveur SMTP, l’authentification
(optionnelle) et l’envoi d’un e‑mail de test.

Usage :
    python smtp_tester.py \
        --host smtp.exemple.com --port 587 \
        --username votre.login --password votre.motdepasse \
        --from you@example.com --to you@example.com \
        --starttls
"""

import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime
import sys

def send_test_email(args) -> None:
    context = ssl.create_default_context()
    try:
        if args['ssl']:
            server = smtplib.SMTP_SSL(args['host'], args['port'], context=context, timeout=10)
        else:
            server = smtplib.SMTP(args['host'], args['port'], timeout=10)
            if args['starttls']:
                server.starttls(context=context)

        print(f"✅ Connexion établie sur {args['host']}:{args['port']}")

        # Authentification si des identifiants sont fournis
        if args['username'] and args['password']:
            server.login(args['username'], args['password'])
            print("✅ Authentification réussie")

        # Préparation du message
        msg = EmailMessage()
        msg["Subject"] = "Test SMTP – " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg["From"] = args['from']
        msg["To"] = args['to']
        msg.set_content("Ceci est un e-mail de test généré automatiquement.")

        # Envoi
        server.send_message(msg)
        print(f"📨 E-mail envoyé avec succès à {args['to']}")

    except (smtplib.SMTPException, OSError) as e:
        print("❌ Erreur SMTP :", e, file=sys.stderr)
    finally:
        try:
            server.quit()
        except Exception:
            pass

if __name__ == "__main__":
    args = {"username":"contact@diexpertis.fr", 
    "password":"Brou77177@",
    "ssl":False,
    "starttls":True,
    "host":"ex4.mail.ovh.net",
    "port":587,
    "from":"contact@diexpertis.fr", 
    "to":"licieltest1@gmail.com"}
    send_test_email(args)
