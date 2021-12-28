-- efficency
INSERT INTO efficency (name, eff_prc)
  	VALUES ('CoronaVac', 82);
INSERT INTO efficency (name, eff_prc)
  	VALUES ('AstraZeneca', 86);
INSERT INTO efficency (name, eff_prc)
  	VALUES ('Comirnaty', 95);
INSERT INTO efficency (name, eff_prc)
  	VALUES ('Moderna', 89);
INSERT INTO efficency (name, eff_prc)
  	VALUES ('Sputnik V', 50);

-- manufacturer
INSERT INTO manufacturer (mnf_name)
  	VALUES ('Sinovac');
INSERT INTO manufacturer (mnf_name)
  	VALUES ('Vaxzevria');
INSERT INTO manufacturer (mnf_name)
  	VALUES ('AstraZeneca-SKBio');
INSERT INTO manufacturer (mnf_name)
  	VALUES ('Pfizer');
INSERT INTO manufacturer (mnf_name)
  	VALUES ('Moderna');
INSERT INTO manufacturer (mnf_name)
  	VALUES ('Фармстандарт');

-- country
INSERT INTO origin_country (country_name)
  	VALUES ('China');
INSERT INTO origin_country (country_name)
  	VALUES ('Europe');
INSERT INTO origin_country (country_name)
  	VALUES ('Korea');
INSERT INTO origin_country (country_name)
  	VALUES ('USA');
INSERT INTO origin_country (country_name)
  	VALUES ('Russia');



-- vaccines
INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('CoronaVac', 
			1, 1);
INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('AstraZeneca', 
			2, 2);
INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('AstraZeneca', 
			3, 3);
INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('Comirnaty', 
			4, 4);
INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('Moderna', 
			5, 4);

INSERT INTO vaccines (name , mnf_id, country_id)
	VALUES ('Sputnik V', 
			6, 5);
