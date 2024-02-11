/*
CREATE USER 'app_quranbot'@'localhost' IDENTIFIED BY 'password';
GRANT INSERT, UPDATE, DELETE, SELECT ON quran_class.* TO 'app_quranbot'@'localhost' WITH GRANT OPTION;
*/

CREATE SCHEMA IF NOT EXISTS `quran_class`;
# DROP DATABASE `quran_class`;

/********** ROLE TABLE QUERIES **********/
CREATE TABLE IF NOT EXISTS `quran_class`.`role` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE INDEX `ix_role_id_UNIQUE` (`role_id` ASC) VISIBLE);

INSERT IGNORE INTO `quran_class`.`role`(`role_id`, `role_name`)
VALUES
(1, 'admin'),
(2, 'teacher'),
(3, 'student');

SELECT * FROM `quran_class`.`role`;
# DROP TABLE `quran_class`.`role`;

/********** USER TABLE QUERIES **********/
CREATE TABLE IF NOT EXISTS `quran_class`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `telegram_id` BIGINT NOT NULL,
  `telegram_username` VARCHAR(32) NULL,
  `first_name` VARCHAR(50) NULL,
  `last_name` VARCHAR(50) NULL,
  `display_name` VARCHAR(50) NULL,
  `email` VARCHAR(320) NULL,
  `role_id` INT NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT FK_role FOREIGN KEY (`role_id`) REFERENCES `role`(`role_id`),
  UNIQUE INDEX `IX_user_id_UNIQUE` (`user_id` ASC) VISIBLE);

INSERT IGNORE INTO `quran_class`.`user`(`user_id`,`telegram_id`,`telegram_username`,`first_name`,`last_name`,`display_name`,`email`,`role_id`)
VALUES
(1, 5295411622, 'abdullatif_farah', 'abdullatif', 'farah', 'Abdullatif F.', 'abdullatiffarah21@gmail.com', 1),
(2, 6466013214, 'goateedguy', 'damaani', 'webber', 'Damaani W.', 'damaaniwebber@aim.com', 1);

SELECT * FROM `quran_class`.`user`;
# DROP TABLE `quran_class`.`user`;