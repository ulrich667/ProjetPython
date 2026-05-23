
import json
import os

FICHIER_JSON = "bibliotheque.json"


def saisir_entier(message, min_val=0, max_val=9999):
    """Demande un entier valide à l'utilisateur dans un intervalle donné."""
    while True:
        try:
            valeur = int(input(message))
            if min_val <= valeur <= max_val:
                return valeur
            print(f"    Veuillez entrer un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("    Entrée invalide. Un nombre entier est attendu.")


def saisir_chaine(message, vide_ok=False):
    """Demande une chaîne non vide (sauf si vide_ok=True)."""
    while True:
        valeur = input(message).strip()
        if valeur or vide_ok:
            return valeur
        print("    Ce champ ne peut pas être vide.")


def saisir_statut():
    """Demande le statut de lecture : 'lu' ou 'non lu'."""
    while True:
        statut = input("  Statut (lu / non lu) : ").strip().lower()
        if statut in ("lu", "non lu"):
            return statut
        print("    Entrez 'lu' ou 'non lu'.")


def sauvegarder(livres):
    """Sauvegarde la liste des livres dans un fichier JSON."""
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(livres, f, ensure_ascii=False, indent=2)
    print(f"\n   Données sauvegardées dans « {FICHIER_JSON} ».")


def charger():
    """Charge et retourne la liste des livres depuis le fichier JSON.
    Retourne une liste vide si le fichier n'existe pas."""
    if not os.path.exists(FICHIER_JSON):
        return []
    with open(FICHIER_JSON, "r", encoding="utf-8") as f:
        return json.load(f)