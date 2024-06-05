import unittest
from model import Projet, Tache, Membre, Risque, Jalon, Changement

class TestProjet(unittest.TestCase):
    def test_ajouter_membre_equipe(self):
        projet = Projet("Test", "Description", "2024-01-01", "2024-12-31", 1000)
        membre = Membre("Alice", "Développeur")
        projet.ajouter_membre_equipe(membre)
        self.assertEqual(len(projet.equipe.obtenir_membres()), 1)
        self.assertEqual(projet.equipe.obtenir_membres()[0].nom, "Alice")

    def test_ajouter_tache(self):
        projet = Projet("Test", "Description", "2024-01-01", "2024-12-31", 1000)
        membre = Membre("Alice", "Développeur")
        tache = Tache("Tâche 1", "Description", "2024-01-01", "2024-01-31", membre)
        projet.ajouter_tache(tache)
        self.assertEqual(len(projet.taches), 1)
        self.assertEqual(projet.taches[0].nom, "Tâche 1")

    def test_ajouter_risque(self):
        projet = Projet("Test", "Description", "2024-01-01", "2024-12-31", 1000)
        risque = Risque("Retard", 0.5, "Moyen")
        projet.ajouter_risque(risque)
        self.assertEqual(len(projet.risques), 1)
        self.assertEqual(projet.risques[0].description, "Retard")

    def test_ajouter_jalon(self):
        projet = Projet("Test", "Description", "2024-01-01", "2024-12-31", 1000)
        jalon = Jalon("Jalon 1", "2024-01-31")
        projet.ajouter_jalon(jalon)
        self.assertEqual(len(projet.jalons), 1)
        self.assertEqual(projet.jalons[0].nom, "Jalon 1")

    def test_enregistrer_changement(self):
        projet = Projet("Test", "Description", "2024-01-01", "2024-12-31", 1000)
        projet.enregistrer_changement("Changement de portée", 2)
        self.assertEqual(len(projet.changements), 1)
        self.assertEqual(projet.changements[0].description, "Changement de portée")

if __name__ == '__main__':
    unittest.main()
