CREATE TABLE Users (
    id VARCHAR(3) NOT NULL,
    name VARCHAR(100) NOT NULL,
    ${commonColumns},
    CONSTRAINT Users_pk PRIMARY KEY (id)
);

INSERT INTO monotraining.users
(id,name)
VALUES
 ('001','Tanaka')
,('002','Tamura')
,('003','Nakata')
