# A URL é dividida em duas grandes partes uma sendo dividida pelo ponto de interogação
# a primeira sendo a base e a segunda são os parametros da URL
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

#".find" retorna qual a posição do objjeto informado
indice_interogacao = url.find("?")
url_base = url[0:indice_interogacao]

#no fatiamento se não passar a segundo argumento é intendido que quer ir de posição
#"X" até o final
url_parametros = url[indice_interogacao+1:]
print(url_parametros)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)


