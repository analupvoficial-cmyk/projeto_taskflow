# importe de biblioteca (instalar no terminal)
from flask import Flask, render_template, request

# criar objeto flask "apelido - app"
app = Flask(__name__)

# base de dados fake
base_fake = []

# rotas
# toda rota é acompanhada de uma função (def)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atividades/criar', methods=['GET','POST'])
def criar_atividade():
    if request.method == 'POST':
        # aqui recebe dados do formulário
        nome_atividade = request.form.get('form_nome')
        data_atividade = request.form.get('form_data')
        tipo_atividade = request.form.getlist('form_tipo')

        dados = {
            'nome': nome_atividade,
            'data': data_atividade,
            'tipo': tipo_atividade
        }
        print(f'dados: {dados}')
        base_fake.append(dados)
        print(f'base_fake: {base_fake}')
        return render_template('criar_atividade.html', dados_atividade=base_fake)

    return render_template('criar_atividade.html')

@app.route('/atividades_listar')
def listar_atividades():
    return render_template('listar_atividades.html', dados_atividade=base_fake)

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

# --- NOVAS ROTAS ADICIONADAS PARA CORRIGIR O ERRO ---
@app.route('/tipos')
def tipo():
    return render_template('tipo.html')

@app.route('/recursos')
def recurso():
    return render_template('recurso.html')


@app.route('/tipo/novo')
def criar_tipo():
    return render_template('criar_tipo.html')
# ----------------------------------------------------

# iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
# nada deve ser colocado abaixo