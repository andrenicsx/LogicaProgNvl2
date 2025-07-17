# **Caça ao tesouro espacial**
# Um tesouro está escondido em um planeta misterioso. Ele está em alguma linha e coluna de um mapa 4x4. Você tem 5 chances para tentar adivinhar onde ele está!

# O que o programa deve fazer:

# - Criar um tabuleiro 3x3 com espaços vazios (listas dentro de listas);
# - Definir uma posição fixa para o tesouro (por exemplo: linha 1, coluna 2);
# - Pedir ao jogador para chutar linha e coluna (valores entre 0 e 2);
# - Atualizar o tabuleiro a cada tentativa:
#     - Marcar com `'X'` os espaços já tentados.
#     - Marcar com `'💎'` quando o tesouro for encontrado.
# - Mostrar uma mensagem se:
#     - O jogador acertar o local do tesouro;
#     - O jogador errar**;**
#     - O jogador tentar uma posição inválida;
#     - O jogador já tiver tentado aquele espaço;
# - Após 5 tentativas, encerrar o jogo e revelar a localização do tesouro.

tabuleiro = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  ]

linhaTesouro = 0
colunaTesouro = 2

def exibeTabuleiro():
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-' * 5)

tentativas = 5

print('Encontre o X escondido pelo tabuleiro')
print('Lembre de usar somente números entre 0 e 2 para linha e coluna')

for i in range(tentativas):
  print(f'\nTentativa {i+1} de {tentativas}')

  linha = int(input('Digite a linha: '))
  coluna = int(input('Digite a coluna: '))

  if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
    print('Posição inválida! Use de 0 a 2')
    continue
  
  if linha == linhaTesouro and coluna == colunaTesouro:
    tabuleiro[linha][coluna] = 'X'
    print('\nParabéns, você encontrou o tesouro!')
    exibeTabuleiro()
    break
  else:
    if tabuleiro[linha][coluna] != ' ':
      print('\nVocê já tentou aqui.')
    else: 
      tabuleiro[linha][coluna] = 'O'
      print('\nContinue procurando')
    exibeTabuleiro()
else:
  print('\nSuas tentativas acabaram!')
  tabuleiro[linhaTesouro][colunaTesouro] = 'X'
  print('\nO tesouro estava aqui.')
  exibeTabuleiro()

