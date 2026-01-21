import requests
def consultar_cep(cep):
    url=f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta=requests.get(url)
        resposta.raise_for_status()
        dados=resposta.json()

        if 'erro' in dados:
            return "CEP inválido."
        
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        localidade = dados['localidade']
        uf = dados['uf']
            
        return f"Logradouro: {logradouro}\nBairro: {bairro}\nLocalidade: {localidade}\nUf: {uf}"
    
    except requests.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"
    
cep = input("Digite o cep: ")
resultado = consultar_cep(cep)
print(resultado)