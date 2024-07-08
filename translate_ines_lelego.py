def remplacer_mots(message, substitutions):
    mots = message.split()
    resultat = []

    for mot in mots:
        mot_lower = mot.lower()  
        if mot_lower in substitutions:
            resultat.append(substitutions[mot_lower])  
        else:
            resultat.append(mot)

    return ' '.join(resultat)

def main():
    substitutions = {
        'tro': 'trop',
        'trist': 'triste',
        'me vwar': 'me voir',
        '+': 'plus',
        'svnt': 'souvent',
        'dent': 'dans',
        'qq': 'quelque',
        'moi': 'mois'        
        
    }

    message = input("Entrez le message d'Ines : ")
    translation = remplacer_mots(message, substitutions)
    print(f"Traduction : \"{translation}\"")

if __name__ == "__main__":
    main()
