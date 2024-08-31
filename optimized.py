import csv


def optimized_algorithm(shares):
    """algorithme optimisé de type glouton triant les données selon le facteur déterminant du rendement
    et sortant le paquet d'action le plus intéressant financièrement
    Args:
        shares (list): liste de listes/actions cleanées
    Returns:
        current_cost (float) : coût du paquet d'actions sélectionnées par l'algorithme
        shares_best_pack_yield (float) : valeur finale de profit dégagé au bout de 2 ans
        shares_best_pack (list) : liste des meilleures actions sélectionnées [[nom, coût, rendement en %], [...], ...]
    """
    # Trier par valeur de rendement (méthode algo glouton : meilleur choix local par tri selon valeur pertinente)
    sorted_shares = sorted(shares, key=lambda x: x[2], reverse=True)
    
    filtered_shares = [share for share in sorted_shares if share[1] >= 4]

    BUDGET = 496
    shares_best_pack = []
    current_cost = 0
    for share in filtered_shares:
        if current_cost + share[1] <= BUDGET:
            shares_best_pack.append(share)
            current_cost += share[1]
    shares_best_pack_yield = sum(share[1] * share[2] / 100 for share in shares_best_pack)
    print(f"\ncoût du meilleur portefeuille d'action : {current_cost}€")
    print(f"Rendement du meilleur portefeuille d'action : {shares_best_pack_yield}€")
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

    ratio = (share_pack_yield * 100) / share_pack_cost
    print(f"\nle ratio de notre solution est de {ratio}")
    print("===============================================") 
    print("\ncomparaison de la solution avec celle de Sienna")
    print("-----------------------------------------------") 
    sienna_ratio = (sienna_profit * 100) / sienna_cost    
    print(f"coût du portefeuille Sienna : {sienna_cost}€        Rendement : {sienna_profit}€")
    print(f"\nle ratio de la solution de Sienna est de {sienna_ratio}")
    print("===============================================")

def main():
    """programme principal"""
    raw_datas, dataset = get_shares()
    shares = cleaning_datas(raw_datas)
    share_pack_cost, share_pack_yield, shares_best_pack = optimized_algorithm(shares)
    benchmarking(share_pack_cost, share_pack_yield, dataset)
    print(f"\nL'algorithme optimisé appliqué au dataset n°{dataset} vous propose d'investir sur ce portefeuille d'action : \n")
    for share in shares_best_pack:
        print(share)
        
if __name__ == "__main__":
    main()