# method - self, método de instância
# @classmethod - cls, método de instância
# @staticmethod - método estático (X self, X cls)
"""
🔁 def método(self, ...) — Método de Instância
Recebe o objeto criado como primeiro argumento (self).

Pode acessar e modificar atributos da instância.


def set_user(self, user):
    self.user = user
💡 Quando usar: quando você quer que o método dependa dos dados daquele objeto específico.
➡️ No seu exemplo: set_user() e set_password() modificam diretamente os atributos da instância.




🧪 @classmethod — Método de Classe
Recebe a classe como primeiro argumento (cls), não a instância.

Pode ser usado para criar ou configurar objetos de forma alternativa.

Muito usado como "fábrica de objetos" (factory method).

@classmethod
def creat_whit_auth(cls, user, password):
    connection = cls()  # chama o __init__
    connection.user = user
    connection.password = password
    return connection
💡 Quando usar: quando você quer criar uma instância, mas talvez com um conjunto diferente de parâmetros, lógica, ou configuração extra.
➡️ creat_whit_auth() (pequeno typo, deveria ser create_with_auth) cria um connection já com user e password.




🔇 @staticmethod — Método Estático
Não recebe self nem cls.

Não depende de nada da instância nem da classe.

Funciona como uma função "normal", mas fica dentro da classe por organização semântica.

@staticmethod
def log(msg):
    print("LOG:", msg)
💡 Quando usar: quando a função faz sentido dentro da classe, mas não precisa acessar a instância nem a classe.
➡️ log() só imprime uma mensagem, então não precisa de nada da classe connection.


🧠 Comparando os 3:
Tipo	Primeiro parâmetro	Acessa self?	Acessa cls?	Usado para...
Instância	self	✅	❌	Modificar/usar atributos do objeto
Classe	cls	❌	✅	Criar/configurar novas instâncias
Estático	nenhum	❌	❌	Função utilitária sem dependência
"""
class connection:
    def __init__(self, host='localhost'):
        self.localhost = host
        self.user = None
        self.password = None

    def set_user(self,user):
        self.user = user
    
    def set_password(self,password):
        self.password = password

    @classmethod
    def creat_whit_auth(cls,user,password):
        connection = cls()
        connection.user = user
        connection.password = password
        
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG: ', msg)

c1 = connection('312321')
c1.set_user('Davi')
c1.set_password('123')
print(vars(c1))

c2 = connection.creat_whit_auth('tabata','123')
print(vars(c2))

connection.log("é os guri")