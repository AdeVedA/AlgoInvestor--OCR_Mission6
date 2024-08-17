import csv


def optimized_algorithm(shares):
    """algorithme optimisé de type glouton triant les données selon le facteur déterminant du rendement
    et sortant le paquet d'action le plus intéressant financièrement
    Args:
        shares (list): liste de listes/actions cleanées
    Returns:
        current_cost (float) : _description_
        shares_best_pack_yield (float) : 
        shares_best_pack (list) : 
    """
    # Filtrer les actions dont le coût est inférieur à 10 (pour optimiser les résultats)
    shares = [share for share in shares if share[1] >= 10]

    # Trier par rendement (méthode algo glouton : meilleur choix local)
    sorted_shares = sorted(shares, key=lambda x: x[2], reverse=True)

    BUDGET = 500
    shares_best_pack = []

    for share in sorted_shares:
        current_cost = sum(share[1] for share in shares_best_pack)
        if current_cost + share[1] <= BUDGET:
            shares_best_pack.append(share)
    shares_best_pack_yield = sum(share[1] * share[2] / 100 for share in shares_best_pack)
    print(f"\ncoût du portefeuille d'action : {current_cost}€        Rendement : {shares_best_pack_yield}€")
    # print(f"Voici le meilleur portefeuille d'action selon l'algorithme optimisé : {shares_best_pack}")
    return current_cost, shares_best_pack_yield, shares_best_pack

def old_optimized_algorithm(shares):
    """algorithme optimisé de type glouton triant les données selon le facteur déterminant du rendement
    et sortant le paquet d'action le plus intéressant financièrement
    Args:
        shares (list): liste de listes/actions cleanées
    Returns:
        current_cost (float) : _description_
        shares_best_pack_yield (float) : 
        shares_best_pack (list) : 
    """
    # Filtrer les actions dont le coût est inférieur à 10 (pour optimiser les résultats)
    # filtered_shares = [share for share in shares if share[1] >= 10]

    # Trier par rendement (méthode algo glouton : meilleur choix local)
    sorted_shares = sorted(shares, key=lambda x: x[2], reverse=True)

    BUDGET = 500
    shares_best_pack = []

    for share in sorted_shares:
        current_cost = sum(share[1] for share in shares_best_pack)
        if current_cost + share[1] <= BUDGET:
            shares_best_pack.append(share)
    shares_best_pack_yield = sum(share[1] * share[2] / 100 for share in shares_best_pack)
    print(f"\ncoût du portefeuille d'action : {current_cost}€        Rendement : {shares_best_pack_yield}€")
    # print(f"Voici le meilleur portefeuille d'action selon l'algorithme optimisé : {shares_best_pack}")
    return current_cost, shares_best_pack_yield, shares_best_pack

def get_shares(file_path='Datas/'):
    """permet de choisir le fichier .csv de data sur lequel on va travailler
    Args:
        file_path (str, optional): repertoire dans lequel se trouvent les fichier dataset[i]_Python+P7.csv
        Defaults to 'Datas/'.
    Returns:
        raw_datas (list): liste de listes/actions à l'état brute
        dataset (int): identifiant du dataset pour automatiser le benchmarking par la suite
    """
    print("\nBonjour, sur quel dataset souhaitez-vous travailler ?")

    while True:
        choice = input("Entrez 1 (dataset1_Python+P7) ou 2 (dataset2_Python+P7) : ")
        match choice:
            case '1':
                shares_file = file_path + "dataset1_Python+P7.csv"
                dataset = 1
                break
            case '2':
                shares_file = file_path + "dataset2_Python+P7.csv"
                dataset = 2
                break
            case _:
                print("Votre choix est invalide. Veuillez recommencer !")

    with open(shares_file, 'r') as file:
        reader = csv.reader(file)
        raw_datas = list(reader)
    return raw_datas, dataset

def cleaning_datas(datas):
    """nettoie les datas :
    enlève la 1ère ligne de titres,
    convertit en types adéquat,
    enlève les actions incorrectes <= 0
    Args:
        raw_shares (list): liste de listes/actions avec [nom, 'coût', 'rendement']
    Returns:
        positive_shares (list): liste de listes/actions avec [nom, coût, rendement]
    """
    titleless_shares = datas[1:]
    raw_shares = [[share[0], float(share[1]), float(share[2])] for share in titleless_shares]
    positive_shares = [share for share in raw_shares if share[1] > 0 and share[2] > 0]
    return positive_shares
    
def benchmarking(share_pack_cost, share_pack_yield, dataset):
    """comparaison des coûts et des profit de la solution de l'algorithme 
    avec la solution précédente de Sienna
    """
    # initialisation des valeurs de coût et de profit à 2ans de Sienna
    # en fonction du dataset choisi dans get_shares()
    if dataset == 1:
        sienna_cost = 498.76
        sienna_profit = 196.61
    elif dataset == 2:
        sienna_cost = 489.24
        sienna_profit = 193.78
        
    print(f"coût du portefeuille Sienna : {sienna_cost}€        Rendement : {sienna_profit}€")
    print("\ncomparaison de la solution avec celle de Sienna")
    print("===============================================")
    cost_difference = share_pack_cost - sienna_cost
    profit_difference = share_pack_yield - sienna_profit
    gain = profit_difference - cost_difference
    print(f"\nle gain differentiel sera donc de {gain}€")
    
    if cost_difference >= 0:
        print(f"\nla solution du nouvel algorithme coûtera {abs(cost_difference)}€ de plus que la solution de Sienna")
    if cost_difference < 0:
        print(f"\nla solution du nouvel algorithme coûtera {abs(cost_difference)}€ de moins que la solution de Sienna")
    if profit_difference >= 0:
        print(f"\nla solution du nouvel algorithme rapportera {abs(profit_difference)}€ de plus que la solution de Sienna")
    if profit_difference < 0:
        print(f"\nla solution du nouvel algorithme rapportera {abs(profit_difference)}€ de moins que la solution de Sienna")

def main():
    raw_datas, dataset = get_shares()
    shares = cleaning_datas(raw_datas)
    share_pack_cost, share_pack_yield, shares_best_pack = optimized_algorithm(shares)
    benchmarking(share_pack_cost, share_pack_yield, dataset)
    print(f"\nun conseil, investissez sur ce portefeuille d'action : \n")
    print(shares_best_pack)
    for e in shares_best_pack:
        print(e)
        
if __name__ == "__main__":
    main()