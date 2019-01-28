CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Almirah', 17);
INSERT INTO Ages (name, age) VALUES ('Sandie', 17);
INSERT INTO Ages (name, age) VALUES ('Derren', 22);
INSERT INTO Ages (name, age) VALUES ('Cecilia', 28);
INSERT INTO Ages (name, age) VALUES ('Sayuri', 23);
INSERT INTO Ages (name, age) VALUES ('Maura', 14);

SELECT hex(name || age) AS X FROM Ages ORDER BY X