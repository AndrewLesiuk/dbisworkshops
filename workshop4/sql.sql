
ALTER TABLE "USERS"
ADD CONSTRAINT name_length_check
CHECK (length(user_name) > 1);

ALTER TABLE "USERS"
ADD CONSTRAINT phone_check
CHECK (user_phone LIKE '+380_________' AND  REGEXP_LIKE(TRIM('+' from user_phone), '^[[:digit:]]+$'));

ALTER TABLE "TAXI"
ADD CONSTRAINT name_length_check
CHECK (length(name_company) > 1);

ALTER TABLE "TAXI"
ADD CONSTRAINT price_check
CHECK (price > 0);

ALTER TABLE "ZAMOV"
ADD CONSTRAINT distance_check
CHECK (distance >= 1);


CREATE OR REPLACE TRIGGER new_price before INSERT ON "ZAMOV" FOR each row
BEGIN 
    SELECT
        price * :new.DISTANCE
        INTO :new.F_PRICE
    FROM
        "TAXI"
    WHERE
        TAXI_ID = :new.ID_TAXI; 
END;
/

