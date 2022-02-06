#CONSTANTS
O_SYMBOL = 'o'
X_SYMBOL = 'x'
NOT_TERMINAL = 0
VICTORY_O = 1
DRAW = 2
VICTORY_X = 3


def genBoard():
  return [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]


def printBoard(board):
  print('  1 2 3')
  for i in range(3):
    print('%d' % (i+1), *board[i],'', sep = '|')



def testTerminal(board):
  if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
    if(board[0][0]==X_SYMBOL):
      return VICTORY_X
    elif(board[0][0]==O_SYMBOL):
      return VICTORY_O

  if board[2][0]==board[1][1] and board[1][1]==board[0][2]:
    if(board[2][0]==X_SYMBOL):
      return VICTORY_X
    elif(board[2][0]==O_SYMBOL):
      return VICTORY_O

  for i in range(3):
    if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
      if(board[i][0]==X_SYMBOL):
        return VICTORY_X
      elif(board[i][0]==O_SYMBOL):
        return VICTORY_O
    if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
      if(board[0][i]==X_SYMBOL):
        return VICTORY_X
      elif(board[0][i]==O_SYMBOL):
        return VICTORY_O
  draw = True
  for i in range(3):
    if(' ' in board[i]):
      draw = False
  if(draw):
    return DRAW
  return NOT_TERMINAL

def action(board,symbol):
  terminal = testTerminal(board)
  if(terminal):
    return [terminal, board]
  actions = []
  for i in range(3):
    for j in range(3):
      if(board[i][j]==' '):
        copy = [list(board[0]),list(board[1]), list(board[2])]
        copy[i][j] = symbol
        actions.append([0, copy])
  if symbol == X_SYMBOL:
    for i in range(len(actions)):
      actions[i][0] = action(actions[i][1],O_SYMBOL)[0]
    return max(actions)
  else: 
    for i in range(len(actions)):
      actions[i][0] = action(actions[i][1],X_SYMBOL)[0]
    return min(actions)



def start_game(option):
  cpu_first = True
  cpu_turn = True
  board = genBoard()
  printBoard(board)
  player_turn = True
  while(not testTerminal(board)):
    if(cpu_turn and (option == 1 or option == 2)):
      if(player_turn and cpu_first):
        aux = action(board,X_SYMBOL)
        board = aux[1]
      elif(not player_turn):
        aux = action(board,O_SYMBOL)
        board = aux[1]
    if(option == 2 and not cpu_turn or option == 3):
      while(True):
        if(player_turn and (option == 3 or not cpu_first)):
          print('Jogador [x]: ')
          symbol = X_SYMBOL
        else:
          print('Jogador [o]: ')
          symbol = O_SYMBOL
        lin = int(input('linha: '))
        col = int(input('coluna: '))
        if(lin>0 and lin <4 and col>0 and col <4):
          if(board[lin-1][col-1]==' '):
            board[lin-1][col-1] = symbol
            break
    if(option == 2):
      cpu_turn = not cpu_turn
    printBoard(board)      
    player_turn = not player_turn
  return board