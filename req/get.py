import requests

base_url = 'http://localhost:8080'
num_requests = 378

paths = ['', '/api', '/api/v1']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for i in range(num_requests):
    for path in paths:
        try:
            url = f'{base_url}{path}'

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print(f'Requisição {i+1} para {url}: Resposta 200 OK')
            elif response.status_code == 404:
                print(f'Requisição {i+1} para {url}: Resposta 404 Not Found')
            else:
                print(f'Requisição {i+1} para {url}: Resposta {response.status_code}')

        except requests.exceptions.RequestException as e:
            print(f'Requisição {i+1} para {url}: Erro de conexão - {e}')