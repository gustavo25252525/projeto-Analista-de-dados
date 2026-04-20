# projeto-Analista-de-dados
Repositorio para desenvolvimento de projetos relacionado a análise de dados

1. Como executar o arquivo .sh (Shell Script)
O arquivo calculadora.sh foi criado para automatizar a preparação do ambiente Linux e rodar a aplicação. Ele executa três tarefas: atualiza a lista de pacotes do sistema (apt update), garante que o Python 3 esteja instalado (apt install python3) e executa o código Python.

Para executar este arquivo no seu terminal Linux, siga os passos abaixo:

Passo 1: Ajuste o caminho do arquivo (Opcional, mas recomendado)
Verifique se o seu arquivo Python está realmente salvo no diretório /home/pratica2/. Caso o arquivo esteja na mesma pasta que o script .sh, você pode editar a última linha do calculadora.sh para:
python3 calculadora.py

Passo 2: Conceda permissão de execução
Antes de rodar um script no Linux, você precisa dar a ele a permissão de execução usando o comando de permissões. No terminal, navegue até a pasta onde o arquivo está e digite:

Bash
chmod +x calculadora.sh
Passo 3: Execute o script
Como o script utiliza o comando sudo para instalar pacotes, você precisará executá-lo com privilégios de administrador. Execute:

Bash
sudo ./calculadora.sh
(O terminal pedirá a sua senha de usuário para confirmar a instalação dos pacotes).

2. Estrutura e Explicação do Código Python (calculadora.py)
O script em Python é o coração do projeto. Ele foi estruturado para ser interativo e amigável, permitindo navegação via texto ou números. Abaixo está o detalhamento das principais engrenagens do código:

2.1. Estruturas de Dados (Dicionários e Listas)
Logo no início, o código inicializa duas estruturas cruciais:

historico = []: Uma lista vazia que atuará como a memória da sessão, guardando todas as equações e resultados gerados pelo usuário.

Operadores = {...}: Um dicionário robusto que mapeia cada operação matemática (Soma, Subtração, etc.). Dentro de cada chave, há outro dicionário contendo a 'Formula' base (em formato de string) e a 'legenda' que será exibida na tela. Isso deixa o código muito mais limpo do que se fossem usados múltiplos prints espalhados.

2.2. Interação Inicial
O sistema utiliza a função input() para capturar o nome do usuário (User_Name). Esse nome é utilizado posteriormente usando f-strings (ex: f'Muito bem {User_Name}...') para personalizar as mensagens e os registros do histórico.

2.3. Menu Principal
O usuário é apresentado a um menu principal onde escolhe entre:

Calculadora Simples

Calculadora de Proporção

O uso do método .upper() no input garante que, se o usuário digitar "simples", "Simples" ou "SIMPLES", o sistema consiga validar a entrada na lista de condições ['1', 'CALCULADORA SIMPLES', 'SIMPLES'], evitando erros de digitação.

2.4. A Calculadora Simples
Se a primeira opção for escolhida, o programa entra em um laço de repetição infinito (while True).

Captura de Dados: Dependendo da operação, um laço for roda duas vezes para capturar os números e guardá-los na lista temporária num.

Processamento de Strings: Uma funcionalidade muito inteligente aqui é o uso do .replace(). O código pega a fórmula armazenada no dicionário (ex: 'num1 + num2') e substitui as palavras "num1" e "num2" pelos números reais digitados.

Cálculo e Registro: A operação matemática real é feita (ex: resultado = num[0] + num[1]), exibida na tela, e uma string formatada é adicionada à lista historico.

Visualização de Histórico: A opção 6 utiliza a função enumerate() para varrer a lista de histórico e imprimir cada registro com seu respectivo índice numérico.

2.5. A Calculadora de Proporção (Regra de Três)
Se a segunda opção for escolhida, o sistema entra na lógica de proporção matemática.

Proteção contra Erros: O código verifica se a ou c são iguais a zero (if a == 0 or c == 0:). Isso é uma ótima prática para evitar erros de divisão por zero que "quebrariam" o programa.

Lógica Direta vs. Inversa:

Direta: Calcula a regra de três padrão: x = (b * c) / a.

Inversa: Calcula multiplicando em linha reta: x = (a * b) / c.

O resultado também é formatado e injetado na lista global de historico, mantendo a consistência do sistema.
