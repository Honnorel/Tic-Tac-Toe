tries = 0
winner = None
ivalue = ""
grid = [[ivalue for _i in range (3)] for _a in range (3)]
rounds = 0
value1 = input("Digite o símbolo do primeiro jogador:")
value2 = input("Digite o símbolo do segundo jogador:")
inusevalue = [value1,value2]
x = None
y = None
while True:

  #Representando o cenário de jogo
  for l in range(3):
    for c in range(3):
      print(f'[{grid[l][c]:^5}]',end='')
    print()

  #Escolha da jogada
  while True:
    x, y = input("Informe a linha e a coluna em que você deseja jogar: ").split()
    if grid[int(x)][int(y)]== "":
      break
    else:
      print("Novamente, o espaço escolhido já foi ocupado")
  grid [int(x)][int(y)] = inusevalue[0]
  rounds += 1

  #Avaliando o cenário para possível vitória
  for _a in range (3):
    if grid[_a][0] == grid[_a][1] == grid[_a][2] and grid[_a][0] != "":
      winner = inusevalue[0];
    if grid[0][_a] == grid[1][_a] == grid[2][_a] and grid[0][_a] != "":
      winner = inusevalue[0];
  for _a in range (2):
    if grid[0][abs(0-(_a*2))] == grid[1][1] == grid[2][abs(2-(_a*2))] and grid[1][1] != "":
      winner = inusevalue[0];

  #Reconstruindo as condições iniciais do jogo
  if winner != None:
    print(f"O jogador {winner} venceu!!")
    if int(input("Você quer rejogar? Responda 0 para não e 1 para sim: ")) == 1:
      print("Preparando revanche...")
      grid = [[ivalue for _i in range (3)] for _a in range (3)]
      rounds = 0
      winner = None
    else:
      break
  if rounds == 9:
    print("Deu velha!! Que pena, joguemos novamente")
    grid = [[ivalue for _i in range (3)] for _a in range (3)]
    rounds = 0

  #alterando a vez dos jogadores
  inusevalue = inusevalue[::-1]
  print(f"Agora é a vez do {inusevalue[0]}")

