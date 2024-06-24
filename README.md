# Python Twitter Trends

Este projeto utiliza FastAPI para recuperar tendências do Twitter e armazená-las no MongoDB.

## Requisitos

- Docker
- Python 3.11

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/magominimalista/python-twitter.git
   cd python-twitter
   ```

2. Construa o ambiente e as dependências com Docker Compose:

    ```bash
   docker-compose build
   ```

3. Executando o Projeto<br>
Para iniciar os serviços (MongoDB, Mongo Express, e FastAPI), execute

    ```bash
   docker-compose up
   ```

4. Acesse os seguintes serviços:
   - FastAPI: http://localhost:8000
   - Mongo Express: http://localhost:8080

## Rodando os testes
Para rodar os testes, você pode usar o Pytest. Certifique-se de ter todas as dependências instaladas (preferencialmente em um ambiente virtual Python).

1. Instale as dependências de desenvolvimento: 
    ```bash
   poetry install --dev
   ```
2. Execute os testes:
    ```bash
   pytest
   ```

## Contribuindo
Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões ou melhorias para este projeto.

## Autor
Philipe Cairon (Mago Minimalista)

GitHub: magominimalista
Contato: magominimalista@gmail.com
