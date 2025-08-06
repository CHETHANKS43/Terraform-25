import json
import requests

# def fetch_google_books_data(query):
#     """Fetch book data from Google Books API for a given query."""
#     url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Failed to fetch data.")
#         return None

# def parse_google_books_json(json_data):
#     """Parse Google Books API JSON response and display book details."""
#     if not json_data:
#         return
    
#     books = json_data.get("items", [])
#     for book in books:
#         volume_info = book.get("volumeInfo", {})
#         title = volume_info.get("title", "Unknown Title")
#         authors = volume_info.get("authors", ["Unknown Author"])
#         published_date = volume_info.get("publishedDate", "Unknown Date")
        
#         print(f"Title: {title}")
#         print(f"Authors: {', '.join(authors)}")
#         print(f"Published Date: {published_date}")
#         print("-" * 40)

# def json_examples():
#     print("--- JSON Module Examples with Google Books API ---")
#     query = "Python programming"
#     json_data = fetch_google_books_data(query)
#     parse_google_books_json(json_data)

if __name__ == "__main__":
    # json_examples()




    respone = requests.get('https://www.googleapis.com/books/v1/volumes?q=%22docker%22')

    print(respone)





