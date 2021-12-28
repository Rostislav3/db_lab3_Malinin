import psycopg2
import matplotlib.pyplot as plt

username = 'Malinin_R'
password = '1234'
database = 'vaccines'
host = 'localhost'
port = '5432'

query_1 = '''
create VIEW EffiencyProc as
select * from efficency
'''

query_2 = '''
create VIEW VacManuf as
select name, count(mnf_name) from manufacturer 
inner join vaccines on manufacturer.mnf_id=vaccines.mnf_id 
group by name
'''

query_3 = '''
create VIEW CountryVac as
select country_name,count(name) from vaccines 
inner join origin_country on vaccines.country_id=origin_country.country_id 
group by country_name

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS EffiencyProc')

    cur.execute(query_1)
    cur.execute('select * from EffiencyProc')
    eff = []
    eff_count = []

    for row in cur:
        eff.append(row[0])
        eff_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS VacManuf')

    cur.execute(query_2)
    cur.execute('select * from VacManuf')
    mnf = []
    mnf_count = []

    for row in cur:
        mnf.append(row[0])
        mnf_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS CountryVac')

    cur.execute(query_3)
    cur.execute('select * from CountryVac')
    cntry = []
    cn_count = []

    for row in cur:
        cntry.append(row[0])
        cn_count.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    # bar
    bar_ax.set_title('Процент еффективності від назви')
    bar_ax.set_xlabel('Назва')
    bar_ax.set_ylabel('процент')
    bar = bar_ax.bar(eff, eff_count)
    bar_ax.set_xticks(range(len(eff)))
    bar_ax.set_xticklabels(eff, rotation=30)

    # pie
    pie_ax.pie(cn_count, labels=cntry, autopct='%1.1f%%')
    pie_ax.set_title('Кількість країн виробників вакцини')

    # graph
    graph_ax.plot(mnf, mnf_count, marker='o')
    graph_ax.set_xlabel('назва вакцини')
    graph_ax.set_ylabel('Кількість підрядників')
    graph_ax.set_title('Графік залежності вакцини від заводу виробника')
    graph_ax.set_xticklabels(mnf, rotation=30)
    for chn, count in zip(mnf, mnf_count):
        graph_ax.annotate(count, xy=(chn, count), xytext=(7, 2), textcoords='offset points')

plt.get_current_fig_manager().resize(1400, 600)
plt.show()