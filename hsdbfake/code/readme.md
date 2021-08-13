# 建立一個簡單的測試服務器

安裝資料庫
``` bash
pip3 install pymysql sqlalchemy
```
以mariadb的測試資料庫test為主
``` sql
CREATE DATABASE IF NOT EXISTS ttomdb;
USE ttomdb;
ALTER DATABASE ttomdb CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `stocks` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`code` CHAR(4) NOT NULL COLLATE 'utf8_general_ci',
	`name` VARCHAR(32) NOT NULL COLLATE 'utf8_general_ci',
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	`deleted_at` TIMESTAMP NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```


# 參考資料
https://stackoverflow.com/questions/52992361/flask-sqlalchemy-does-not-close-mysql-database-connections

https://ithelp.ithome.com.tw/articles/10220446