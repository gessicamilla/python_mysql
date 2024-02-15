# Importando a biblioteca de conexão com o banco de dados mysql
# Vamos adicionar um alias a biblioteca
import mysql.connector as mc

# Vamos estabelecer a conexão com o banco de dados e para tal, iremos passar os seguintes dados:
# servidor, porta, usuário, senha, banco
conexao = mc.connect(
    host = "127.0.0.1",
    port = "3784",
    user = "root",
    password = "senac@123",
    database = "banco"
)
# Estamos testando a conexão, pedindo para exibir o id da conexão. Caso exiba uma pilha de erros, então você tem um erro na linha conexão.
print(conexao)

# Para se movimentar dentro da estrutura de banco de dados e retornar dos dados necessários, iremos criar um cursos
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor
# cursor.execute("Create Database Ola")

# cursor.execute("insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@uol.com.br','(54) 9985-6854')")

# Vamos selecionar todos os dados da tabela cliente
cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"Nome do Cliente: {c[1]}")
    print(f"E-mail: {c[2]}")