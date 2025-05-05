import sqlite3
from pathlib import Path

# Definindo o diretório raiz do projeto (onde este arquivo está)
ROOT_DIR = Path(__file__).parent

# Nome e caminho do arquivo de banco de dados
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

# Nome da tabela que será usada no CRUD
TABLE_NAME = 'customers'

# =============================================
# 1) Conexão com o banco de dados
# =============================================
# Abre (ou cria) o arquivo de banco SQLite na rota especificada
connection = sqlite3.connect(DB_FILE)
# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

# =============================================
# 2) Criação da tabela (caso ainda não exista)
# =============================================
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'weight REAL'
    ')'
)
# Persiste a criação da tabela no banco
connection.commit()

# =============================================
# 3) Operação CREATE (INSERT)
# =============================================
# SQL parametrizado para inserir novos registros
sql_insert = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso) '
)
# Insere um registro único
cursor.execute(sql_insert, {'nome': 'Sem nome', 'peso': 3})
connection.commit()

# Insere múltiplos registros de uma só vez
cursor.executemany(sql_insert, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))
connection.commit()

# =============================================
# 4) Operação DELETE
# =============================================
# Remove registros com nome igual a "Maria"
cursor.execute(
    f'DELETE FROM {TABLE_NAME} WHERE name = :nome',
    {'nome': 'Maria'}
)
# Confirma a exclusão
connection.commit()

# =============================================
# 5) Operação READ (SELECT)
# =============================================
# Executa uma consulta para listar todos os registros
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)
# O SELECT retorna linhas, então usamos fetchall() para capturar tudo
for row in cursor.fetchall():
    _id, name, weight = row
    # Printar cada registro (id, nome, peso)
    print(_id, name, weight)

# =============================================
# 6) Operação UPDATE
# =============================================
# Altera o nome e peso do registro com id = 9
cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name = :novo_nome, weight = :novo_peso '
    'WHERE id = :id',
    {'novo_nome': 'Davi', 'novo_peso': 80.00, 'id': 9}
)
# Persiste a atualização
connection.commit()

# =============================================
# 7) Leitura após UPDATE
# =============================================
# Novamente, listamos todos os registros para ver a alteração
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# =============================================
# 8) Fechamento da conexão
# =============================================
# Fecha o cursor e a conexão para liberar recursos\cursor.close()
connection.close()
