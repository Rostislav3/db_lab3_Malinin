import csv
import psycopg2

username = 'Malinin_R'
password = '1234'
database = 'vaccines'
host = 'localhost'
port = '5432'


INPUT_CSV_FILE = 'Culmulativ pecentage of vaccines.csv'

query_0 = '''
CREATE TABLE new_vacs
(
    Date varchar(40) ,
    Vaccinated_firs_dose character varying(40),
    Vaccinated_second_dose  character varying(40),
    Vaccinated_third_dose character varying(40),
    Percentage_of_vaccinated_first_dose character varying(40),
    Percentage_of_vaccinated_second_dose character varying(40),
    Percentage_of_vaccinated_third_dose character varying(400),
    CONSTRAINT pk_new_vacs PRIMARY KEY (Date)
)
'''

query_1 = '''
DELETE FROM new_vacs
'''

query_2 = '''
INSERT INTO new_vacs ( Date,  Vaccinated_firs_dose, Vaccinated_second_dose, Vaccinated_third_dose, Percentage_of_vaccinated_first_dose, Percentage_of_vaccinated_second_dose, Percentage_of_vaccinated_third_dose) 
VALUES ( %s, %s, %s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS new_vacs')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):

            values = ( idx, row['Vaccinated firs dose'], row['Vaccinated second dose'], row['Vaccinated third dose'],row['Percentage of vaccinated first dose'],row['Percentage of vaccinated second dose'],row['Percentage of vaccinated third dose'])
            cur.execute(query_2, values)

    conn.commit()