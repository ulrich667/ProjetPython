
# ─────────────────────────────────────────────
# 1. AJOUTER UN LIVRE
# ─────────────────────────────────────────────

def ajouter_livre(livres, titre, auteur, annee, genre, statut):
    """Ajoute un livre (dict) à la liste si le titre n'existe pas déjà.

    Args:
        livres (list): collection de livres
        titre, auteur (str): informations textuelles
        annee (int): année de publication
        genre (str): genre littéraire
        statut (str): 'lu' ou 'non lu'

    Returns:
        bool: True si ajouté, False si doublon détecté
    """
    titres_existants = {l["titre"].lower() for l in livres}   # set pour détection rapide
    if titre.lower() in titres_existants:
        return False

    livre = {
        "titre":  titre,
        "auteur": auteur,
        "annee":  annee,
        "genre":  genre,
        "statut": statut,
    }
    livres.append(livre)
    return True


# ─────────────────────────────────────────────
# 2. SUPPRIMER UN LIVRE
# ─────────────────────────────────────────────

def supprimer_livre(livres, titre):
    """Supprime le livre dont le titre correspond (insensible à la casse).

    Args:
        livres (list): collection de livres
        titre (str): titre à supprimer

    Returns:
        bool: True si supprimé, False si introuvable
    """
    for i, livre in enumerate(livres):
        if livre["titre"].lower() == titre.lower():
            livres.pop(i)
            return True
    return False


# ─────────────────────────────────────────────
# 3. RECHERCHER DES LIVRES
# ─────────────────────────────────────────────

def rechercher_par_titre(livres, mot_cle):
    """Recherche partielle (insensible à la casse) dans les titres.

    Returns:
        list: livres correspondants
    """
    return [l for l in livres if mot_cle.lower() in l["titre"].lower()]


def rechercher_par_auteur(livres, auteur):
    """Recherche exacte (insensible à la casse) par auteur.

    Returns:
        list: livres correspondants
    """
    return [l for l in livres if l["auteur"].lower() == auteur.lower()]


def rechercher_par_genre(livres, genre):
    """Recherche exacte (insensible à la casse) par genre.

    Returns:
        list: livres correspondants
    """
    return [l for l in livres if l["genre"].lower() == genre.lower()]


# ─────────────────────────────────────────────
# 4. MODIFIER LE STATUT DE LECTURE
# ─────────────────────────────────────────────

def modifier_statut(livres, titre):
    """Bascule le statut lu
     zéézénon lu pour le livre indiqué.

    Returns:
        str | None: nouveau statut ou None si livre introuvable
    """
    for livre in livres:
        if livre["titre"].lower() == titre.lower():
            livre["statut"] = "non lu" if livre["statut"] == "lu" else "lu"
            return livre["statut"]
    return None


# ─────────────────────────────────────────────
# 5. STATISTIQUES
# ─────────────────────────────────────────────

def statistiques(livres):
    """Calcule et retourne les statistiques de la bibliothèque.

    Utilise :
      - set   → genres uniques
      - tuple → (annee, titre) pour trouver le plus ancien / récent

    Returns:
        dict contenant toutes les statistiques
    """
    total = len(livres)
    if total == 0:
        return {"total": 0}

    lus     = sum(1 for l in livres if l["statut"] == "lu")
    non_lus = total - lus

    genres_uniques = {l["genre"] for l in livres}   # set

    # tuples (annee, titre) pour comparaisons
    tuples_annees = [(l["annee"], l["titre"]) for l in livres]
    plus_ancien  = min(tuples_annees)
    plus_recent  = max(tuples_annees)

    return {
        "total":         total,
        "lus":           lus,
        "non_lus":       non_lus,
        "genres":        genres_uniques,
        "plus_ancien":   plus_ancien,
        "plus_recent":   plus_recent,
    }