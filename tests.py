from main import BooksCollector



class TestBooksCollector:
    # добавление одной книги в коллекцию
    def test_add_new_book_add_one_book(self, one_book_collection):
        assert len(one_book_collection.get_books_rating()) == 1
    # значение рейтинга соответствует значению рейтинга по умолчанию
    def test_add_new_book_rating_equals_default_rating(self, one_book_collection):
        DEFAULT_RATING = 1
        name = list(one_book_collection.books_rating)[0]
        assert one_book_collection.books_rating[name] == DEFAULT_RATING
    # нельзя добавить книгу, которая уже находится в списке
    def test_add_new_book_existing_book_not_added(self):
        name = 'Гордость и предубеждение и зомби'
        ONE_BOOK_DICT_LEN = 1

        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)

        assert len(collector.books_rating) == ONE_BOOK_DICT_LEN
    # установка нового значения для рейтинга
    def test_set_book_rating_new_rating_updates_rating(self):
        name = 'Гордость и предубеждение и зомби'
        rating = 2
        collector = BooksCollector()
        collector.add_new_book(name)

        collector.set_book_rating(name, rating)

        assert collector.books_rating[name] == rating

    # получение значения текущего рейтинга книги
    def test_get_book_rating_existing_book_current_rating(self):
        name = 'Гордость и предубеждение и зомби'
        rating = 2
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == rating

    # получение списка книг с указанным значение рейтинга
    def test_get_books_with_specific_rating(self):
        SPECIFIC_RATING = 4

        names_and_ratings = {
            'Глава 1': 2,
            'Глава 2': 3,
            'Глава 3': SPECIFIC_RATING,
            'Глава 4': SPECIFIC_RATING,
            'Глава 5': SPECIFIC_RATING
        }

        collector = BooksCollector()

        for name, rating in names_and_ratings.items():
            collector.add_new_book(name)
            collector.set_book_rating(name, rating)

        assert list(names_and_ratings)[2:] == collector.get_books_with_specific_rating(SPECIFIC_RATING)

    # получение списка книг books_rating
    def test_get_books_rating_several_new_books_equals_current_result(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_rating == collector.get_books_rating()

    # добавление книги в список "избранное"
    def test_add_book_in_favorites_new_book_in_favorites_list(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]

    # удаление книги из списка "избранное"
    def test_delete_book_from_favorites_one_book_empty_list(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    # получение списка "избранное"
    def test_get_list_of_favorites_books_several_books_two_books_in_favorite_list(self):
        names = ['Гордость и предубеждение и зомби', 'Справочник по Python']
        collector = BooksCollector()
        for name in names:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        assert collector.favorites == names

