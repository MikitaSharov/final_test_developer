DROP DATABASE IF EXISTS friends_human;
CREATE DATABASE friends_human;
USE friends_human;

-- создание таблиц
CREATE TABLE dog(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE cat(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE hamster(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE horse(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE camel(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE donkey(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE pet(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    class VARCHAR(30) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE pack(
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    class VARCHAR(30) NOT NULL,
    PRIMARY KEY(name, date_of_birthday)
);

CREATE TABLE animal(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    date_of_birthday DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    animal_type VARCHAR(30),
    class VARCHAR(30) NOT NULL
);

-- заполнение таблиц
INSERT INTO dog(name, date_of_birthday, commands)
VALUES
    ('Шарик', '2019-01-02', 'голос, сидеть, лежать'),
    ('Тузик', "2014-11-11", 'дружить, голос');

INSERT INTO cat(name, date_of_birthday, commands)
VALUES
    ('Мурка', '2015-01-22', 'голос, спать'),
    ('Мурзик', '2023-10-11', 'есть, просить');

INSERT INTO hamster(name, date_of_birthday, commands)
VALUES
    ('Винтик', '2020-05-03', 'голос');

INSERT INTO horse(name, date_of_birthday, commands)
VALUES
    ('Амадеус', '2015-01-22', 'но, грузи'),
    ('Буран', '2023-10-11', 'ждать');

INSERT INTO camel(name, date_of_birthday, commands)
VALUES
    ('Самец', '2015-01-22', 'плюнь');

INSERT INTO donkey(name, date_of_birthday, commands)
VALUES
    ('Иа', '2000-01-22', 'грустить, голос'),
    ('Пленник', '2022-10-11', 'красть');

-- удаление верблюдов
DELETE FROM camel;
DROP TABLE IF EXISTS camel;

-- объединение таблиц
DELIMITER //

CREATE PROCEDURE insert_into_pet_or_pack(IN class_as_table_name VARCHAR(30))
BEGIN
    DECLARE animal_type VARCHAR(30);
    SET @table_name = class_as_table_name;

    CASE class_as_table_name
        WHEN 'dog' THEN SET animal_type = 'pet';
        WHEN 'cat' THEN SET animal_type = 'pet';
        WHEN 'hamster' THEN SET animal_type = 'pet';
        WHEN 'horse' THEN SET animal_type = 'pack';
        WHEN 'camel' THEN SET animal_type = 'pack';
        WHEN 'donkey' THEN SET animal_type = 'pack';
        ELSE SELECT 'Нет такой таблицы' AS message;
    END CASE;

    IF animal_type = 'pet' THEN
        SET @request = CONCAT('INSERT INTO pet (name, date_of_birthday, commands, class)
                                 SELECT name, date_of_birthday, commands, ? FROM ', @table_name);
    ELSEIF animal_type = 'pack' THEN
        SET @request = CONCAT('INSERT INTO pack (name, date_of_birthday, commands, class)
                                 SELECT name, date_of_birthday, commands, ? FROM ', @table_name);
    END IF;

    PREPARE request FROM @request;
    EXECUTE request USING @table_name;
    DEALLOCATE PREPARE request;
END //

DELIMITER ;

CALL insert_into_pet_or_pack('dog');
CALL insert_into_pet_or_pack('cat');
CALL insert_into_pet_or_pack('hamster');
CALL insert_into_pet_or_pack('horse');
CALL insert_into_pet_or_pack('donkey');

INSERT INTO animal (name, date_of_birthday, commands, animal_type, class)
SELECT name, date_of_birthday, commands, 'pet' AS animal_type, class
FROM pet;

INSERT INTO animal (name, date_of_birthday, commands, animal_type, class)
SELECT name, date_of_birthday, commands, 'pack' AS animal_type, class
FROM pack;

-- новая таблица с возрастом
CREATE TABLE young_animal (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    date_of_birth DATE NOT NULL,
    commands VARCHAR(250) NOT NULL,
    animal_type VARCHAR(30),
    class VARCHAR(30) NOT NULL,
    age_in_months INT NOT NULL
);

INSERT INTO young_animal (id, name, date_of_birth, commands, animal_type, class, age_in_months)
SELECT id, name, date_of_birthday, commands, animal_type, class,
    TIMESTAMPDIFF(MONTH, date_of_birthday, CURDATE()) AS age_in_months
FROM animal
WHERE date_of_birthday BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

select * from young_animal;
