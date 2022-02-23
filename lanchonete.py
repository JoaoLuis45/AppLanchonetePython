import PySimpleGUI as sg
from miau import *

def TelaLogin():
    sg.theme('LightBrown')
    layout = [
        [sg.Text('Nome')],
        [sg.Input('',key='nome')],
        [sg.Text('Senha')],
        [sg.Input('',password_char='*',key='senha')],
        [sg.Button('Entrar',key='entrar'),sg.Button('Sair',key='Sair')],
        [sg.Text('Não tem cadastro? '),sg.Button('Cadastro',key='cadastro')]
    ]

    return sg.Window('Lanchonete SIGMA',layout=layout,finalize=True)


def TelaCadastro():
    sg.theme('DarkBrown')
    layout = [
        [sg.Text('Nome'),sg.Input('',key='nomec')],
        [sg.Text('Senha'),sg.Input('',password_char='*',key='senhac')],
        [sg.Button('Cadastrar',key='cadastrar'),sg.Button('Voltar',key='voltar')]
    ]
    return sg.Window('Tela de Cadastro',layout=layout,finalize=True)


def TelaLanchonete():
    sg.theme('LightBrown')
    pedidolanche = [
        [sg.Text('Escolha o lanche:')],
        [sg.Checkbox('Hamburguer',key='hamburguer'),sg.Checkbox('Pizza',key='pizza'),sg.Checkbox('Biscoito',key='biscoito')]
    ]
    pedidobebida = [
        [sg.Text('Escolha a bebida:')],
        [sg.Checkbox('Refrigerante',key='refri'),sg.Checkbox('Suco',key='suco'),sg.Checkbox('MilkShake',key='milkshake')]
    ]
    pagamento = [
        [sg.Text('Escolha a forma de pagamento:')],
        [sg.Radio('Dinheiro','pagamento'),sg.Radio('Cartão','pagamento')],
        [sg.Button('Enviar',key='enviar')]
    ]
    pag = [
        []
    ]

    layout = [
        [sg.Frame('Lanche',layout=pedidolanche)],
        [sg.Frame('Bebida',layout=pedidobebida)],
        [sg.Button('Pronto',key='pronto')],
        [sg.Frame('',layout=pag,key='pag')]
    ]
    return sg.Window('Tela lanchonete',layout=layout,finalize=True)


def ChamarApp():
    janela,janelacadastro,janelalanchonete = TelaLogin(), None, None
    if not ExisteArquivo():
        CriarArquivo()

    while True:
        lista = LerArquivo()
        window, event, values = sg.read_all_windows()
        #TELA LOGIN
        if window == janela and event == sg.WINDOW_CLOSED:
            break
        elif window == janela and event == 'Sair':
            exit()
        elif window == janela and event == 'entrar':
            login = values['nome'] + ';' + values['senha'] + '\n'
            if login in lista:
                sg.popup(f'Bem vindo {values["nome"]}')
                nome = values['nome']
                janela.hide()
                janelalanchonete = TelaLanchonete()
            else:
                sg.popup('Usuário ou senha incorretos!')
        elif window == janela and event == 'cadastro':
            janela.hide()
            janelacadastro = TelaCadastro()

        #TELA CADASTRO
        if window == janelacadastro and event == sg.WINDOW_CLOSED:
            break
        elif window == janelacadastro and event == 'cadastrar':
            EscreverArquivo(values['nomec'],values['senhac'])
        elif window == janelacadastro and event == 'voltar':
            janelacadastro.hide()
            janela.un_hide()

        #TELA LANCHONETE
        if window == janelalanchonete and event == sg.WINDOW_CLOSED:
            break
        elif window == janelalanchonete and event == 'pronto':
            janelalanchonete.extend_layout(janelalanchonete['pag'],[
        [sg.Text('Escolha a forma de pagamento:')],
        [sg.Radio('Dinheiro','pagamento',key='dinheiro'),sg.Radio('Cartão','pagamento',key='cartao')],
        [sg.Button('Enviar',key='enviar')]
    ])
        elif window == janelalanchonete and event == 'enviar':
            pediu = []
            if values['hamburguer'] == True:
                hamburguer = 'hamburguer'
                pediu.append(hamburguer)
            if values['pizza'] == True:
                pizza = 'pizza'
                pediu.append(pizza)
            if values['biscoito'] == True:
                biscoito = 'biscoito'
                pediu.append(biscoito)
            if values['refri'] == True:
                refri = 'refrigerante'
                pediu.append(refri)
            if values['suco'] == True:
                suco = 'suco'
                pediu.append(suco)
            if values['milkshake'] == True:
                milkshake = 'milkshake'
                pediu.append(milkshake)
            if values['dinheiro'] == True:
                dinheiro = 'dinheiro'
                pediu.append(dinheiro)
            if values['cartao'] == True:
                cartao = 'cartao'
                pediu.append(cartao)
            sg.popup(f'Nota de {nome}: {pediu}')








ChamarApp()