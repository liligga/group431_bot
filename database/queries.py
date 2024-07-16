class Queries:
    CREATE_SURVEY_TABLE = """
    CREATE TABLE IF NOT EXISTS survey_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        genre TEXT
    )
    """

    DROP_GENRES = "DROP TABLE IF EXISTS genres"

    CREATE_GENRES_TABLE = """
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    POPULATE_GENRES = """
    INSERT INTO genres(name) VALUES 
    ('детектив'),
    ('фантастика'),
    ('триллер')
    """

    DROP_BOOKS = "DROP TABLE IF EXISTS books"

    CREATE_BOOKS_TABLE = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        author TEXT,
        cover TEXT,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genres(id)
    )
    """

    POPULATE_BOOKS = '''
    INSERT INTO books(name, author, price, cover, genre_id) VALUES 
        ("Тень в зеркале", "Алексей Смирнов", 1000, "images/book1.jpg", 1),
        ("Хроники Серебряного леса", "Елена Волкова", 2000, "images/book1.jpg", 2),
        ("Квантовый разлом", "Игорь Петров", 1200, "images/book1.jpg", 3),
        ("Осенние письма", "Мария Соколова", 1300, "images/book1.jpg", 1),
        ("Код мести", "Сергей Антонов", 2300, "images/book1.jpg", 2),
        ("Княжна Тараканова", "Ольга Романова", 2400, "images/book1.jpg", 3)
    '''

