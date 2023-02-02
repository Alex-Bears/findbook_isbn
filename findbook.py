import isbnlib
import pprint

pp = pprint.PrettyPrinter(indent=4, sort_dicts=True)


def find_book(isbn_text):
    """
    Find book from isbn catalog
    isbn_text - ISBN Code ex: "978-5-4461-1917-2"
    """
    isbn_data = isbnlib.meta(isbn_text)
    if isbn_data == {}:
        print("No data :(")
        return
    pp.pprint(isbn_data)

    filename = f'{isbn_data["Title"]} - {isbn_data["Authors"][0]} - {isbn_data["Year"]}'.replace(":", "")
    print(filename)


find_book("978-5-49807-747-5")
