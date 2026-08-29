import random

#LISTA DE FILMES

filmes_comedia = [
    "As Branquelas",
    "Shrek",
    "A nova onda do Imperador",
    "Miss Simpatia",
    "Se Beber, Não Case",
    "O Auto da Compadecida",
    "Uma Noite no Museu",
    "Tá dando Onda",
    "Madagascar",
    "Legalmente Loira",
    "Meninas Malvadas",
    "Minha Mãe é uma Peça",
    "Diário de um Banana",
    "Click",
    "Curtindo a Vida Adoidado"
]

filmes_tristes = [
    "Um Olhar do Paraíso",
    "A Espera de um Milagre",
    "Diário de uma Paixão",
    "Viva, a Vida é uma Festa",
    "Uma prova de Amor",
    "Te Amarei para Sempre",
    "Questo de Tempo",
    "A Culpa é das Estrelas",
    "As Vantagens de Ser Invisível",
    "A Beleza Oculta",
    "Ponte para Terabítia",
    "Robô Selvagem",
    "O Menino do Pijama Listrado",
    "Sempre ao Seu Lado",
    "Marley e Eu"
]

filmes_romance = [
    "Como Eu Era Antes de Você",
    "Orgulho e Preconceito",
    "Ele Não Está Tão a Fim de Você",
    "10 Coisas que Eu Odeio em Você",
    "Um lugar Chamado Notting Hill",
    "Elementos",
    "Casa Comigo?",
    "Enquanto Você Dormia",
    "O Diário de Bridget Jones",
    "A Proposta",
    "O Amor Não Tira Férias",
    "Simplesmente Acontece",
    "O Casamento do Meu Melhor Amigo",
    "Antes do Amanhecer",
    "E se fosse Verdade"
]

filmes_reflexao = [
    "A Chegada",
    "O Jogo da Imitação",
    "O Show de Truman",
    "Interstellar",
    "A Origem",
    "A Lista de Schindler",
    "Divertida Mente",
    "Soul",
    "Sonhos de Trem",
    "Coringa",
    "Brilho Eterno de uma Mente sem Lembranças",
    "Vidas Passadas",
    "A Ghost Story",
    "O Quarto de Jack",
    "Garota, Interrompida"
]

filmes_terror = [
    "Obssessão",
    "O Iluminado",
    "Corra!",
    "O Exorcista",
    "O Massacre da Serra Elétrica",
    "Hereditário",
    "A Hora do Pesadelo",
    "A Hora do Mal",
    "Midsommar",
    "Eu Sei o que Vocês Fizeram no Verão Passado",
    "Pânico",
    "Faça ela voltar",
    "A Hora da sua Morte",
    "Jogos Mortais",
    "Nós"
]

filmes_acao = [
    "Mad Max: Estrada da Fúria",
    "John Wick",
    "Missão Impossível",
    "Duro de Matar",
    "Em Ritmo de Fuga",
    "O Exterminador do Futuro",
    "Matrix",
    "A Odisseia",
    "Guardiôes da Galáxia",
    "Gladiador",
    "Top Gun: Maverick",
    "X-men: O Filme",
    "Jogos Vorazes",
    "Piratas do Caribe: A Maldição do Pérola Negra",
    "Capitão América: Guerra Civil"
]

filmes_fantasia = [
    "Alice no País das Maravilhas",
    "Avatar",
    "O Lar das crianças Peculiares",
    "Como Treinar o seu Dragão",
    "As Crônicas de Nárnia",
    "A Viagem de Chihiro",
    "Coração de Tinta",
    "Viagem ao Centro da Terra",
    "Malévola",
    "Animais Fantásticos e Onde Habitam",
    "Duna",
    "Castelo Animado",
    "Mestres do Universo",
    "Super Mario Bros: O Filme",
    "Wicked"
]

filmes_suspense = [
    "Não olhe para cima",
    "Backrooms",
    "Fragmentado",
    "Mãe!",
    "Àguas rasas",
    "Um lugar silencioso",
    "Sinais",
    "Bugonia",
    "Garota Exemplar",
    "Telefone Preto",
    "Ilha do Medo",
    "Anatomia de uma Queda",
    "Five Night´s at Freddy´s: O Pesadelo sem Fim",
    "O Ilusionista",
    "Corpo Fechado"
]

filmes_musical = [
    "Frozen 2",
    "O Rei Leão 2",
    "Encantada",
    "A Bela e a Fera",
    "Mamma Mia",
    "O Rei do Show",
    "Irmão Urso",
    "Moana",
    "Mulan",
    "O Príncipe do Egito",
    "O Mágico de Oz",
    "Enrolados",
    "Tarzan",
    "Nem que a Vaca Tussa",
    "A Pequena Sereia"
]

filmes_lgbt = [
    "Brookeback Mountain",
    "Love, Simon",
    "Me Chame pelo seu Nome",
    "Imagine Eu e Você",
    "Nunca fui Santa",
    "Vermelho, Branco e Sangue Azul",
    "Um Amor Secreto",
    "Luar",
    "O País de Deus",
    "LHoney, Não!",
    "Twinless: Um Gêmeo a Menos",
    "Paloma",
    "Retrato de Uma Jovem em Chamas",
    "Matthias e Maxime",
    "Rafiki"
]

filmes_femininos = [
    "De Repente 30",
    "O Diabo veste Prada",
    "Uma Linda Mulher",
    "Miss Simpatia",
    "Adoráveis Mulheres",
    "Red: Crescer é uma Fera",
    "Eu, Tonya",
    "O Diário da Princesa",
    "Barbie",
    "Legalmente Loira",
    "Meninas Malvadas",
    "Lady Bird",
    "Estrelas Além do Tempo",
    "Cruella",
    "Mulan"
]

filmes_diversos = [
    "Encontros e Desencontros",
    "Na Natureza Selvagem",
    "Diários de Motocicleta",
    "Up: Altas Aventuras",
    "A Vida Secreta de Walter Mitty",
    "Para Roma, com amor",
    "Sob o sol da Toscana",
    "A Praia",
    "Ultima viagem a Vegas",
    "Paris pode esperar",
    "Thelma & Louise",
    "O Turista",
    "Meia-Noite em Paris",
    "Antes de Partir",
    "Entre Montanhas",
]

#TÍTULO

print("================================")
print("          🎬 CINEMOOD")
print("================================")
print("Encontre um filme para o seu momento atual!")

#MENU

print("\nComo você quer se sentir hoje?\n")

print("1 - 😂 Quero morrer de rir")
print("2 - 😭 Quero chorar até desidratar")
print("3 - ❤️ Quero me apaixonar")
print("4 - 🤔 Quero refletir")
print("5 - 😱 Quero sentir medo")
print("6 - 🔥 Quero adrenalina")
print("7 - 💭​ Quero fugir da realidade")
print("8 - 👀 Quero me surpreender")
print("9 - 🎵​ Quero cantar até perder a voz")
print("10 - ​👤​ Quero me redescobrir como ser humano")
print("11 - 👩‍🦰​ Quero me redescobrir como mulher")
print("12 - ​🌍​ Quero descobrir o mundo")

#ESCOLHA DO USUÁRIO

escolha = input("\nDigite o número correspondente à sua escolha: ")

#RECOMENDAÇÃO

if escolha == "1":
    recomendacao = random.choice(filmes_comedia)
    print("\n😂 Recomendação: ", recomendacao)

elif escolha == "2":
    recomendacao = random.choice(filmes_tristes)
    print("\n😭 Recomendação: ", recomendacao)

elif escolha == "3":
    recomendacao = random.choice(filmes_romance)
    print("\n❤️ Recomendação: ", recomendacao)

elif escolha == "4":
    recomendacao = random.choice(filmes_reflexao)
    print("\n🤔 Recomendação: ", recomendacao)

elif escolha == "5":
    recomendacao = random.choice(filmes_terror)
    print("\n😱 Recomendação: ", recomendacao)

elif escolha == "6":
    recomendacao = random.choice(filmes_acao)
    print("\n🔥​ Recomendação: ", recomendacao)

elif escolha == "7":
    recomendacao = random.choice(filmes_fantasia)
    print("\n💭​ Recomendação: ")

elif escolha == "8":
    recomendacao = random.choice(filmes_suspense)
    print("\n👀​ Recomendação: ", recomendacao)

elif escolha == "9":
    recomendacao = random.choice(filmes_musical)
    print("\n​​🎵​ Recomendação: ", recomendacao)    

elif escolha == "10":
    recomendacao = random.choice(filmes_lgbt)
    print("\n​👤​ Recomendação: ", recomendacao)

elif escolha == "11":
    recomendacao = random.choice(filmes_femininos)
    print("\n👩‍🦰​ Recomendação: ", recomendacao)

elif escolha == "12":
    recomendacao = random.choice(filmes_diversos)
    print("\n🌍 Recomendação: ", recomendacao)

else:
    print("\n❌ Opção inválida!")

