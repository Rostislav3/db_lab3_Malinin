DO $$
DECLARE
    country_id  origin_country.country_id%TYPE;
    country_name     origin_country.country_name%TYPE;

BEGIN
    country_id := 10;
    country_name := 'CountryName';
    FOR counter IN 1..10
        LOOP
            INSERT INTO origin_country(country_id, country_name)
            VALUES (country_id + counter, country_name || counter);
        END LOOP;
END;
$$
 --select * from origin_country
