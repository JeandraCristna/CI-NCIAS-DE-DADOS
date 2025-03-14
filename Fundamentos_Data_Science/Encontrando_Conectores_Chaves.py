from collections import Counter
from collections import defaultdict

users = [
    { "id": 0, "name": "Jeandra"},
    { "id": 1, "name": "Alex"},
    { "id": 2, "name": "Hugo"},
    { "id": 3, "name": "Jadna"},
    { "id": 4, "name": "Karina"},
    { "id": 5, "name": "Ysa"},
    { "id": 6, "name": "Everton"},
    { "id": 7, "name": "Raquel"},
    { "id": 8, "name": "Vanja"},
    { "id": 9, "name": "Veronica"}
]

# Recebendo dados de amizades 
friendship_pairs = [(0, 1), (0,2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Inicializando (criando) o dict com uma lista vazia para cada id de usuário:
friendships = {user["id"]: [] for user in users} 

# Agora execute um loop pelos pares de amigos para preenchê-las:
for i, j in friendship_pairs:
    friendships[i].append(j) # Adiciona j como amigo do usuário i
    friendships[j].append(i) # Adiciona i como amigo do usuário j
    
#para Realizar consultas (perguntas) ao grafo, primeiro, determinamos o número total de conexões somando os tamanhos
# de todas as listas de friends
def number_of_friends(user):
    '''Quantos amigos tem o _user_?'''
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

total_connection = sum(number_of_friends(user) for user in users)

print(total_connection) #total 24 conexões    

# Dividando pelo número de usuários
num_users = len(users)                            # tamanho da lista de usuário
avg_connections = total_connection / num_users    # 24 / 10 == 2.4

print(avg_connections) 

# Agora vamos Encontrar as pessoas mais conectadas 
# Pra isso vamos coloca-los em ordem decrescente, dos que têm mais amigos para os que têm menos amigos
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users] # criando uma lista (user_id, number_of_friends)
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True) # classificando a lista por num_friends do maior para o menor
