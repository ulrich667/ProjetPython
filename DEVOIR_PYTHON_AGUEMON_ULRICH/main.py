
zzZzé
zé
zézézézzzzé
from gestion_livres import (ajouter_livre, supprimer_livre, modifier_statut,
                             rechercher_par_titre, rechercher_par_auteur,
                             rechercher_par_genre, statistiques)
from affichage import (afficher_menu, afficher_livres,
                       afficher_statistiques, afficher_menu_recherche)
from utils import saisir_chaine, saisir_entier, saisir_statut, sauvegarder, charger

def handle_ajouter(livres):
    """Saisie et ajout d'un nouveau livre."""
    print("\n  ── Ajouter un livre ──")
    titre  = saisir_chaine("  Titre  : ")
    auteur = saisir_chaine("  Auteur : ")
    annee  = saisir_entier("  Année  : ", 0, 2100)
    genre  = saisir_chaine("  Genre  : ")
    statut = saisir_statut()

    if ajouter_livre(livres, titre, auteur, annee, genre, statut):
        print(f"\n  « {titre} » ajouté avec succès !")
    else:
        print(f"\n    Un livre intitulé « {titre} » existe déjà.")


def handle_afficher(livres):
    """Affiche tous les livres."""
    afficher_livres(livres)


def handle_rechercher(livres):
    """Sous-menu de recherche."""
    afficher_menu_recherche()
    choix = saisir_entier("  Votre choix : ", 1, 3)

    if choix == 1:
        mot = saisir_chaine("  Mot-clé dans le titre : ")
        resultats = rechercher_par_titre(livres, mot)
        afficher_livres(resultats, f"Résultats pour « {mot} »")
    elif choix == 2:
        auteur = saisir_chaine("  Nom de l'auteur : ")
        resultats = rechercher_par_auteur(livres, auteur)
        afficher_livres(resultats, f"Livres de « {auteur} »")
    elif choix == 3:
        genre = saisir_chaine("  Genre : ")
        resultats = rechercher_par_genre(livres, genre)
        afficher_livres(resultats, f"Genre « {genre} »")


def handle_modifier_statut(livres):
    """Bascule le statut lu  non lu d'un livre."""
    afficher_livres(livres)
    titre = saisir_chaine("\n  Titre du livre à modifier : ")
    nouveau = modifier_statut(livres, titre)
    if nouveau:
        print(f"\n  ✅ Statut mis à jour → « {nouveau} ».")
    else:
        print(f"\n  ⚠️  Livre « {titre} » introuvable.")


def handle_supprimer(livres):
    """Supprime un livre par son titre."""
    afficher_livres(livres)
    titre = saisir_chaine("\n  Titre du livre à supprimer : ")
    confirmation = input(f"  Confirmer la suppression de « {titre} » ? (o/n) : ").strip().lower()
    if confirmation == 'o':
        if supprimer_livre(livres, titre):
            print(f"\n  ✅ « {titre} » supprimé.")
        else:
            print(f"\n  ⚠️  Livre « {titre} » introuvable.")
    else:
        print("  Suppression annulée.")


def handle_statistiques(livres):
    """Calcule et affiche les statistiques."""
    stats = statistiques(livres)
    afficher_statistiques(stats)


# ══════════════════════════════════════════════════════════
#  BOUCLE PRINCIPALE
# ══════════════════════════════════════════════════════════

def main():
    """Point d'entrée : charge les données et lance le menu en boucle."""
    livres = charger()
    print(f"\n  📂 Bibliothèque chargée : {len(livres)} livre(s) trouvé(s).")

    actions = {
        1: handle_ajouter,
        2: handle_afficher,
        3: handle_rechercher,
        4: handle_modifier_statut,
        5: handle_supprimer,
        6: handle_statistiques,
    }

    while True:
        afficher_menu()
        choix = saisir_entier("  Votre choix (1-8) : ", 1, 8)

        if choix in actions:
            actions[choix](livres)

        elif choix == 7:              # Sauvegarder et quitter
            sauvegarder(livres)
            print("\n  À bientôt ! \n")
            break

        elif choix == 8:              # Quitter sans sauvegarder
            confirm = input("  Quitter sans sauvegarder ? (o/n) : ").strip().lower()
            if confirm == 'o':
                print("\n  À bientôt ! \n")
                break


if __name__ == "__main__":
    main()