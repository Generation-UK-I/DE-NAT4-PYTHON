CREATE DATABASE normalised_movies_db;
-- switch to normalised_movies_db in Adminer or \c to change database in a postgres psql container terminal

CREATE TABLE movies (
  movie_id INT NOT NULL,
  movie_name VARCHAR(255) NOT NULL,
  movie_year INT,
  PRIMARY KEY (movie_id)
);

INSERT INTO movies (movie_id, movie_name, movie_year)
VALUES
  (1, 'The Shining', 1980),
  (2, 'Titanic', 1997),
  (3, 'Minions', 2015),
  (4, 'IT', 2017);

CREATE TABLE genres (
  genre_id INT NOT NULL,
  genre_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (genre_id)
);

INSERT INTO genres (genre_id, genre_name)
VALUES
  (1, 'Comedy'),
  (2, 'Romance'),
  (3, 'Horror');

CREATE TABLE members (
  member_id INT NOT NULL,
  email VARCHAR(255) NOT NULL,
  fav_genre_id INT,
  username VARCHAR(255),
  PRIMARY KEY (member_id),
  FOREIGN KEY (fav_genre_id) REFERENCES genres(genre_id)
);

INSERT INTO members (member_id, email, fav_genre_id, username)
VALUES
  (1, 'tomk@example.com', 3, 'tommy-k'),
  (2, 'johnd@example.com', 2, 'the-movie-guy'),
  (3, 'janed@example.com', 1, 'i-love-minions'),
  (4, 'maryw@example.com', 3, 'horror-fan-1990');

CREATE TABLE member_movies (
  member_id INT NOT NULL,
  movie_id INT NOT NULL,
  PRIMARY KEY (member_id, movie_id),
  FOREIGN KEY(member_id) REFERENCES members(member_id),
  FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);

INSERT INTO member_movies (member_id, movie_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 2),
  (3, 3),
  (4, 1),
  (4, 4);
