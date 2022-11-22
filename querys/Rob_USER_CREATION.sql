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