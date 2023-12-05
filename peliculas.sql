CREATE DATABASE IF NOT EXISTS CINE;
USE CINE;
CREATE TABLE peliculas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha INT NOT NULL,
	foto VARCHAR(255)
);

CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', '2022-03-01');
INSERT INTO `peliculas` (`nombre`, `descripcion`, `fecha`, `foto`) VALUES ('Top Secret!', 'Una satira sobre las peliculas de espias, en la cual una estrella de rock se ve envuelta en una red de espionaje.', '1984', 'foto1.jpg');
INSERT INTO `peliculas` (`nombre`, `descripcion`, `fecha`, `foto`) VALUES ('Oppenheimer', 'El fisico J Robert Oppenheimer trabaja con un equipo de cientificos durante el Proyecto Manhattan, que condujo al desarrollo de la bomba atomica.', '2023', 'foto2.jpg');
INSERT INTO `peliculas` (`nombre`, `descripcion`, `fecha`, `foto`) VALUES ('El renacido', 'Hugh Glass, un trampero y explorador de finales del siglo XIX resulta herido de muerte por el ataque de un oso. Sus compañeros deciden dejarle para proseguir con la expedicion.', '2015', 'foto3.jpg');
INSERT INTO `peliculas` (`nombre`, `descripcion`, `fecha`, `foto`) VALUES ('Django Desencadenado', 'Un antiguo esclavo une sus fuerzas con un cazador de recompensas aleman que lo libera y ayuda a cazar a los criminales mas buscados del Sur, todo ello con la esperanza de encontrar a su esposa perdida hace mucho tiempo.', '2013', 'foto4.jpg');
INSERT INTO `peliculas` (`nombre`, `descripcion`, `fecha`, `foto`) VALUES ('Una historia del bronx', 'El distrito de Fordam, en el Bronx, esta dominado por la mafia siciliana. El honesto conductor de autobuses y padre de familia Lorenzo Anello se niega a aceptar sobornos y vive una vida al margen de la mafia.', '1993', 'foto5.jpg');