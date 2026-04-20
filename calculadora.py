import time

historico=[]
Operadores = {
  'Soma':{
      'Formula':'num1 + num2',
      'legenda': '\nVocê acabou de escolher a soma!\n'
  },
  'Subtração':{
      'Formula':'num1 - num2',
      'legenda': '\nVocê acabou de escolher a Subtração!\n'
  },
  'Divisão': {
      'Formula':'num1/num2',
      'legenda': '\nVocê acabou de escolher a Divisão!\n'
  },

  'Potencia': {
      'Formula':'num1^num2',
      'legenda': '\nVocê acabou de escolher a Potencia!\n'
  },
  'Multiplicacao':{
      'Formula':'num1 X num2',
      'legenda': '\nVocê acabou de escolher a Multiplicação!\n'
  },
  'Historico':{

      'legenda': '\nVocê gostaria de ver o seu histórico, aqui está!\n'
}
}
print('Bem vindo a sua calculadora inteligente!\nPara começarmos digite como você gostaria de ser chamado.\n')

User_Name = input('Digite o seu nome aqui: ')

print(f'\nMuito bem {User_Name}, agora podemos começar!\nAntes de qualquer coisa preciso que entenda como funciona o nosso prompt!\nO sistema foi montado para que as suas respostas na hora de escolher uma opção, você tenha a liberdade de escolher pelo numero da opção, nome da opção ou no caso da calculadora simples pelo seu operador.\nSabendo disso, tenha um bom proveito!\n')


Escolha_Cal = input('\nAqui está as suas calculadoras:\n\n1- Calculadora Simples\n2- Calculadora de proporção\n\nDigite a sua escolha: ').upper()

if Escolha_Cal in ['1', 'CALCULADORA SIMPLES', 'SIMPLES']:
    while True:
        num = []

        Operador = input('\nAgora escolha a operação\n\n1- Soma\n2- Subtração\n3- Divisão\n4- Potência\n5- Multiplicação\n6- Histórico\n7- Sair\nDigite a operação: ').upper()

        if Operador in ['1', 'SOMA']:
            print(Operadores['Soma']['legenda'])
            for i in range(2):
                numero = float(input(f'Digite o {i+1}º número: '))
                num.append(numero)

            formula = Operadores['Soma']['Formula']
            resultado = num[0] + num[1]
            formula_preparada = formula.replace("num1", str(num[0])).replace("num2", str(num[1]))

            print(f'\nResultado: {formula_preparada} = {resultado}')
            historico.append(f'{User_Name}: {formula_preparada} = {resultado}')

        elif Operador in ['2', 'SUBTRAÇÃO', 'SUBTRACAO']:
            print(Operadores['Subtração']['legenda'])
            for i in range(2):
                numero = float(input(f'Digite o {i+1}º número: '))
                num.append(numero)

            formula = Operadores['Subtração']['Formula']
            resultado = num[0] - num[1]
            formula_preparada = formula.replace("num1", str(num[0])).replace("num2", str(num[1]))

            print(f'\nResultado: {formula_preparada} = {resultado}')
            historico.append(f'{User_Name}: {formula_preparada} = {resultado}')

        elif Operador in ['3', 'DIVISÃO', 'DIVISAO']:
            print(Operadores['Divisão']['legenda'])
            for i in range(2):
                numero = float(input(f'Digite o {i+1}º número: '))
                num.append(numero)

            formula = Operadores['Divisão']['Formula']
            resultado = num[0] / num[1]
            formula_preparada = formula.replace("num1", str(num[0])).replace("num2", str(num[1]))

            print(f'\nResultado: {formula_preparada} = {resultado}')
            historico.append(f'{User_Name}: {formula_preparada} = {resultado}')

        elif Operador in ['4', 'POTÊNCIA', 'POTENCIA']:
            print(Operadores['Potencia']['legenda'])
            for i in range(2):
                numero = float(input(f'Digite o {i+1}º número: '))
                num.append(numero)

            formula = Operadores['Potencia']['Formula']
            resultado = num[0] ** num[1]
            formula_preparada = formula.replace("num1", str(num[0])).replace("num2", str(num[1]))

            print(f'\nResultado: {formula_preparada} = {resultado}')
            historico.append(f'{User_Name}: {formula_preparada} = {resultado}')

        elif Operador in ['5', 'MULTIPLICAÇÃO', 'MULTIPLICACAO']:
            print(Operadores['Multiplicacao']['legenda'])
            for i in range(2):
                numero = float(input(f'Digite o {i+1}º número: '))
                num.append(numero)

            formula = Operadores['Multiplicacao']['Formula']
            resultado = num[0] * num[1]
            formula_preparada = formula.replace("num1", str(num[0])).replace("num2", str(num[1]))

            print(f'\nResultado: {formula_preparada} = {resultado}')
            historico.append(f'{User_Name}: {formula_preparada} = {resultado}')

        elif Operador in ['6', 'HISTÓRICO', 'HISTORICO']:
            print(Operadores['Historico']['legenda'])

            if not historico:
                print('Você ainda não possui histórico.')
                continue
            for indice, registro in enumerate(historico):
                print(f'{indice + 1}º Histórico: {registro}')

        elif Operador in ['7','SAIR']:
            print('\nVocê saiu da calculadora simples!')
            break

        else:
            print('\nSua opção foi inválida. Tente novamente.')


elif Escolha_Cal in ['2', 'PROPORÇÃO', 'PROPORCAO', 'CALCULADORA DE PROPORÇÃO']:

    print('\nVocê está na Calculadora de Proporção (Regra de Três)!')
    print('Se quiser voltar, é só escolher a opção de Sair.')

    while True:
        print('\nEscolha o tipo de proporção:')
        print('1- Direta (Ex: Mais litros de tinta = Mais metros pintados)\n2- Inversa (Ex: Mais pedreiros = Menos tempo de obra)\n2- Inversa (Ex: Mais pedreiros = Menos tempo de obra)\n3- Sair\n')



        Tipo_Prop = input('Digite a opção: ').upper()

        if Tipo_Prop in ['3', 'SAIR']:
            print('\nVocê saiu da calculadora de proporção!')
            break

        elif Tipo_Prop in ['1', 'DIRETA', '2', 'INVERSA']:
            print('\nVamos montar a estrutura:')
            print('Se [A] está para [B], assim como [C] está para [X]')

            a = float(input('Digite o valor de A: '))
            b = float(input('Digite o valor de B: '))
            c = float(input('Digite o valor de C: '))


            if a == 0 or c == 0:
                print('\nErro Matemático: Os valores base não podem ser zero!')
                continue


            if Tipo_Prop in ['1', 'DIRETA']:
                x = (b * c) / a
                formula_str = f'({b} * {c}) / {a}'
                nome_prop = 'Direta'


            else:
                x = (a * b) / c
                formula_str = f'({a} * {b}) / {c}'
                nome_prop = 'Inversa'

            print(f'\nResultado da Proporção {nome_prop}: X = {x}')


            historico.append(f'{User_Name} (Prop. {nome_prop}): {formula_str} = {x}')

        else:
            print('\nOpção inválida. Tente novamente.')
else:
    print('\nCalculadora não encontrada ou em desenvolvimento!')










