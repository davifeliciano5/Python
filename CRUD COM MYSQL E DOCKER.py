# -*- coding: utf-8 -*-
"""
CRUD em MySQL usando PyMySQL

Este script demonstrativo organiza e documenta operações básicas de CRUD
no MySQL, utilizando diferentes tipos de cursores (cursors) disponíveis
no PyMySQL.

Tipos de cursores disponíveis:
- **Cursor**: retorna resultados como tuplas padrão (acesso por índice numérico). Ideal para conjuntos pequenos e quando desempenho é prioridade.
- **DictCursor**: retorna resultados como dicionários (chave-valor), onde cada coluna vira uma chave. Facilita a leitura e evite erros de índice de coluna.
- **SSCursor (Server-Side Cursor)**: streaming cursor que busca registros gradualmente do servidor, útil para conjuntos de dados muito grandes sem sobrecarregar a memória local.
- **SSDictCursor**: combinação de SSCursor com dicionários, unindo streaming a acesso por nome de coluna.

Como usar um cursor específico:
- Informe o parâmetro `cursorclass` no `connect()` (e.g., `cursorclass=DictCursor`).
- Use context managers (`with connection.cursor()`) para garantir fechamento automático ao final do bloco.

"""
import pymysql
from pathlib import Path
from typing import cast
import pymysql.cursors

# Configurações iniciais ------------------------------------------------------
CURRENT_CURSOR = pymysql.cursors.DictCursor  # Pode trocar para Cursor, SSCursor, SSDictCursor conforme necessidade
DB_HOST    = 'localhost'
DB_USER    = 'usuario'
DB_PASS    = 'senha'
DB_NAME    = 'base_de_dados'
TABLE_NAME = 'customers'

# ----------------------------------------------------------------------------
# 1) Conexão e estabelecimento do cursor
# ----------------------------------------------------------------------------
connection = pymysql.connect(
    host       = DB_HOST,
    user       = DB_USER,
    password   = DB_PASS,
    database   = DB_NAME,
    cursorclass= CURRENT_CURSOR
)

# ----------------------------------------------------------------------------
# 2) Criação da tabela e limpeza (TRUNCATE)
# ----------------------------------------------------------------------------
with connection:
    with connection.cursor() as cursor:
        # Cria a tabela caso não exista
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            '  id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # Remove todos os registros para iniciar do zero
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

# ----------------------------------------------------------------------------
# 3) Inserções (INSERT)
# ----------------------------------------------------------------------------
with connection:
    # Inserção simples via parâmetros posicionais (%s)
    with connection.cursor() as cursor:
        sql = f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'
        cursor.execute(sql, ("Ivi", 50))
        cursor.execute(sql, ("Tonhão", 38))
    connection.commit()

    # Inserção usando placeholders nomeados
    with connection.cursor() as cursor:
        sql_named = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%(name)s, %(age)s)'
        )
        cursor.execute(sql_named, {"name": "Carlinhos", "age": 25})
    connection.commit()

    # Inserção em lote (executemany)
    with connection.cursor() as cursor:
        batch = [
            {"name": "Davi",   "age": 16},
            {"name": "Marta",  "age": 43},
            {"name": "João",   "age": 50}
        ]
        cursor.executemany(sql_named, batch)
    connection.commit()

# ----------------------------------------------------------------------------
# 4) Leitura de dados (SELECT)
# ----------------------------------------------------------------------------
with connection.cursor() as cursor:
    # Consulta entre dois IDs (exemplo de uso de placeholders posicionais)
    min_id, max_id = 3, 5
    sql_select = (
        f'SELECT * FROM {TABLE_NAME} '
        'WHERE id BETWEEN %s AND %s'
    )
    cursor.execute(sql_select, (min_id, max_id))
    results = cursor.fetchall()  # Retorna lista de dicionários quando usando DictCursor
    # Itera e imprime cada linha
    for row in results:
        print(row)

# ----------------------------------------------------------------------------
# 5) Deleção de registros (DELETE)
# ----------------------------------------------------------------------------
with connection.cursor() as cursor:
    sql_delete = f'DELETE FROM {TABLE_NAME} WHERE id = %s'
    cursor.execute(sql_delete, (1,))
    # .rowcount mostra quantas linhas foram afetadas
    print("Rows deleted:", cursor.rowcount)
    connection.commit()

# ----------------------------------------------------------------------------
# 6) Atualização de dados (UPDATE)
# ----------------------------------------------------------------------------
with connection.cursor() as raw_cursor:
    cursor = cast(CURRENT_CURSOR, raw_cursor)
    sql_update = (
        f'UPDATE {TABLE_NAME} '
        'SET nome = %s, idade = %s '
        'WHERE id = %s'
    )
    cursor.execute(sql_update, ('Eleonor', 12, 4))
    connection.commit()

    # Pega o último id alterado
    last_id = cursor.lastrowid
    print("Last inserted/updated ID:", last_id)

# ----------------------------------------------------------------------------
# 7) Métodos úteis de cursor e scroll
# ----------------------------------------------------------------------------
# - cursor.lastrowid : ID da última inserção/atualização
# - cursor.rowcount  : número de linhas afetadas
# - cursor.rownumber : índice da linha atual no conjunto de resultados (após fetch)
# - fetchone(), fetchmany(n), fetchall() para recuperação de dados
# - cursor.scroll(value, mode) para reposicionar o ponteiro de leitura:
#     * mode='absolute': move para a linha de índice exato (value)
#     * mode='relative': move 'value' linhas a partir da posição atual

# Exemplo de uso de scroll:
# cursor.execute('SELECT * FROM customers')
# cursor.scroll(0, 'absolute')  # volta ao início do conjunto de resultados

# ----------------------------------------------------------------------------
# 8) Fechamento da conexão
# ----------------------------------------------------------------------------
connection.close()  # Garante o encerramento da conexão com o banco
