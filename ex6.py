# **Quiz de perguntas e respostas**
# Crie um jogo de perguntas com pontuação.

# O que o programa deve fazer:

# - Guardar uma lista de perguntas com as respectivas respostas;
# - Mostrar uma pergunta por vez e esperar a resposta do jogador;
# - Verificar se a resposta está correta;
# = Somar +1 ponto a cada acerto;
# - No final, mostrar uma mensagem com a pontuação total.

# - Use uma **lista de listas** com a estrutura `["pergunta", "resposta"]`;
# - Use um **laço** `for` para percorrer todas as perguntas;
# - Compare a resposta com a correta usando `lower()`;
# - Crie uma **variável** `acertos` que começa em 0 e vai aumentando a cada acerto.

perguntas = [
  ["1+1 = ?", "2"],
  ["Meu primeiro nome:", "André"],
  ["Este ano?", "2025"],
  ["Nome da minha namorada", "Lara"]
  ]

acertos = 0

for pergunta in perguntas:
  resposta = input(pergunta[0] + " ")
  if resposta.lower() == pergunta[1].lower():
    acertos += 1

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")
