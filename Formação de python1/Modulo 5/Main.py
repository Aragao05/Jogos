# A URL é dividida em duas grandes partes uma sendo dividida pelo ponto de interogação
# a primeira sendo a base e a segunda são os parametros da URL
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

#Sanitização da URL, Troca algo da url, por algo digitado 
url = url.replace(" ","")

#Validação pra saber se a URl passada não está vazia 
if url == "":
    raise ValueError("A URL esta vazia ")# retorna um erro com a mensagem escrita 

#".find" retorna qual a posição do objeto informado, (separa base e parametros)
indice_interogacao = url.find("?")
url_base = url[0:indice_interogacao]

#no fatiamento se não passar a segundo argumento é intendido que quer ir de posição
#"X" até o final
url_parametros = url[indice_interogacao+1:]
print(url_parametros)

#busca o valor de um parametro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&",indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)


