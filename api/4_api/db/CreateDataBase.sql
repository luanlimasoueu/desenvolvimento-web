USE Pycoderbr;

CREATE TABLE carros (
    id integer not null auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
    PRIMARY KEY (id)
);


INSERT INTO carros (marca, modelo, ano) VALUES ('Fiat','Marea',1999) ;
INSERT INTO carros (marca, modelo, ano)  VALUES ('Fiat', 'Uno', 1992) ;
INSERT INTO carros  (marca, modelo, ano)VALUES ('Ford', 'Escort',1985) ;

