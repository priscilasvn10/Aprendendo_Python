import requests

def retorna_dados_cep(cep)
	response = requests.get('https://viacep.com.br/ws/01001000/{}/json/'.format(cep))
	print(response.status_code)
	print(response.json())
	dados_cep = reponse.json()
	print(dados_cep['logradouro'])
	print(dados_cep['complemento'])
	return dados_cep

def retorna_dados_pokemon(pokemon):
	reponse= requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
	dados_pokemon = retorna_dados_pokemon('pikachu')
	print(dados_pokemon['sprites']['front_shiny'])


def retorna_reponse(url):
	reponse = requests.get(url)
	return reponse.text


if __name__ == '__main__':
	reponse = retorna_reponse('https://globallabs.academy/')
	print(reponse)
#	retorna_dados_cep('22041001')
#	dados_pokemon = retorna_dados_pokemon('pikachu')
#	print(dados_pokemon['sprites']['front_shiny'])
