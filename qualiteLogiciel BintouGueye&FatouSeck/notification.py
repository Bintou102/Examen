# notification.py
import logging

class EmailNotificationStrategy:
    def envoyer(self, message: str, membre: 'Membre'):
        logging.info(f"Notification envoyée à {membre.nom} par email: {message}")

class SMSNotificationStrategy:
    def envoyer(self, message: str, membre: 'Membre'):
        logging.info(f"Notification envoyée à {membre.nom} par SMS: {message}")
