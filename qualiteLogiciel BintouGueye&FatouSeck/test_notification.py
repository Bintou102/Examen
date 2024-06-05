# test_notification.py
import unittest
import logging
from model import Membre
from notification import EmailNotificationStrategy, SMSNotificationStrategy

class TestNotificationStrategies(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_email_notification(self):
        strategy = EmailNotificationStrategy()
        membre = Membre("Alice", "Développeur")
        with self.assertLogs(level='INFO') as log:
            strategy.envoyer("Test message", membre)
            self.assertIn("Notification envoyée à Alice par email: Test message", log.output[0])

    def test_sms_notification(self):
        strategy = SMSNotificationStrategy()
        membre = Membre("Bob", "Manager")
        with self.assertLogs(level='INFO') as log:
            strategy.envoyer("Test message", membre)
            self.assertIn("Notification envoyée à Bob par SMS: Test message", log.output[0])

if __name__ == '__main__':
    unittest.main()
