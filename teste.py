import json

def lambda_handler(event, context):
    # Extrair os parâmetros da chamada atual
    function = event.get("function", "UNKNOWN_FUNCTION")
    new_parameters = event.get("parameters", {})  # Parâmetros da função chamada agora

    # Buscar parâmetros já armazenados na sessão anterior (se houver)
    previous_parameters = event.get("sessionState", {}).get("parameters", {})

    print(f"Função executada: {function}")
    print(f"Novos parâmetros recebidos: {json.dumps(new_parameters, indent=2)}")
    print(f"Parâmetros anteriores na sessão: {json.dumps(previous_parameters, indent=2)}")

    # Mesclar os parâmetros antigos com os novos
    merged_parameters = {**previous_parameters, **new_parameters}

    print(f"Parâmetros combinados na sessão: {json.dumps(merged_parameters, indent=2)}")

    # Responder com o estado atualizado da sessão
    responseBody = {
        "parameters": merged_parameters  # Retorna o estado atualizado da sessão
    }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "responseBody": responseBody,
            "messageVersion": event.get("messageVersion", "1.0")
        })
    }
