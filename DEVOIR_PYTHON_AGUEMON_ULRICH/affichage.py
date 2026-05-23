

# ─────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────

def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n" + "═" * 45)
    print("   MA BIBLIOTHÈQUE PYTHON")
    print("═" * 45)
    print("  1. Ajouter un livre")
    print("  2. Afficher tous les livres")
    print("  3. Rechercher un livre")
    print("  4. Modifier le statut de lecture")
    print("  5. Supprimer un livre")
    print("  6. Statistiques")
    print("  7. Sauvegarder et quitter")
    print("  8. Quitter sans sauvegarder")
    print("═" * 45)


# ─────────────────────────────────────────────
# AFFICHAGE DES LIVRES (tableau formaté)
# ─────────────────────────────────────────────

def afficher_livres(livres, titre_section="Tous les livres"):
    """Affiche les livres sous forme de tableau formaté.

    Args:
        livres (list): liste de dicts à afficher
        titre_section (str): titre du tableau
    """
    if not livres:
        print("\n  ℹ️  Aucun livre à afficher.")
        return

    print(f"\n  ── {titre_section} ({len(livres)} livre(s)) ──")
    print(f"  {'#':<4} {'Titre':<28} {'Auteur':<20} {'Année':<6} {'Genre':<15} {'Statut'}")
    print("  " + "─" * 82)

    for i, l in enumerate(livres, 1):
        statut_icon = "✅ lu" if l["statut"] == "lu" else "📖 non lu"
        print(f"  {i:<4} {l['titre']:<28} {l['auteur']:<20} {l['annee']:<6} {l['genre']:<15} {statut_icon}")

    print("  " + "─" * 82)


# ─────────────────────────────────────────────
# AFFICHAGE DES STATISTIQUES
# ─────────────────────────────────────────────

def afficher_statistiques(stats):
    """Affiche les statistiques de la bibliothèque.

    Args:
        stats (dict): résultat de gestion_livres.statistiques()
    """
    print("\n  ── 📊 Statistiques ──")
    if stats["total"] == 0:
        print("  Bibliothèque vide.")
        return

    print(f"  Total de livres    : {stats['total']}")
    print(f"  Livres lus         : {stats['lus']}")
    print(f"  Livres non lus     : {stats['non_lus']}")
    print(f"  Genres présents    : {', '.join(sorted(stats['genres']))}")
    print(f"  Livre le + ancien  : {stats['plus_ancien'][1]} ({stats['plus_ancien'][0]})")
    print(f"  Livre le + récent  : {stats['plus_recent'][1]} ({stats['plus_recent'][0]})")


# ─────────────────────────────────────────────
# AFFICHAGE DU SOUS-MENU RECHERCHE
# ─────────────────────────────────────────────

def afficher_menu_recherche():
    """Affiche le sous-menu de recherche."""
    print("\n  Rechercher par :")
    print("    1. Titre (partiel)")
    print("    2. Auteur")
    print("    3. Genre")