CREATE DATABASE SpaceObservations;
USE SpaceObservations;

CREATE TABLE `sector` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `coordinates` VARCHAR(255),
    `light_intensity` FLOAT,
    `foreign_objects` TEXT,
    `num_sky_objects` INT,
    `num_undefined_objects` INT,
    `num_defined_objects` INT,
    `notes` TEXT,
    `date_update` DATETIME DEFAULT NOW() NULL
);

CREATE TABLE `objects` (
    `object_id` INT AUTO_INCREMENT PRIMARY KEY,
    `type` VARCHAR(255),
    `determination_accuracy` FLOAT,
    `quantity` INT,
    `time` TIME,
    `date` DATE,
    `note` TEXT
);

CREATE TABLE `natural_objects` (
    `object_id` INT AUTO_INCREMENT PRIMARY KEY,
    `type` VARCHAR(255),
    `galaxy` VARCHAR(255),
    `accuracy` FLOAT,
    `light_flux` FLOAT,
    `associated_objects` TEXT,
    `note` TEXT
);

CREATE TABLE `position` (
    `position_id` INT AUTO_INCREMENT PRIMARY KEY,
    `earth_position` VARCHAR(255),
    `sun_position` VARCHAR(255),
    `moon_position` VARCHAR(255)
);

CREATE TABLE `relations` (
    `relation_id` INT AUTO_INCREMENT PRIMARY KEY,
    `sector_id` INT,
    `object_id` INT,
    `natural_object_id` INT,
    `position_id` INT,
    FOREIGN KEY (`sector_id`) REFERENCES `sector`(`id`),
    FOREIGN KEY (`object_id`) REFERENCES `objects`(`object_id`),
    FOREIGN KEY (`natural_object_id`) REFERENCES `natural_objects`(`object_id`),
    FOREIGN KEY (`position_id`) REFERENCES `position`(`position_id`)
);

DELIMITER //

CREATE TRIGGER `before_update_sector_date`
BEFORE UPDATE ON `sector`
FOR EACH ROW
BEGIN
    SET NEW.date_update = NOW();
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE JoinSectorAndObjects()
BEGIN
    SELECT s.id AS sector_id, s.coordinates, s.light_intensity, s.foreign_objects, s.num_sky_objects, s.num_undefined_objects, s.num_defined_objects, s.notes AS sector_notes,
           o.object_id, o.type, o.determination_accuracy, o.quantity, o.time, o.date, o.note AS object_note
    FROM relations r
    JOIN sector s ON r.sector_id = s.id
    JOIN objects o ON r.object_id = o.object_id;
END //

DELIMITER ;


INSERT INTO `sector` (`coordinates`, `light_intensity`, `foreign_objects`, `num_sky_objects`, `num_undefined_objects`, `num_defined_objects`, `notes`) 
VALUES 
('10,20', 150.5, 'None', 200, 10, 190, 'Observation 1'),
('30,40', 200.0, 'Meteor', 250, 20, 230, 'Observation 2'),
('50,60', 100.0, 'Satellite', 180, 15, 165, 'Observation 3'),
('70,80', 300.5, 'Debris', 220, 25, 195, 'Observation 4'),
('90,100', 250.0, 'None', 210, 12, 198, 'Observation 5');

INSERT INTO `objects` (`type`, `determination_accuracy`, `quantity`, `time`, `date`, `note`)
VALUES
('Star', 99.9, 5, '12:00:00', '2023-01-01', 'Star data 1'),
('Planet', 95.5, 3, '13:00:00', '2023-01-02', 'Planet data 1'),
('Comet', 98.0, 2, '14:00:00', '2023-01-03', 'Comet data 1'),
('Asteroid', 92.5, 4, '15:00:00', '2023-01-04', 'Asteroid data 1'),
('Meteor', 96.5, 1, '16:00:00', '2023-01-05', 'Meteor data 1');

INSERT INTO `natural_objects` (`type`, `galaxy`, `accuracy`, `light_flux`, `associated_objects`, `note`)
VALUES
('Star', 'Milky Way', 99.9, 1500.5, 'None', 'Natural object 1'),
('Planet', 'Andromeda', 95.5, 1200.0, 'Moon', 'Natural object 2'),
('Comet', 'Triangulum', 98.0, 900.0, 'None', 'Natural object 3'),
('Asteroid', 'Whirlpool', 92.5, 1100.5, 'None', 'Natural object 4'),
('Meteor', 'Milky Way', 96.5, 1300.0, 'None', 'Natural object 5');

INSERT INTO `position` (`earth_position`, `sun_position`, `moon_position`)
VALUES
('10,20', '30,40', '50,60'),
('15,25', '35,45', '55,65'),
('20,30', '40,50', '60,70'),
('25,35', '45,55', '65,75'),
('30,40', '50,60', '70,80');

INSERT INTO `relations` (`sector_id`, `object_id`, `natural_object_id`, `position_id`)
VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5);
