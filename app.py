from flask import Flask, render_template, request
from functions import functions as fc

app = Flask(__name__)

#registro a rota para a pagina inicial - raiz
@app.route("/")
def inicio():
    return render_template("index.html")

#registra a rota para a pagina de monitoramento
@app.route("/painel", methods=['POST', 'GET'])
def monitoramento():
    cpu = fc.dados_cpu()
    memoria = fc.dados_memoria()
    processos = fc.listar_processos()
    verificacao = verificar_limites(memoria[1], cpu, processos[0])
    dados = [cpu, memoria, processos, verificacao]
    
    return render_template("painel.html", dados=dados)

def verificar_limites(val1, val2, val3):
    limites_estourado = []
    #pega os dados passados pelo formulario
    limite_memo = request.form["memoria"]
    limite_cpu = request.form["processador"]
    limite_processos = request.form["processos"]
    #verifica se o consumo do hardware esta dentro dos limites
    if float(val1) > float(limite_memo):
        limites_estourado.append("Consumo de memória excedeu o limite.")
    if float(val2) > float(limite_cpu):
        limites_estourado.append("Consumo de processador (CPU) excedeu o limite.")
    if int(val3) > int(limite_processos):
        limites_estourado.append("Quantidade de processos excedeu o limite.")
    #Esse retorno vai para o metodo "monitoramento"
    return limites_estourado

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4142)