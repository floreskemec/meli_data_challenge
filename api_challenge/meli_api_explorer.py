import requests
import csv

SEARCH_TERMS = ["chromecast", "google home", "apple tv", "amazon fire tv"] 
LIMIT = 50

def get_search_results(search_term, limit, offset=0):
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={search_term}&limit={limit}&offset={offset}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    return response.json()

def process_item(item_id):  
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    item = response.json()

    row = [
        item['id'],
        item['title'],
        item['price'],
        item['condition'],
        item['seller_id'],
        item['pictures'][0]['url'], 
    ]
    return row

def write_to_csv(rows):
    with open('results.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            'id',        
            'title',
            'price',
            'condition',
            'seller_id',
            'picture',
        ])
        for row in rows:
            csv_writer.writerow(row)

def main():
    all_rows = []
    for term in SEARCH_TERMS:
        print(f"Buscando {term}...")
        offset = 0
        total_results = 0

        while True:
            results = get_search_results(term, LIMIT, offset)
            paging_info = results["paging"]
            total_results = paging_info["total"]

            for result in results["results"]:
                row = process_item(result['id'])        
                all_rows.append(row)

            offset += LIMIT
            if offset >= total_results:
                break

    write_to_csv(all_rows)
    print("¡Resultados guardados en results.csv!")

if __name__ == "__main__":
    main()