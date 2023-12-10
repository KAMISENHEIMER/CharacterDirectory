CREATE DATABASE character_directory;
USE character_directory;
CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `discord_id` BIGINT NOT NULL UNIQUE
);
CREATE TABLE `characters`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `user` BIGINT UNSIGNED NOT NULL,
    `class` VARCHAR(255) NOT NULL,
    `subclass` VARCHAR(255) NOT NULL,
    `race` VARCHAR(255) NOT NULL,
    `lvl` INT NOT NULL DEFAULT '1',
    `balance` INT NOT NULL DEFAULT '0',
    `status` ENUM('alive','dead','retired','missing') NOT NULL DEFAULT 'alive',
    `quests_completed` INT NOT NULL DEFAULT '0',
    `XP` FLOAT NOT NULL DEFAULT '0',
    `body_status` VARCHAR(255) NULL,
    `death_month` INT NULL,
    `notes` VARCHAR(255) NULL,
    `dm_notes` VARCHAR(255) NULL
);
ALTER TABLE
    `characters` ADD CONSTRAINT `character_user_foreign` FOREIGN KEY(`user`) REFERENCES `users`(`id`);