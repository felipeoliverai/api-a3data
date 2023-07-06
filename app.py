
import requests


def main():
    UF = "SP"
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/distritos"

    # Fazendo a chamada GET na API
    data = requests.get(url).json()
    print(data)



if __name__ == "__main__":
    main()
