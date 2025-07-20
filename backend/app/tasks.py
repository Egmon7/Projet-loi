from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

@shared_task
def send_acknowledgment_email(to_email, sujet):
    """
    Envoie un accusé de réception à la personne qui a proposé la loi.
    """
    message = f"Votre proposition de loi intitulée : « {sujet} » a bien été reçue et sera traitée sous peu."
    send_mail(
        "Accusé de réception de votre proposition de loi",
        message,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )


@shared_task
def send_validation_notification(to_email, decision, sujet):
    """
    Envoie la notification de validation ou déclassement par le Bureau.
    """
    status = "classée" if decision == "valider" else "déclassée"
    message = f"""
La loi intitulée : « {sujet} » a été {status} par le Bureau après avis et considérations.

Merci pour votre contribution au processus législatif.
"""
    send_mail(
        "Décision du Bureau sur la Loi",
        message,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )


@shared_task
def send_conference_invitation(to_emails, conference_title, date):
    """
    Envoie une convocation à une conférence ou plénière aux destinataires concernés.
    """
    subject = f"Convocation à la conférence/plénière : {conference_title}"
    message = f"Vous êtes convoqué(e) à la conférence/plénière intitulée « {conference_title} » prévue le {date}."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        to_emails,
        fail_silently=False,
    )


@shared_task
def send_vote_reminder(to_emails, bill_subject):
    """
    Envoie un rappel pour participer au vote sur une loi.
    """
    subject = f"Rappel de vote pour la loi : {bill_subject}"
    message = f"Merci de ne pas oublier de participer au vote concernant la loi « {bill_subject} »."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        to_emails,
        fail_silently=False,
    )


@shared_task
def send_mass_notification(to_emails, subject, message):
    """
    Envoie une notification de masse (exemple : info plénière à tous les députés).
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        to_emails,
        fail_silently=False,
    )


@shared_task
def generate_bureau_report(nom_auteur, sujet, avis, decision, file_name=None):
    """
    Génère un rapport PDF du traitement par le Bureau.
    """
    dossier = os.path.join(settings.MEDIA_ROOT, 'rapports')
    os.makedirs(dossier, exist_ok=True)

    if not file_name:
        safe_nom = nom_auteur.replace(' ', '_')
        safe_sujet = sujet[:20].replace(' ', '_')
        file_name = f"rapport_{safe_nom}_{safe_sujet}.pdf"

    chemin_fichier = os.path.join(dossier, file_name)
    c = canvas.Canvas(chemin_fichier, pagesize=A4)

    # Titre
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 800, "RAPPORT DU BUREAU PARLEMENTAIRE")

    # Auteur et sujet
    c.setFont("Helvetica", 12)
    c.drawCentredString(300, 760, f"Auteur : {nom_auteur}")
    c.drawCentredString(300, 740, f"Sujet de la Loi : {sujet}")

    # Avis et considérations
    c.setFont("Helvetica-Bold", 13)
    c.drawString(70, 700, "Avis et considérations :")
    c.setFont("Helvetica", 11)
    text = c.beginText(80, 680)
    for line in avis.split('\n'):
        text.textLine(line)
    c.drawText(text)

    # Décision finale
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70, 150, f"Décision finale : LOI {decision.upper()}")

    c.save()
    return f"rapports/{file_name}"
