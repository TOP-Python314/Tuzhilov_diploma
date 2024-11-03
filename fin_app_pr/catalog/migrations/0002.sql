BEGIN;
--
-- Alter field id on category
--
CREATE TABLE "new__categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "products" decimal NOT NULL, "lunch" decimal NOT NULL, "cloth" decimal NOT NULL, "sport" decimal NOT NULL, "petrol" decimal NOT NULL, "service" decimal NOT NULL, "home" decimal NOT NULL, "leisure" decimal NOT NULL, "mobile" decimal NOT NULL, "internet" decimal NOT NULL);
INSERT INTO "new__categories" ("name", "products", "lunch", "cloth", "sport", "petrol", "service", "home", "leisure", "mobile", "internet", "id") SELECT "name", "products", "lunch", "cloth", "sport", "petrol", "service", "home", "leisure", "mobile", "internet", "id" FROM "categories";
DROP TABLE "categories";
ALTER TABLE "new__categories" RENAME TO "categories";
--
-- Create model Budget
--
CREATE TABLE "budgets" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" decimal NOT NULL, "period_start" date NOT NULL, "period_end" date NOT NULL, "category_id" bigint NOT NULL REFERENCES "categories" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "budgets_category_id_328a159f" ON "budgets" ("category_id");
COMMIT;
