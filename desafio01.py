



contato = {
    'id': 0,
    'nome': 'Raul Almeida',
    'telefone': 84992428678,
    'email': 'raulalmeida22@gmail.com',
    'favorito': False
}

contato2 = {
    'id': 1,
    'nome': 'Raulteste',
    'telefone': 6199228483,
    'email': 'raulalmeida@metalknight.frc',
    'favorito': False
}
contato3 = {
    'id': 2,
    'nome': '',
    'telefone': '',
    'email': '',
    'favorito': False
}


# lista de contatos
contatos = [contato,contato2]




lang =  (input("Digite a opcao desejada: "))




match lang:
    case 'adicionar':
        contato3['nome'] = input("Digite o nome: ")
        contato3['telefone'] = input("Digite o seu telefone: ")
        contato3['email'] = input("Digite o email: ")
        contato3['favorito'] = bool(input("Deseja marcar como favorito?: "))
        contatos.append(contato3)
        print(contatos)
    case 'remover':
        i = int(input("Digite a posição do contato: "))
        contatos.remove(contatos[i])
        print(contatos)
    case 'editar':
        contato3['nome'] = input("Digite o nome: ")
        contato3['telefone'] = input("Digite o seu telefone: ")
        contato3['email'] = input("Digite o email: ")
        contato3['favorito'] = bool(input("Deseja marcar como favorito?: "))
    case 'favoritar':
        contato['favorito'] = True
        print(contatos)

