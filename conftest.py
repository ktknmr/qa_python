from main import BooksCollector
import pytest

# создание коллекции с одной книгой
@pytest.fixture
def one_book_collection():
    name = 'Справочник по Python'
    one_book_collection = BooksCollector()
    one_book_collection.add_new_book(name)

    return one_book_collection


