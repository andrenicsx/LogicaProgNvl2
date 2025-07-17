# 4. **Meu crachá de programador(a)**
# Peça o nome, idade, linguagem favorita e um emoji que representa a pessoa. 
# Depois, mostre tudo formatado como se fosse um crachá de evento tech.

# O que o programa deve fazer:

# - Pedir o nome e todas as outras informações da pessoa com `input()`;
# - Exibir essas informações de forma organizada, com um “título” e moldura visual;

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
linguagem = input("Informe sua linguagem de programação favorita: ")

print("---------------")
print("\nCrachá DEV\n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Linguagem de programação: {linguagem}")
print("\n---------------")