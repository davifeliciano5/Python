from pathlib import Path
from abc import ABC, abstractmethod,ABCMeta


LOG_FILE = Path(__file__).parent / '_log.txt'

class Log(metaclass=ABCMeta ):
    @abstractmethod # está é uma classe abstrata(contrato) toda filha de Log deve-
    # rá implementar está classe
    def _log(self,msg):
        ...
        
    
    def log_error(self,msg):
        return self._log(f'Erro: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    


class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_success('oi é pra ser sucesso')
    lp.log_error('é pra ser um erro')

    lf = LogFileMixin()
    lf.log_success("Escrevendo um success em json")
    lf.log_error("Escrevendo um ERRO em json")