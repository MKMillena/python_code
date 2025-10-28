# 1. Importar a classe necessária de uma das bibliotecas
from langchain_core.prompts import ChatPromptTemplate

print("--- Iniciando o script de teste ---")

try:
    # 2. Criar um modelo de prompt simples
    #    Isto cria um modelo para uma conversa, esperando uma variável chamada "assunto".
    prompt_template = ChatPromptTemplate.from_template(
        "Me diga uma curiosidade interessante sobre {assunto}."
    )

    print("Modelo de prompt criado com sucesso.")

    # 3. Usar o modelo para gerar um prompt real
    #    Aqui, nós fornecemos o "assunto" que o modelo esperava.
    prompt_final = prompt_template.invoke({"assunto": "o planeta Marte"})

    print("Prompt final gerado com sucesso.")

    # 4. Imprimir o resultado final para vermos no log do GitHub Actions
    print("\n----- RESULTADO DO TESTE -----")
    print(prompt_final)
    print("----------------------------")
    print("\nScript executado com sucesso! A biblioteca LangChain Core funcionou.")

except Exception as e:
    # Se algo der errado, esta mensagem aparecerá no log de erro
    print(f"\nOcorreu um erro: {e}")
