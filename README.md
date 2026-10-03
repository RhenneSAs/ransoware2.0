# 🔐 Ransomware 2.0 — Simulação em Python

Projeto desenvolvido em **Python** com o objetivo de praticar conceitos de **Programação Orientada a Objetos (POO)**, **interfaces gráficas**, **temporizadores**, **eventos** e **validação de entradas**.

> ⚠️ **Aviso:** Este projeto é apenas uma simulação visual/educacional de uma tela de ransomware. Ele **não criptografa, modifica ou exclui arquivos reais** do computador.

## 📌 Sobre o projeto

O projeto simula uma situação em que o usuário se depara com uma tela semelhante à de um ransomware.

A aplicação apresenta:

* 🖥️ Interface gráfica em tela cheia
* 🔐 Mensagem simulando arquivos criptografados
* ⏱️ Temporizador regressivo
* 🔑 Campo para inserir uma chave de liberação
* 🔢 Limite de 3 tentativas
* 💳 Simulação de verificação de pagamento
* 🔓 Sistema de desbloqueio através de senha
* ⚠️ Alteração visual do título conforme o tempo diminui

A aplicação é construída utilizando uma classe principal chamada `RansomwareApp`, responsável pelo funcionamento da interface e da lógica do programa.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Tkinter** — criação da interface gráfica
* **Pillow (PIL)** — carregamento e utilização da imagem de fundo
* **Threading** — execução do temporizador

## 📂 Estrutura do projeto

```text
ransomware-2.0/
│
├── ransoware 2.0.py
├── the-matrix-background-design-template.jpg
└── README.md
```

> O nome do arquivo principal pode ser alterado para um nome mais organizado, como `ransomware.py`.

## ⚙️ Funcionalidades

### 🔑 Sistema de senha

A aplicação possui uma senha definida internamente para simular a chave de desbloqueio.

O usuário possui **3 tentativas** para inserir a chave correta.

Caso a senha esteja correta, a aplicação exibe uma mensagem de sucesso e encerra a janela.

Caso contrário, o número de tentativas restantes é reduzido.

Essa lógica está implementada no método `decrypt()`.

### ⏱️ Temporizador

O projeto possui um contador regressivo que simula o tempo disponível para realizar o pagamento.

O temporizador é iniciado quando a aplicação começa e atualiza a interface continuamente.

### 🎨 Interface gráfica

A interface utiliza **Tkinter** para criar a janela, textos, botões, campo de entrada e elementos visuais.

O programa também utiliza uma imagem como plano de fundo através da biblioteca **Pillow**.

### 💳 Simulação de pagamento

O botão `Check Payment` não realiza nenhuma transação real.

Ele apenas exibe uma mensagem informando que o pagamento deve ser verificado.

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd ransomware-2.0
```

### 3. Instale a dependência

O projeto utiliza Pillow:

```bash
pip install pillow
```

### 4. Execute o programa

```bash
python "ransoware 2.0.py"
```

## 🔑 Chave de teste

Para testar o desbloqueio da aplicação, utilize:

```text
1234
```

A chave está definida no código apenas para fins de demonstração.

## 📚 Conceitos praticados

Este projeto foi desenvolvido como exercício de aprendizado e permite praticar:

* Classes e objetos
* Métodos
* `self`
* Condicionais
* Variáveis
* Entrada de dados
* Tratamento de eventos
* Tkinter
* `messagebox`
* Threads
* Temporizadores
* Manipulação de imagens
* Organização de código
* Programação Orientada a Objetos

## 🚧 Possíveis melhorias

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Separar a interface e a lógica em diferentes arquivos
* [ ] Criar uma tela inicial
* [ ] Melhorar a responsividade da interface
* [ ] Adicionar diferentes níveis de dificuldade
* [ ] Criar configurações para o temporizador
* [ ] Melhorar o sistema de mensagens
* [ ] Remover caminhos absolutos de arquivos
* [ ] Criar um arquivo `requirements.txt`
* [ ] Melhorar a organização do projeto

## 🎯 Objetivo

O objetivo principal deste projeto é **praticar Python e desenvolvimento de interfaces gráficas**, utilizando uma temática de segurança cibernética para tornar o exercício mais próximo de uma aplicação real.

---

### ⚠️ Disclaimer

Este software foi desenvolvido exclusivamente para **fins educacionais e de demonstração**.

Ele não possui como objetivo realizar ataques, criptografar arquivos, roubar informações ou causar danos a sistemas.
