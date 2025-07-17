# **Oráculo da sabedoria Python**
# Neste exercício, você vai criar um assistente que responde perguntas de programação!

# O que o programa deve fazer:

# - Pedir que o usuário digite um assunto da programação, pode já colocar na pergunta;
# - Verificar qual assunto foi digitado;
# - Exibir uma resposta personalizada com base no tema;
# - Caso o tema não esteja previsto, o Oráculo responde que ainda está aprendendo.

assunto = input("Digite um assunto da programação [python, js, java, c#]: \n")

match assunto:
  case "python":
    print("Python é uma das linguagens de programação mais populares e versáteis da atualidade, conhecida por sua simplicidade e legibilidade")
  case "js":
    print("JavaScript (JS) é uma das linguagens de programação mais fundamentais e onipresentes no cenário atual da web e do desenvolvimento de software")
  case "java":
    print("Java é uma linguagem de programação de alto nível, orientada a objetos, baseada em classes e projetada para ter o mínimo de dependências de implementação possível")
  case "c#":
    print("Lançada em 2000, ela foi projetada para ser uma linguagem poderosa e versátil, combinando os melhores aspectos de linguagens como C++, Java e Visual Basic.")
  case _:
    print("Este tema ainda estou aprendendo...")