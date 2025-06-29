import requests
import csv
from datetime import datetime

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

                # Adiciona os dados da página atual a lista
                for fact_data in data['data']:
                    all_facts.append({
                        'fact': fact_data['fact'],
                        'length': len(fact_data['fact']),
                        'processed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
                    })
                
                #Se não tiverem mais páginas encerra
                if data['current_page'] >= data['last_page']:
                    break

                #Vai para a próxima página        
                page += 1

            else:
                print("Erro ao conectar na API:", r.status_code)
            
        except Exception as e:
            print(f"Erro ao fazer a solicitação: {e}")
            break
    
    return all_facts

#Salvar os fatos em csv
def save_to_csv(facts, filename='cat_facts.csv'):
    try:
        with open(filename, mode='w', newline='\n', encoding='utf-8') as file:
            #Define as colunas
            fieldnames = ['fact', 'length', 'processed_at']

            #Define os parametros do arquivo
            writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter=';')
            
            #Escreve os cabeçalhos
            writer.writeheader()  
            
            #Escreve as linhas
            for fact in facts:
                writer.writerow(fact)
                
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