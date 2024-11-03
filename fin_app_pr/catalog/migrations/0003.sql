BEGIN;
--
-- Create model Transaction
--
CREATE TABLE "transactions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" decimal NOT NULL, "transaction_date" date NOT NULL, "description" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "categories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "transactions_category_id_65740af9" ON "transactions" ("category_id");
CREATE INDEX "transactions_user_id_766cc893" ON "transactions" ("user_id");
COMMIT;
