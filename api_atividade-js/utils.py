from models import Pessoas

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


# Ponto de entrada do script
if __name__ == '__main__':
    #insere_pessoas()  # Inserir uma pessoa
    #altera_pessoas()
    #excluir_pessoas()
    consulta_pessoas()        # Consultar todas as pessoas

