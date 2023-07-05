contatos = {

    "gui@pop.com": {"nome": "aldeneida", "telefone": "98765-4321"},
    "seumadruga@sbt.com": {"nome": "madruga", "telefone": "98765-5555"}

    }

contatos.clear() #apaga o dicionario
copia = contatinhos.copy() #copia o dicionário
dict.fromkeys(["nome", "telefone"]) #Cria o dicinário com um valor none
contatos.get("chave") #pesquisa pelo objeto chave, porém se não achar retorna none
contatos.get("chave", {}) #se não achar o objeto pesquisado retorna um dicionário vazio
contatos.itens() #retorna uma lista de tuplas, bom para iterar junto com o for
contatos.keys() #retorna as chaves do dicionario
contatos.pop() #remove uma chave do dicionário
contatos.pop("gui@pop.com", {}) #remove e retorna o valor add entre as chaves
contatos.popitem() #remove os itens na sequência
contatos.setdefault("nome", "Giovana") #add um valor ao dicionário caso ele não exista, caso o valor exista ele será exibido.
contatos.update({"gui@pop.com": {"nome", "guilherme"}}) #atualiza um dicionário com outro
contatos.values() #retorna os valores dos dicionário sem a chave
resultado = "gui@pop.com" in contatos #verifica se a chave existe dentro do dicionario
del contatos["gui@pop.com"]["telefone"] #remove o item telefone do dicionário
del contatos["gui@pop.com"] #remove toda a chave e seus respectivos itens
del contatos #apaga todo o dicionário


