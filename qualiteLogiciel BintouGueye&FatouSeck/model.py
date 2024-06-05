from datetime import datetime
from typing import List

class Membre:
    def __init__(self, nom: str, role: str):
        self.nom = nom
        self.role = role

class Equipe:
    def __init__(self):
        self.membres: List[Membre] = []  # Type annotation ajoutée

    def ajouter_membre(self, membre: Membre):
        self.membres.append(membre)

    def obtenir_membres(self) -> List[Membre]:
        return self.membres

class Tache:
    def __init__(self, nom: str, description: str, date_debut: str, date_fin: str, responsable: Membre, statut: str = 'Non démarrée'):
        self.nom = nom
        self.description = description
        self.date_debut = datetime.strptime(date_debut, "%Y-%m-%d")
        self.date_fin = datetime.strptime(date_fin, "%Y-%m-%d")
        self.responsable = responsable
        self.statut = statut
        self.dependances: List['Tache'] = []  # Type annotation ajoutée

    def ajouter_dependance(self, tache: 'Tache'):
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str):
        self.statut = statut

class Jalon:
    def __init__(self, nom: str, date: str):
        self.nom = nom
        self.date = datetime.strptime(date, "%Y-%m-%d")

class Risque:
    def __init__(self, description: str, probabilite: float, impact: str):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact
class Changement:
    def __init__(self, description: str, version: int, date: str):
        self.description = description
        self.version = version
        self.date = datetime.strptime(date, "%Y-%m-%d")

class Projet:
    def __init__(self, nom: str, description: str, date_debut: str, date_fin: str, budget: float):
        self.nom = nom
        self.description = description
        self.date_debut = datetime.strptime(date_debut, "%Y-%m-%d")
        self.date_fin = datetime.strptime(date_fin, "%Y-%m-%d")
        self.budget = budget
        self.taches: List[Tache] = []  # Type annotation ajoutée
        self.equipe = Equipe()
        self.risques: List[Risque] = []  # Type annotation ajoutée
        self.jalons: List[Jalon] = []  # Type annotation ajoutée
        self.changements: List[Changement] = []  # Type annotation ajoutée
        self.notification_context = None

    def set_notification_strategy(self, strategy):
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        self.taches.append(tache)
        self.notifier(f"Nouvelle tâche ajoutée: {tache.nom}")

    def ajouter_membre_equipe(self, membre: Membre):
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajouté à l'équipe")

    def definir_budget(self, budget: float):
        self.budget = budget
        self.notifier(f"Le budget du projet a été défini à {budget} unités monétaires")

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)
        self.notifier(f"Nouveau risque ajouté: {risque.description}")

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)
        self.notifier(f"Nouveau jalon ajouté: {jalon.nom}")

    def enregistrer_changement(self, description: str, version: int):
        changement = Changement(description, version, datetime.now().strftime("%Y-%m-%d"))
        self.changements.append(changement)
        self.notifier(f"Changement enregistré: {description} (version {version})")

    def notifier(self, message: str):
        if self.notification_context:
            destinataires = self.equipe.obtenir_membres()
            self.notification_context.notifier(message, destinataires)

class NotificationContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def notifier(self, message: str, destinataires: List[Membre]):
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
