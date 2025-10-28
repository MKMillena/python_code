# Projeto de Exploração com Python e LangChain

Este repositório contém códigos e experimentos para explorar as funcionalidades da biblioteca LangChain e suas integrações com modelos de linguagem (LLMs).

O projeto está configurado com um ambiente de dependências definido e automação de testes via GitHub Actions para garantir que os scripts principais funcionem corretamente a cada nova alteração.

---

## 🚀 Começando

Siga estas instruções para obter uma cópia do projeto e executá-la em sua máquina local para desenvolvimento e testes.

### Pré-requisitos

*   Python 3.10 ou superior
*   Git instalado na sua máquina

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/SEU-USUARIO/python_code.git
    cd python_code
    ```
    *(Lembre-se de substituir `SEU-USUARIO` pelo seu nome de usuário do GitHub)*

2.  **Crie um ambiente virtual (altamente recomendado):**
    Isso isola as dependências do seu projeto e evita conflitos com outras bibliotecas do seu sistema.
    
    *   No Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   No macOS e Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias. Para instalá-las, execute:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente (se necessário):**
    Para usar serviços como a API da OpenAI, você precisará de chaves de API. Crie um arquivo chamado `.env` na raiz do projeto e adicione suas chaves nele.
    
    *   Crie um arquivo `.env`.
    *   Adicione suas chaves no formato `NOME_DA_CHAVE=valor_da_chave`:
        ```
        OPENAI_API_KEY="sua-chave-secreta-aqui"
        ```
    *(O arquivo `.env` nunca deve ser enviado para o GitHub).*

---

## 💻 Como Usar

Para executar o script de teste principal, que valida a funcionalidade da biblioteca LangChain Core, use o seguinte comando no seu terminal:

```sh
python pythonTest.py
