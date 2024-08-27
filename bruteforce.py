def get_best_investment(shares_pack_listing):
    """Calculer/comparer/enregistrer le meilleur pack/rendement"""
    best_shares_pack = []
    best_shares_pack_yield = 0
    
    print(f"le nombre de combinaisons ne dépassant pas 500€ : {len(shares_pack_listing)}")

    # itérer sur l'ensemble des packs d'actions et calculer le coût et le rendement de chacun
    for shares_pack in shares_pack_listing:
        shares_pack_cost = sum(share[1] for share in shares_pack)
        shares_pack_yield = sum(
            share[1] * share[2] / 100 for share in shares_pack)

        # trouver le pack qui a le plus haut rendement
        if shares_pack_yield > best_shares_pack_yield:
            best_shares_pack = shares_pack
            best_shares_pack_yield = shares_pack_yield
    # afficher les valeurs importantes du résultat 
    print(f"coût du meilleur portefeuille d'action : {sum(share[1] for share in best_shares_pack)}€")
    print(f"Rendement du meilleur portefeuille d'action : {best_shares_pack_yield}€")
    return best_shares_pack


def explore_shares_packs(shares, shares_pack=[], BUDGET=500):
    """Créer toutes les combinaisons d'actions valides par récursivité"""
    combinations = []
    current_cost = sum(share[1] for share in shares_pack)

    # verifier si on peut ajouter une action sans dépasser la limite de 500e
    for share in shares:
        if current_cost + share[1] <= BUDGET:
            break
        # quand mon panier est plein, je l'enregistre (condition d'arrêt)
        else:
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

def main():
    """programme principal"""
    # Initialiser la variable THE_SHARES avec les données de datas.txt
    THE_SHARES = get_shares()
    # Explorer toutes les combinaisons possibles
    combinations = explore_shares_packs(THE_SHARES)
    # Trouver la meilleure combinaison
    best_shares_pack = get_best_investment(combinations)
    # Affichage du résultat
    print("Le meilleur portefeuille d'actions : ", best_shares_pack)

if __name__ == "__main__":
    main()