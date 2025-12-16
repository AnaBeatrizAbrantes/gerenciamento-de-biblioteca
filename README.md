# Sistema de Biblioteca

## Visão Geral

Este projeto propõe o desenvolvimento de um **Sistema de Biblioteca** com foco em análise, modelagem, prototipação e testes. O objetivo é aplicar conceitos de engenharia de software, desde a elicitação de requisitos até a validação do sistema por meio de testes automatizados.

O sistema foi modelado de forma **independente de banco de dados**, utilizando apenas **coleções em Python (listas e dicionários)** para representar os dados, facilitando o entendimento da lógica e a portabilidade do projeto.

---

Para acessar o projeto:

---

## Objetivos do Projeto

* Documentar os requisitos funcionais e não funcionais do sistema
* Modelar o sistema por meio de diagramas UML
* Representar o modelo de dados com Diagrama Entidade-Relacionamento
* Desenvolver protótipos de telas em média fidelidade
* Implementar testes automatizados em Python
* Demonstrar o funcionamento do sistema de forma clara e organizada

---

## Escopo do Sistema

O sistema de biblioteca permite:

* Cadastro e gerenciamento de usuários
* Cadastro e gerenciamento de livros
* Controle de empréstimos e devoluções
* Consulta de disponibilidade de livros
* Registro do histórico de empréstimos

---

## Requisitos do Sistema

### Requisitos Funcionais

* Cadastrar usuários
* Cadastrar livros
* Atualizar e remover usuários
* Atualizar e remover livros
* Realizar empréstimo de livros
* Registrar devolução de livros
* Consultar livros disponíveis
* Consultar histórico de empréstimos por usuário

### Requisitos Não Funcionais

* Sistema simples e intuitivo
* Código organizado e legível
* Testes automatizados para validação das regras de negócio
* Não utilizar banco de dados externo

---

## Diagramas do Sistema

### Diagrama de Casos de Uso

Representa as interações entre os atores (Usuário/Bibliotecário) e o sistema, destacando funcionalidades como cadastro, empréstimo, devolução e consulta.

### Diagramas de Atividades

Descrevem o fluxo de ações do sistema, como:

* Processo de empréstimo de um livro
* Processo de devolução
* Processo de cadastro de usuários e livros

### Diagrama Entidade-Relacionamento (DER)

Modela as principais entidades do sistema e seus relacionamentos:

* **Usuário**
* **Livro**
* **Empréstimo**

Cada entidade contém seus atributos essenciais, bem como as chaves que definem os relacionamentos.

---

## Protótipo das Telas (Mid-Fidelity)

Os protótipos representam a interface do sistema em média fidelidade, focando na organização visual e na usabilidade.

As telas podem ser desenvolvidas utilizando:

* **Figma**, para prototipação visual
* **HTML + CSS**, para representação estrutural das interfaces

Telas previstas:

* Tela inicial
* Tela de cadastro de usuários
* Tela de cadastro de livros
* Tela de empréstimo
* Tela de devolução
* Tela de consulta

---

## Implementação e Estrutura de Dados

O sistema utiliza **listas e dicionários em Python** para simular o banco de dados.

Exemplos:

* Lista de usuários
* Lista de livros
* Lista de empréstimos

Essa abordagem permite testar toda a lógica do sistema sem dependência de um SGBD.

---

## Testes do Sistema

Os testes foram desenvolvidos em **Python**, com o objetivo de validar:

* Cadastro correto de usuários e livros
* Regras de empréstimo (disponibilidade do livro)
* Registro correto de devoluções
* Integridade dos dados armazenados nas coleções

Os testes garantem que o sistema se comporte conforme os requisitos definidos.

---

## Tecnologias Utilizadas

* Python
* Listas e Dicionários (simulação de banco de dados)
* Figma ou HTML + CSS (protótipos)
* UML (diagramas)

---

## Status do Projeto

Este projeto **não se encontra em sua versão final**. A documentação, os diagramas, os protótipos de telas e partes do sistema ainda estão **em desenvolvimento e sujeitos a modificações**.
A versão atual tem como objetivo apresentar a proposta do sistema, sua estrutura inicial e a aplicação dos conceitos de engenharia de software, podendo sofrer ajustes, melhorias ao longo do processo de desenvolvimento, inclusive no site e na implementação das funcionalidades.

---
