DROP TABLE IF EXISTS Song;
DROP TABLE IF EXISTS  Album;
DROP TABLE IF EXISTS Artist;


CREATE TABLE Artist (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT
);

CREATE TABLE Album (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(id)
);

CREATE TABLE Song (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    track_num INT,
    length_seconds INT,
    album_id INT,
    FOREIGN KEY (album_id) REFERENCES Album(id)
);