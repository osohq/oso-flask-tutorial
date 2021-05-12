PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" ("id" integer PRIMARY KEY AUTOINCREMENT NOT NULL, "email" varchar, "title" varchar, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO users VALUES(1,'alice@foo.com','CEO','2020-07-23 01:59:24.803843','2020-07-23 01:59:24.803843');
INSERT INTO users VALUES(2,'bhavik@foo.com','Senior Accountant','2020-07-23 01:59:24.893020','2020-07-23 01:59:24.893020');
CREATE TABLE IF NOT EXISTS "expenses" ("id" integer PRIMARY KEY AUTOINCREMENT NOT NULL, "user_id" integer, "amount" integer, "description" varchar, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO expenses VALUES(1,2,64165,'Trust fund pour-over.','2020-07-23 01:59:26.793029','2020-07-23 01:59:26.793029');
INSERT INTO expenses VALUES(2,1,17743,'Pug irony.','2020-07-23 01:59:26.829541','2020-07-23 01:59:26.829541');
COMMIT;
