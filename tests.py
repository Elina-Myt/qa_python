from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)

        assert len(collector.books_genre) == 1

    def test_set_book_genre_book(self):
        collector = BooksCollector()
        collector.add_new_book('name1')
        collector.set_book_genre('name1', 'Фантастика')

        assert collector.books_genre['name1'] == 'Фантастика'

    def test_set_book_genre_book_out_of_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('name1')
        collector.set_book_genre('name1', 'Роман')

        assert collector.books_genre['name1'] == ''

    def test_get_book_genre_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_genre().get('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_book_list_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('1984')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('1984', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна','1984']

    def test_get_books_genre_book_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Дракула', 'Ужасы')

        assert collector.get_books_genre() == {'Дюна':'Фантастика','Дракула':'Ужасы'}

    def test_get_books_for_children_book_list(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Дракула', 'Ужасы')

        assert collector.get_books_for_children() == ['Колобок']

    def test_add_book_in_favorites_book_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        assert collector.favorites == ['1984']

    def test_delete_book_from_favorites_book_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Колобок')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Колобок')
        collector.delete_book_from_favorites('Колобок')

        assert collector.favorites == ['1984']

    def test_get_list_of_favorites_book_list(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать?')
        collector.add_book_in_favorites('Что делать?')

        assert collector.get_list_of_favorites_books() == ['Что делать?']
