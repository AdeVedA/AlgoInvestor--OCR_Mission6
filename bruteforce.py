def get_best_investment(shares_pack_listing):
    """Calculer/comparer/enregistrer le meilleur pack/rendement"""
    best_shares_pack = []
    best_shares_pack_yield = 0

    for shares_pack in shares_pack_listing:
        shares_pack_cost = sum(share[1] for share in shares_pack)
        shares_pack_yield = sum(
            share[1] * share[2] / 100 for share in shares_pack)

        # prendre en compte les packs qui respectent le budget
        # et qui ont un plus haut rendement
        if shares_pack_cost <= 500 and \
                shares_pack_yield > best_shares_pack_yield:
            best_shares_pack = shares_pack
            best_shares_pack_yield = shares_pack_yield

    return best_shares_pack


def explore_shares_packs(shares, shares_pack=[], BUDGET=500):
    """Créer toutes les combinaisons d'actions valides"""
    combinations = []
    current_cost = sum(share[1] for share in shares_pack)

    # verifier si on peut ajouter une action sans dépasser la limite de 500e
    can_extend = False
    for share in shares:
        if current_cost + share[1] <= BUDGET:
            can_extend = True
            break

    # quand mon panier est plein, je l'enregistre
    if not can_extend:
        combinations.append(shares_pack)

    # boucle et appel recursif pour explorer
    # toutes les combinaisons (respectant le budget)
    for i in range(len(shares)):
        share = shares[i]
        if current_cost + share[1] <= BUDGET:
            new_combination = shares_pack + [share]
            combinations += explore_shares_packs(
                shares[i + 1:], new_combination, BUDGET)

    return combinations

def get_shares():
    # Lire les données du fichier contenant les actions et leurs valeurs
    with open('Datas/actions.txt', 'r') as file:
        stock_market_shares = [line.strip().split() for line in file]
    # Convertir les données en format adéquat
    THE_SHARES = [[share[0], int(share[1]), int(
        share[2].replace('%', ''))] for share in stock_market_shares]
    return THE_SHARES

# # Initialiser la variable avec les données de datas.txt
# THE_SHARES = get_shares()
# 
# # Explorer toutes les combinaisons possibles
# combinations = explore_shares_packs(THE_SHARES)
# 
# # Trouver la meilleure combinaison
# best_shares_pack = get_best_investment(combinations)
# 
# # Affichage du résultat
# print("Le meilleur portefeuille d'actions : ", best_shares_pack)
