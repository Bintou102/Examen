"""
Module de gestion de projet.

Ce module gère la création, la gestion et la notification des événements de projet.
"""

from model import Projet, Tache, Membre, Risque, Jalon  # Supprimé Changement
from notification import EmailNotificationStrategy  # Supprimé SMSNotificationStrategy

# Initialisation du projet
projet = Projet("Nouveau Produit", "Développement d'un nouveau produit",
                "2024-01-01", "2024-12-31", 50000)

# Ajout des membres de l'équipe
membre1 = Membre("Modou", "Chef de projet")
membre2 = Membre("Christian", "Développeur")
projet.ajouter_membre_equipe(membre1)
projet.ajouter_membre_equipe(membre2)

# Définition de la stratégie de notification
projet.set_notification_strategy(EmailNotificationStrategy())

# Ajout des tâches
tache1 = Tache("Analyse des besoins", "Analyser les besoins des clients",
               "2024-01-01", "2024-01-31", membre1)
tache2 = Tache("Développement", "Développer le produit",
               "2024-02-01", "2024-06-30", membre2)
projet.ajouter_tache(tache1)
projet.ajouter_tache(tache2)

# Définition du budget
projet.definir_budget(50000)

# Ajout des risques
risque = Risque("Retard de livraison", 0.3, "Élevé")
projet.ajouter_risque(risque)

# Ajout des jalons
jalon = Jalon("Phase 1 terminée", "2024-01-31")
projet.ajouter_jalon(jalon)

# Enregistrement des changements
projet.enregistrer_changement("Changement de la portée du projet", 2)

# Générer un rapport (simplifié pour l'exemple)
print(f"Rapport d'activités du Projet '{projet.nom}':")
print(f"Version: {projet.changements[-1].version}")
print(f"Date: {projet.date_debut} à {projet.date_fin}")
print(f"Budget: {projet.budget} unités monétaires")
print("Équipe:")
for membre in projet.equipe.obtenir_membres():
    print(f"- {membre.nom} ({membre.role})")
print("Tâches:")
for tache in projet.taches:
    print(f"- {tache.nom} ({tache.date_debut} à {tache.date_fin}) "
          f"Responsable: {tache.responsable.nom} Statut: {tache.statut}")
print("Jalons:")
for jalon in projet.jalons:
    print(f"- {jalon.nom} ({jalon.date})")
print("Risques:")
for risque in projet.risques:
    print(f"- {risque.description} (Probabilité: {risque.probabilite} "
          f"Impact: {risque.impact})")
print("Chemin critique (simplifié):")
for tache in projet.taches:
    print(f"- {tache.nom} ({tache.date_debut} à {tache.date_fin})")
