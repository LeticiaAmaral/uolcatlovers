import requests
import csv

#Função para extrair todos os fatos de gatos
def fetch_all_cat_facts():
    url = "https://catfact.ninja/facts"
    page = 1
    all_facts = []
    
    while True:
        try:
            #Requisição para a API com o parâmetro de página
            r = requests.get(f"{url}?page={page}")

            #Verifica se a conexão foi bem sucedida
            if r.status_code == 200:
                data = r.json()

                # Adiciona os fatos da página atual a lista
                for fact_data in data['data']:
                    all_facts.append(fact_data['fact'])

                # Verifica se há mais páginas
                if data['current_page'] >= data['last_page']:
                    break

                page += 1

            else:
                print("Erro ao conectar na API:", r.status_code)
            
        except Exception as e:
            print(f"Erro ao faxer a solicitação: {e}")
            break
    
    return all_facts

def save_to_csv(facts, filename='cat_facts.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['fact'])  # Cabeçalho
            
            for fact in facts:
                writer.writerow([fact])
                
        print(f"Dados salvos com sucesso em {filename}")
    except IOError as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

def main():
    print("Iniciando extração de fatos sobre gatos...")
    cat_facts = fetch_all_cat_facts()
    
    print(f"Total de fatos coletados: {len(cat_facts)}")
    save_to_csv(cat_facts)

if __name__ == "__main__":
    main()