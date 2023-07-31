import pymongo
cluster = pymongo.MongoClient("mongodb+srv://campos2512:campos2512@cluster0.vfp6e.mongodb.net/?retryWrites=true&w=majority")
db = cluster.get_database('mydatabase')
colletion = db.get_collection('mycollection')

dado = {
     'nome': 'Pedro italo Campos',
     'email' : 'Pedro@yahoo.com.br',
     'idade' : 33
 }
# # colletion.insert_one(dado)

dado2 = {
     'nome': 'Marcos Paulo',
     'email' : 'MP@gmail.com',
     'idade' : 45
 }

dado3 = {
     'nome': 'Joao Vinicius',
     'email' : 'JV@gmail.com',
     'idade' : 10,
     'cidade': 'Fortaleza',
     'estado': 'CE'
 }
dado4 = {
     'nome': 'Maria Antonia Nascimento',
     'email' : 'Antonia@gmail.com',
     'idade' : 24,
     'cidade': 'São Paulo',
     'estado': 'SP'
 }

colletion.insert_many([dado2,dado3,dado4,dado])

resultado =colletion.find({})

for dado in resultado:
    print(dado['nome'])

# resultado =colletion.find_one({'nome': 'Livia Nascimento'})

# if resultado:
#     print(resultado)
# else:
#     print('Valor invalido')

# resultado = colletion.delete_one({'nome': 'Livia Nascimento'})

# if resultado:
#     print('Usario deletado')
# else:
#     print('Nome invalido')

#colletion.delete_many({'idade' : {'$lt' : 33}})
#colletion.delete_many({})