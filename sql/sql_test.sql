

USE hontodb
SELECT * FROM books;

CREATE TABLE IF NOT EXISTS books(\
                id int not null primary key auto_increment, \
                book_title varchar(255) not null




CREATE TABLE IF NOT EXISTS comic_ranking(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    book_title VARCHAR(255) NOT NULL,
    rank_num INT NOT NULL,
    created_at DATETIME NOT NULL
);
