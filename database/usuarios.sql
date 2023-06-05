create database smartpots;
use smartpots
create table usuario(
    id int primary key auto_increment,
    perfil blob,
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

insert into usuario values(
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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
    (imagen),
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



