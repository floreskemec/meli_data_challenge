# MELI API explorer by Gonzalo Flores Kemec

This Python script utilizes the MercadoLibre API to conduct specific item searches and stores the outcomes in a CSV file.

## Dependencies
- Python 3
- `requests` library

## Usage
First install requirements with:

```bash
pip install -r requirements.txt
```

Then run the script using Python:

```bash
python -m meli_api_explorer.py
```

## How it Works
The script interfaces with the MercadoLibre API to search for items based on predefined terms in the **SEARCH_TERMS** list. It fetches a limited number of results for each term, processes them, and then compiles the data into a CSV file.

## Functions
**get_search_results(search_term, limit, offset=0)**

This function takes a search term, a limit, and an optional offset. It sends a GET request to the MercadoLibre API and returns the JSON response.

**process_item(item_id)**

This function takes an item ID, sends a GET request to the MercadoLibre API to retrieve the item's details, and returns a list containing the item's ID, title, price, condition, seller ID, first picture URL.

## Output
The script generates a CSV file named results.csv with the following columns:

id
title
price
condition
seller_id
picture

Upon completion, the script displays a message confirming the results have been saved to the CSV file.

## A note on Pagination and Offset
The offset parameter in the get_search_results function facilitates pagination within the MercadoLibre API.

This pagination handling is necessary due to the API's limitation on retrieving more than 50 results per page, which would otherwise trigger a bad request.

