from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Santos', idade=26)
    print(pessoa)
    pessoa.save()

# Função para consultar todas as pessoas no banco de dados
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='José').first()
    print(pessoa.nome, pessoa.idade)
    #print(pessoa.nome)

# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Jorge').first()
    #pessoa.idade = 30
    pessoa.nome = 'José'
    pessoa.save

# Exclui dados na tabela pessoa
def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Santos').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consultar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


# Ponto de entrada do script
if __name__ == '__main__':
    insere_usuario('jorge', '1234')
    insere_usuario('Santos', '4321')
    consultar_usuarios()
    #insere_pessoas()  # Inserir uma pessoa
    #altera_pessoas()
    #excluir_pessoas()
    #consulta_pessoas()        # Consultar todas as pessoas

