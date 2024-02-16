# Conexão do Python com o MySQL

!["Imagem Python com MySQL"](https://www.learntek.org/blog/wp-content/uploads/2019/06/Mysql-python.png)

## Drive de comunicação com o mysql
Para estabelecer a comunicação entre o Python e o banco de dados MySQL, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#description"> https://pypi.org/project/mysql-connector-python/#description </a>

### Comando para instalar o drive
```python
    python -m pip install mysql-connector-python
```

### Configuração do banco de dados MySQL
O nosso banco de dados está em um container de docker. Para acessá-lo será necessário criar o container, então faremos os seguintes comandos em um servidor Fedora com o docker instalado:

#### Criação do volume
```shell
mkdir dadosclientes
```

#### Criação do container
<center>
<img src = "https://cdn.iconscout.com/icon/free/png-256/free-docker-226091.png" height = "100" width = "100">
</center>

```shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```

### Criação do banco de dados e da tabela clientes
```sql
CREATE DATABASE banco;
USE banco;
CREATE TABLE clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)
```

#### Arquivo clientes.py

```python
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

```