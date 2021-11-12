import psutil as ps

def listar_processos():
    """Lista os processos e retorna:\n
    [nome, pid]"""
    processos = geral = []
    for proc in ps.process_iter():
        info = proc.as_dict(attrs=['pid', 'name']) #seleciona os parametros de cada processo
        processos.append([info['name'], info['pid']]) #atribui a uma lista
    processos.insert(0, len(processos))
    return geral

def dados_memoria():
    """Retorna informacoes sobre a memoria:\n
    [geral, percentual_usado, percentual_livre]"""
    geral = dict(ps.virtual_memory()._asdict()) #obtem dados gerais da memoria
    percentual_usado = ps.virtual_memory().percent # % usado da memoria
    percentual_livre = ps.virtual_memory().available * 100 / ps.virtual_memory().total #memoria livre
    memoria = [geral, "{:.2f}".format(percentual_usado), "{:.2f}".format(percentual_livre)]
    return memoria

def dados_cpu():
    """Retorna o percentual usado de CPU"""
    carga_cpu = ps.cpu_percent(interval=1) #percentual de CPU usado no intervalo de 1 seg
    return carga_cpu