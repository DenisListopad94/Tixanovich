'''
1.	Подключить готовую базу с актёрами и режиссёрами использую SQLite3. При помощи “сырого” запроса вывести все фильмы,
которые были сняты с 2015 по 2020 год.

import sqlite3

con = sqlite3.connect("cinema.db")
cur = con.cursor()

res = cur.execute(
    """
    SELECT name_movie, release
    FROM movies
    WHERE release >= 2015 AND release <= 2020
    """
)

mov = res.fetchall()
print(mov)

2.	Использую SQLite3 при помощи “сырого”  запроса вывести актёров и режиссёров, которые не участвовали
не в одном из фильмов.

import sqlite3

con = sqlite3.connect("cinema.db")
cur = con.cursor()

res = cur.execute(
    """
    SELECT actors.name, actors.surname
    FROM actors
    LEFT JOIN actors_movies ON actors.actors_id = actors_movies.actors_id
    WHERE actors_movies.actors_movies_id IS NULL;
    """
)

actors = res.fetchall()
print(actors)
res = cur.execute(
    """
    SELECT directors.name, directors.surname
    FROM directors
    LEFT JOIN movies ON directors.director_id = movies.director_id
    WHERE movies.movie_id IS NULL;
    """
)

directors = res.fetchall()
print(directors)

3.	Использую SQLite3 при помощи “сырого”  запроса вывести все фильмы  которые были сняты
после 2000 года и в которых приняло участие более 1 актёра.

import sqlite3

con = sqlite3.connect("cinema.db")
cur = con.cursor()

res = cur.execute(
    """
    SELECT movies.name_movie, movies.release
    FROM movies
    WHERE movies.release > 2000 AND (
        SELECT COUNT(*)
        FROM actors_movies
        WHERE actors_movies.movies_id = movies.movie_id
    ) > 1;
    """
)

movies = res.fetchall()
print(movies)

4.	Использую SQLite3 при помощи “сырого”  запроса вывести первых 5 самых высокооплачиваемых актёров.

import sqlite3

con = sqlite3.connect("cinema.db")
cur = con.cursor()

res = cur.execute(
    """
    SELECT actors.name, actors.surname, movies.budjet
    FROM actors
    JOIN actors_movies ON actors.actors_id = actors_movies.actors_id
    JOIN movies ON actors_movies.movies_id = movies.movie_id
    ORDER BY movies.budjet DESC
    LIMIT 5;
    """
)

actors = res.fetchall()
print(actors)

5.	Использую SQLite3 при помощи “сырого”  запроса вывести всех режиссёров и актёров
которые были задействованы только в 1 фильме.

import sqlite3

con = sqlite3.connect("cinema.db")
cur = con.cursor()

res = cur.execute(
    """
    SELECT actors.name, actors.surname
    FROM actors
    JOIN actors_movies ON actors.actors_id = actors_movies.actors_id
    GROUP BY actors.actors_id
    HAVING COUNT(actors_movies.movies_id) = 1
    """
)

actors = res.fetchall()
print(actors)
______
    SELECT directors.name, directors.surname
    FROM directors
    JOIN movies ON directors.director_id = movies.director_id
    GROUP BY directors.director_id
    HAVING COUNT(movies.movie_id) = 1

directors = res.fetchall()
print(directors)

6.	Создать питоновский файл models.py . Создать таблицу Users определив поля
( id: первичный ключ, first_name,last_name:строки длинной в 50 символов, age: целое число).
Создать “движок” для подключения SQLite и создать таблицу через Base.metadata.create_all(engine)


from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]

engine = create_engine("sqlite://", echo=True)

Base.metadata.create_all(engine)

7.	Создать сессию и добавить в базу 5 разных пользователей.

engine = create_engine("sqlite://", echo=True)
with Session(engine) as session:
    Travolta = User(
        first_name="John",
        last_name="Travolta",
        age=53
    )
    Jolie = User(
        first_name="Angelina",
        last_name="Jolie",
        age=47
    )
    Hanks = User(
         first_name="Tom",
         last_name="Hanks",
         age=66
    )
    Willis = User(
         first_name="Bruce",
         last_name="Willis",
         age=67
    )
    Bullock = User(
         first_name="Sandra",
         last_name="Bullock",
         age=58
    )
    session.add_all([Travolta, Jolie, Hanks, Willis, Bullock])
    session.commit()

8.	Создать сессию и вывести первых 3 пользователей отсортированных по убыванию возроста
engine = create_engine("sqlite://", echo=True)
with Session(engine) as session:

    stmt = select(User).order_by(User.age.desc()).limit(3)
    for user in session.scalars(stmt):
        print(user.first_name, user.last_name, user.age)

9.	Создать сессию и вывести  пользователей по имени “Jhon”
engine = create_engine("sqlite://", echo=True)
with Session(engine) as session:

    stmt = select(User).where(User.first_name == "John")
    for user in session.scalars(stmt):
        print(user.first_name, user.last_name, user.age)

____________________________________________
'''

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    Travolta = User(
        first_name="John",
        last_name="Travolta",
        age=53
    )
    Jolie = User(
        first_name="Angelina",
        last_name="Jolie",
        age=47
    )
    Hanks = User(
         first_name="Tom",
         last_name="Hanks",
         age=66
    )
    Willis = User(
         first_name="Bruce",
         last_name="Willis",
         age=67
    )
    Bullock = User(
         first_name="Sandra",
         last_name="Bullock",
         age=58
    )
    session.add_all([Travolta, Jolie, Hanks, Willis, Bullock])
    session.commit()

with Session(engine) as session:

    stmt = select(User).where(User.first_name == "John")
    for user in session.scalars(stmt):
        print(user.first_name, user.last_name, user.age)

