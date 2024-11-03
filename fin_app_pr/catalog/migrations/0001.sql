BEGIN;
--
-- Alter field id on category
--
CREATE TABLE "new__categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "products" decimal NOT NULL, "lunch" decimal NOT NULL, "cloth" decimal NOT NULL, "sport" decimal NOT NULL, "petrol" decimal NOT NULL, "service" decimal NOT NULL, "home" decimal NOT NULL, "leisure" decimal NOT NULL, "mobile" decimal NOT NULL, "internet" decimal NOT NULL);
INSERT INTO "new__categories" ("name", "products", "lunch", "cloth", "sport", "petrol", "service", "home", "leisure", "mobile", "internet", "id") SELECT "name", "products", "lunch", "cloth", "sport", "petrol", "service", "home", "leisure", "mobile", "internet", "id" FROM "categories";
DROP TABLE "categories";
ALTER TABLE "new__categories" RENAME TO "categories";
COMMIT;
