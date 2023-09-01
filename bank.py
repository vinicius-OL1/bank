from conta import cont
import random 
import requests     
import json

def cadastro (pessoa):
    pessoa ['nome'] = str(input("digite seu nome para cadastro: "))
    pessoa ['nasc'] = int(input("digite sua idade: "))
    while True:
        pessoa ['sexo'] = str (input("selecione seu sexo [M/F]: ")).upper()
        if pessoa['sexo'] == 'M' or 'F':
            break
        else:
            print('porfavor selecione uma opção valida!!!')
    pessoa ['email'] = str (input('digite seu email para cadastro: '))
    

link = ("https://test-1e58c-default-rtdb.firebaseio.com")
menu = '''
BEM VINDO AO BANK O BANCO NUMERO 1!

SELECIONE UMA DAS OPÇÔES ABAIXO:

[1]*CADASTRO
[2]**USUARIO
[3]***DEPOSITO
[4]****SAQUE
[5]*****TRANSFERENCIA
[6]****** SAIR
[7]*******ENTRAR vasco
'''
contador = 0
usuario = dict()
usuario['saldo'] = 0
id = ''
id_prop = ''
while True:
    print (menu)
    while True:
        conta = random.randint(0,1000)
        if cont(conta) == True:
            print (f'sua conta é {conta}')
            usuario['conta'] = conta
            break
        else:
            conta = random.randint(0,1000000)
    opcao = int (input ('selecione uma das opões acima listadas: '))
    if opcao == 1:
        cadastro (usuario)
        nome = usuario['nome']
        idade = usuario['nasc']
        sexo = usuario['sexo']
        email = usuario['email']
        saldo = usuario['saldo']
        informações = {'info':{'nome':nome,'idade':idade,'sexo':sexo,'email':email,'conta': conta, 'saldo':saldo}}
        requisicao = requests.post(f"{link}/usuarios/.json",data =json.dumps(informações))
        print (requisicao)
        print (nome)
    elif opcao == 2:
        print (usuario)
    elif opcao == 3:
        saldo = 0
        valor = int (input('digite o valor que gostaria de depositar: '))
        contadest = (str(input('digite o nome do proprietario da conta: ')))
        deposito = lambda saldo, n: saldo + n
        usuario['saldo'] += deposito(saldo, valor)
        print(f"seu saldo atual é de R${usuario['saldo']}")
    
        deposit = valor
        informações = {'deposito':deposit}
        requisicao2 = requests.get(f'{link}/usuarios/.json')
        dic_req = requisicao2.json()
        for id_usi in dic_req:
            id = id_usi
            if contadest == (dic_req[id_usi]['info']['nome']):
                saldo_temp = dic_req[id_usi]['info']['saldo']
                saldo_temp += valor
                
                info2 = {'saldo':saldo_temp}

                print ('destinario encontrado')
                id_prop = id 
                print(id_prop)
                print (requisicao2)
                requisicao2 = requests.patch(f"{link}/usuarios/{id_prop}/info/.json",data =json.dumps(info2))
                
    elif opcao == 6:
        break
    elif opcao == 4 :
        saldo = usuario['saldo']
        valor = float (input('digite o valor que deseja sacar LIM[R$500] por dia: '))
        dest = str (input('digite o nome do proprietario da conta: '))
        saque = lambda saldo, n: saldo - n
        usuario['saldo'] = saque(saldo,valor)
        requisicao2 = requests.get(f'{link}/usuarios/.json')
        dic_req = requisicao2.json()
        for id_usi in dic_req:
            id = id_usi
            if dest == (dic_req[id_usi]['info']['nome']):
                saldo_temp = dic_req[id_usi]['info']['saldo']
                saldo_temp -= valor
                info2 = {'saldo':saldo_temp}
                print ('destinario encontrado')
                id_prop = id 
                print(id_prop)
                print (requisicao2)
                requisicao2 = requests.patch(f"{link}/usuarios/{id_prop}/info/.json",data =json.dumps(info2))
                
        
        
    elif opcao == 5:
        contas = dict()
        #saldo = usuario['saldo']
        conta_pro = int(input('digite o numero da sua conta: '))
        conta_dest = int (input('digite o numero da conta do destinatario: '))
        val = float (input('digite o valor que gostaria de transferir: '))
        #valor = float (input('digite o valor que deseja transferir: '))
        #saque = lambda saldo, n: saldo - n
        #usuario['saldo'] = saque(saldo,valor)
        #print(f"seu saldo atual é de R${usuario['saldo']}")
        requisicao2 = requests.get(f'{link}/usuarios/.json')
        dic_req = requisicao2.json()
        
        for id_usi in dic_req:
            if conta_pro == dic_req[id_usi]['info']['conta']:
                print('conta do usuario encontrada')
                print (id_usi)
                id_trans_prop = id_usi
                saldo_temp_prop = dic_req[id_usi]['info']['saldo']
                saldo_temp_prop -= val
                info2 = {'saldo':saldo_temp_prop}
                requisicao2 = requests.patch(f"{link}/usuarios/{id_trans_prop}/info/.json",data =json.dumps(info2))
        for id_usi in dic_req:
            if conta_dest == dic_req[id_usi]['info']['conta']:
                print( 'conta do destinatario encontrada')
                print (id_usi)
                id_trans_dest = id_usi
                saldo_temp_dest = dic_req[id_usi]['info']['saldo']
                saldo_temp_dest += val
                info2 = {'saldo':saldo_temp_dest}
                requisicao2 = requests.patch(f"{link}/usuarios/{id_trans_dest}/info/.json",data =json.dumps(info2))
        
        
                

                #
                #contas = dict()

                #requisicao2 = requests.get(f'{link}/usuarios/.json')
                #dic_req = requisicao2.json()
                #conta_dest = int (input('digite o numero da conta do destinatario: '))
                #if conta_dest == contas:
                  #      print ('conta encontrada')
                 #       id_trans_dest = id_usi
                 #       print (id_trans_dest)
                    
                  #  valor_trans = int(input('digite o valor que gostaria de transferir'))
                   # saldo_temp2 = valor_trans
                   # requisicao2 = requests.patch(f"{link}/usuarios/{id_prop}/info/.json",data =json.dumps(info2))
                    
               # else:
                  #  print ('conta nao consta no banco de dados')