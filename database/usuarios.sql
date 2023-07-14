create database smartnest;
use smartnest
create table usuario(
    id int primary key auto_increment,
    name varchar(50) not null,
    edad tinyint not null,
    sexo char(1) check (sexo='M'  or sexo='F') not null,
    country,
    fecha_nac date not null,
    address varchar(50),
    phone int not null,
    email varchar(50) not null,
    google varchar(50)
);
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL
);


insert into usuario values(
    'Javier Gutierrez Alvarado',
    23,
    M,
    'Peru',
    01/01/2000,
    Jr. Aldevaran 154,
    996581234,
    'JGAlvarado@gmail.com',
    ...
);

insert into usuario values(
    'Alexis Blanco Perez',
    45,
    M,
    'Peru',
    01/01/1978,
    Av. Circunvalacion 7986,
    996558744,
    'ABP@gmail.com',
    ...
);

insert into usuario values(
    'Elena Maria Cordon',
    37,
    F,
    'Venezuela',
    01/01/1986,
    Av. Los Cañones 784512,
    996558744,
    'CañonMaria@gmail.com',
    ...
);

insert into usuario values(
    'Jose-Andres Hinojosa Wu',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Miraflores 2878,
    998758224,
    'J@gmail.com',
    ...
);

insert into usuario values(
    'Raimundo Mira Elizabeth',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);

insert into usuario values(
    'Amaia Jara',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);

insert into usuario values(
    'Neus Minguez',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);

insert into usuario values(
    'John Cañizares',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);

insert into usuario values(
    'Rayan Roldan',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);

insert into usuario values(
    'Milagros Nevado',
    18,
    M,
    'Argentina',
    01/01/2005,
    Av. Flor 5694,
    996532148,
    '@gmail.com',
    ...
);






https://www.thecreativedev.com/how-to-store-a-file-in-database/
 horas decimal (5,1));
  foreign key (idcarrera) references carrera(idcarrera));



