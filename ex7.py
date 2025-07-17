# **Número secreto**
# Escolha um número fixo e peça para o usuário tentar adivinhar até acertar (de verdade).

# O que o programa deve fazer:

# - Pedir para o jogador digitar um número;
# - Repetir essa pergunta até ele acertar o número secreto;
# - Contar quantas tentativas ele fez;
# - Mostrar uma mensagem de parabéns e quantas tentativas ele fez até acertar.

num = 7
tentativas = 0

while True:
  numero = int(input("Digite um número de 1 a 10: "))
  tentativas += 1
  
  if numero == num:
    print(f"Parabéns, você acertou em {tentativas} tentativas")
    break
  else:
    print("Tente novamente!")

