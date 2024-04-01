local = int(input())
if local == 1:
    genero = int(input())
    if genero == 0:
        rpg = int(input())
        if rpg == 0:
            ano = int(input())
            if ano == 0:
                print('Valheim')
            elif ano == 1:
                print('God of War')
            elif ano == 2:
                print("Baldur's Gate 3")
            elif ano == 3:
                print('Palworld')
        elif rpg == 1:
            tematica = int(input())
            if tematica == 0:
                print('Horizon Forbidden West')
            elif tematica == 1:
                print('Hogwarts Legacy')
            elif tematica == 2:
                print("ELDEN RING")
    elif genero == 1:
        categoria = int(input())
        if categoria == 0:
            print('Forza Horizon 4')
        elif categoria == 1:
            print('Session: Skate Sim')
        elif categoria == 2:
            print('FIFA 22')

    elif genero == 2:
        tipo = int(input())
        if tipo == 0:
            print('Euro Truck Simulator 2')
        elif tipo == 1:
            print('Stardew Valley')
        elif tipo == 2:
            print('Kerbal Space Program')
        elif tipo == 3:
            jogo_sims = int(input())
            if jogo_sims == 0:
                print('The Sims 1')
            elif jogo_sims == 1:
                print('The Sims 2')
            elif jogo_sims == 2:
                print('The Sims 3')
            elif jogo_sims == 3:
                exp_sims = int(input())
                if exp_sims == 0:
                    print('Parenthood')
                elif exp_sims == 1:
                    print('Junte-se à Galera')
                elif exp_sims == 2:
                    print('Vida Campestre')
                elif exp_sims == 3:
                    print('A Aventura de Crescer')
                elif exp_sims == 4:
                    print('Vida Universitária')
                elif exp_sims == 5:
                    print('Cats & Dogs')

    elif genero == 3:
        steam_review = int(input())
        if steam_review == 0:
            print('Thronefall')
        if steam_review == 1:
            print('Orcs Must Die! 3')
        if steam_review == 2:
            print('Plants vs. Zombies')

elif local == 0:
    com_quem = int(input())
    if com_quem == 0:
        faixa_etaria = int(input())
        if faixa_etaria == 0:
            print('O Castelo é Nosso')
        elif faixa_etaria == 1:
            print('Mysterium Park')
        elif faixa_etaria == 2:
            print('Pandemic')
        elif faixa_etaria == 3:
            print('Qual É o Seu Meme?')
    elif com_quem == 1:
        pessoas_max = int(input())
        if pessoas_max == 0:
            print('Descent: Lendas da Escuridão')
        elif pessoas_max == 1:
            print('Dixit')
        elif pessoas_max == 2:
            print('The Resistance')
        elif pessoas_max == 3:
            print('Sim, Mestre das Trevas (Edição Verde)')

    elif com_quem == 2:
        preços = int(input())
        if preços == 0:
            print('Dobble: Pixar')
        elif preços == 1:
            print('Caça aos Monstros')
        elif preços == 2:
            print('Ticket to Ride: Trem Fantasma')
        elif preços == 3:
            print('Scooby-Doo: The Board Game')
    elif com_quem == 3:
        tempo_de_partida = int(input())
        if tempo_de_partida == 0:
            print('Exploding Kittens')
        elif tempo_de_partida == 1:
            print('7 Wonders Duel')
        elif tempo_de_partida == 2:
            print('Azul: Pavilhão de Verão')
        elif tempo_de_partida == 3:
            print('Power Grid: Versão Energizada')
        elif tempo_de_partida == 4:
            print('Star Wars Rebellion')