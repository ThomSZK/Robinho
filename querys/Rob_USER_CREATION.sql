CREATE TABLE Rob_User (
	User_ID SERIAL PRIMARY KEY,
	User_Acc VARCHAR(255) NOT NULL,
	User_Password VARCHAR(255) NOT NULL
);

ALTER TABLE Rob_User 
ADD User_Type INTEGER;

CREATE TABLE Rob_Review_Tasks (
	Task_ID INTEGER NOT NULL,
	User_ID INTEGER  NOT NULL,
	Task_Grade INTEGER,
	Task_Reviewed BOOL NOT NULL DEFAULT false,
	Task_Reviewer INTEGER,
	Task_Time INTEGER,
	PRIMARY KEY (Task_ID, User_ID),
	FOREIGN KEY (User_ID) REFERENCES Rob_User (User_Id),
	FOREIGN KEY (Task_Reviewer) REFERENCES Rob_User (User_Id)
);

CREATE TABLE Rob_Tasks (
	Task_ID INTEGER NOT NULL,
	Task_Name VARCHAR(255) NOT NULL,
	Task_Level INTEGER NOT NULL,
	Task_Order INTEGER NOT NULL
);

INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (1, 'Piscar LED', 1, 1);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (2, 'Movimento do robô', 1, 2);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (3, 'Percorrer trajeto', 1, 3);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (4, 'Ler sensor de cor', 1, 4);

INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (5, 'Identificar cor', 2, 1);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (6, 'Botões', 2, 2);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (7, 'Encontrar a caixa', 2, 3);

INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (8, 'Labirinto', 3, 1);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (9, 'Levar a caixa no lugar', 3, 2);
INSERT INTO Rob_Tasks (Task_ID, Task_Name, Task_Level, Task_Order)
VALUES (10, 'Genius', 3, 3);

ALTER TABLE Rob_User
add user_current_task integer;

CREATE table Rob_Queue (
	Queue_Id serial primary key,
	User_Id integer not null,
	User_Name varchar(255) not null,
	Task_Id integer not null
);

ALTER TABLE Rob_Tasks
ADD COLUMN Task_Description VARCHAR(1000);

UPDATE Rob_Tasks
SET Task_Description = 'Os LEDs do robô deverão ser acesos em qualquer cor.'
WHERE Task_Id = 1;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá realizar movimentos de tal maneira que seja formado um quadrado. Ao fim da tarefa, o robô deverá estar na posição inicial.'
WHERE Task_Id = 2;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá ir até a posição inicial do trajeto, e então percorrer ele até o destino final. O trajeto pode ser definido de qualquer forma, contando que respeite as seguintes posições: Posição inicial: (10, 4); Posição final: (5, 1).'
WHERE Task_Id = 3;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá identificar a cor do chão através do sensor de cor.'
WHERE Task_Id = 4;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá encontrar o quadrado vermelho no chão e piscar os LEDs na mesma cor.'
WHERE Task_Id = 5;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá pressionar os botões da arena na seguinte sequência: 3-2-4-1'
WHERE Task_Id = 6;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá encontrar e pegar a caixa azul.'
WHERE Task_Id = 7;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá entrar no labirinto com o objetivo de encontrar a região com paredes verdes. Assim que encontrar, ele deverá piscar os LEDs na mesma cor.'
WHERE Task_Id = 8;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá encontrar o bloco da cor amarela, piscar os LEDs indicando a cor encontrada e levar o bloco até a posição de mesma cor.'
WHERE Task_Id = 9;

UPDATE Rob_Tasks
SET Task_Description = 'O robô deverá observar a sequência de cor mostrada pelo LED da arena e, então, apertar os botões correspondentes na mesma sequência.'
WHERE Task_Id = 10;