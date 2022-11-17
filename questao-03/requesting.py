import requests

resposta = requests.get('https://www.cesupa.br/css/imagens/LogoNovAzul.png')

with open('logo.png', 'wb') as f:
    f.write(resposta.content)

print(resposta.headers)

resposta = requests.post('https://httpbin.org/post')

print(resposta.headers)

resposta = requests.patch('https://httpbin.org/patch')

print(resposta.headers)
