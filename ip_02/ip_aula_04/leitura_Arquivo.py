# with open('C:/Users/marci/OneDrive/Documentos/GitHub/MBA-Software-Developer/ip_02/ip_aula_04/arquivo.txt', 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open('C:/Users/marci/OneDrive/Documentos/GitHub/MBA-Software-Developer/ip_02/ip_aula_04/pg1232.txt', 'r', encoding='utf-8') as livro:
#   for linha in livro:
#       print(linha.rstrip())  # rstrip() remove espaços em branco no final da linha


with open('C:/Users/marci/OneDrive/Documentos/GitHub/MBA-Software-Developer/ip_02/ip_aula_04/pg1232.txt', 'r', encoding='utf-8') as livro:
    linhas = livro.readlines()

print(type(linhas))  # Verifica o tipo de 'linhas'
print(linhas[:5])  # Exibe as primeiras 5 linhas do arquivo