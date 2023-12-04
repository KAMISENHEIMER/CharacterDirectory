CREATE DATABASE character_directory;
USE character_directory;
CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `discord_id` BIGINT NOT NULL
);
ALTER TABLE
    `users` ADD PRIMARY KEY `users_id_primary`(`id`);
ALTER TABLE
    `users` ADD UNIQUE `users_discord_id_unique`(`discord_id`);
CREATE TABLE `character`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `user` BIGINT NOT NULL,
    `class` VARCHAR(255) NOT NULL,
    `subclass` VARCHAR(255) NOT NULL,
    `race` VARCHAR(255) NOT NULL,
    `lvl` INT NOT NULL DEFAULT '1',
    `balance` INT NOT NULL,
    `status` ENUM('') NOT NULL DEFAULT 'alive',
    `quests_completed` INT NOT NULL,
    `XP` DOUBLE(8, 2) NOT NULL,
    `body_status` VARCHAR(255) NULL,
    `death_week` INT NULL,
    `notes` VARCHAR(255) NULL,
    `dm_notes` VARCHAR(255) NULL
);
ALTER TABLE
    `character` ADD PRIMARY KEY `character_id_primary`(`id`);
ALTER TABLE
    `character` ADD CONSTRAINT `character_user_foreign` FOREIGN KEY(`user`) REFERENCES `users`(`id`);