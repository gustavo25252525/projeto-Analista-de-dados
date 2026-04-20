# Manual do Utilizador: Calculadora Inteligente
Bem-vindo à sua Calculadora Inteligente! Este guia foi criado para o ajudar a navegar pelo sistema e a realizar os seus cálculos de forma rápida e intuitiva diretamente no terminal.

### 1. Como Iniciar o Programa
Para começar, abra o seu terminal Linux, navegue até à pasta onde os ficheiros estão guardados e execute o comando de automação:

`` Bash
    sudo ./calculadora.sh ``
Nota: Logo no início, o sistema pedirá o seu nome. Digite-o e prima Enter para iniciar uma sessão personalizada.

### 2. Navegação Inteligente (Dica de Ouro) 💡
O sistema foi concebido para se adaptar à sua forma de escrever. Quando o menu apresentar as opções, não precisa de ficar preso apenas aos números. Pode escolher escrevendo:

O Número: 1, 2, 3...

O Nome: soma, subtração, direta, sair (o sistema aceita maiúsculas ou minúsculas).

O Símbolo: No caso da calculadora simples, pode usar `+`, -, /, *.

### 3. Usar a Calculadora Simples
Ao escolher a opção 1 no menu inicial, entrará no modo de cálculos aritméticos básicos.

Passo a passo:
Escolha a operação: O ecrã mostrará as opções: Soma, Subtração, Divisão, Potência e Multiplicação.

Insira os valores:

O sistema pedirá o num1 (primeiro número). Digite e prima Enter.

Depois, pedirá o num2 (segundo número).

Resultado: O ecrã exibirá a equação completa e o resultado final.

Repetir: Para fazer outra conta, basta selecionar uma nova operação.

### 4. Usar a Calculadora de Proporção (Regra de Três)
Para resolver problemas de proporcionalidade, escolha a opção 2 no menu principal.

Passo a passo:
Escolha o Tipo de Proporção:

#### 1 - Direta: Use se as grandezas aumentam juntas. (Ex: Se 2L de tinta pintam 10m², quantos litros pintam 20m²?)

#### 2 - Inversa: Use se quando uma grandeza aumenta, a outra diminui. (Ex: Se 2 trabalhadores demoram 10h, quanto tempo demoram 4 trabalhadores?)

Preencha a Estrutura (A, B e C):
O sistema utiliza a lógica: "Se [A] está para [B], assim como [C] está para [X]". Insira os valores conforme solicitado.

Resultado: O sistema calcula automaticamente o valor de X e exibe a lógica utilizada.

### 5. Consultar o Histórico 
Esqueceu-se do resultado de um cálculo anterior? O sistema guarda a memória da sua sessão!

No menu de operações, escolha a opção Histórico (ou o número 6).

O sistema listará todas as equações e resultados calculados desde que iniciou o programa, de forma organizada e numerada.

### 6. Como Sair
Para encerrar o programa de forma segura e voltar ao terminal:

Digite ` Sair` ou selecione a opção numérica correspondente em qualquer um dos menus principais.

Atenção: Ao sair, o histórico da sessão será limpo.

---

## Como Executar o Projeto

Para facilitar o uso, o projeto conta com um script de automação Shell (`.sh`) que prepara o ambiente Linux para você.

### 1. Preparação
Certifique-se de que o arquivo `calculadora.sh` e o `calculadora.py` estão na mesma pasta (ou ajuste o caminho no script `.sh`).

### 2. Permissões de Execução
No terminal, dê permissão para o script rodar:
```bash
chmod +x calculadora.sh
