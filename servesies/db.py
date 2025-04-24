import asyncpg
import asyncio
from bot.load_conf import *

class DB:
    def __init__(self, host, user, password, dbname, port):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.port = port

    async def connect_db(self):
        con = await asyncpg.connect(
            database=self.dbname,
            user=self.user,
            host=self.host,
            password=self.password,
            port=self.port
        )
        return con

    async def insert_db(self, link):
        connect = await self.connect_db()
        await connect.execute("INSERT INTO vacancy_links (link) VALUES ($1)", link)
        await connect.close()

    async def select_urls(self):
        connect = await self.connect_db()
        rows = await connect.fetch("SELECT * FROM vacancy_links")
        urls_list = [row[0] for row in rows]
        await connect.close()
        return urls_list

    async def create_work_table(self):
        connect = await self.connect_db()
        await connect.execute(
            "CREATE TABLE IF NOT EXISTS vacancy_values (id SERIAL PRIMARY KEY, v_name VARCHAR(255), v_company VARCHAR(255), salary VARCHAR(255), exp VARCHAR(255), type VARCHAR(255), requirements VARCHAR(255), reg_date VARCHAR(255), link TEXT)"
        )
        await connect.close()

    async def insert_in_work(self, name, company, salary, exp, type_, req, r_date, link):
        connect = await self.connect_db()
        await connect.execute(
            "INSERT INTO vacancy_values (v_name,v_company,salary,exp,type,requirements,reg_date,link) VALUES ($1,$2,$3,$4,$5,$6,$7,$8)",
            name, company, salary, exp, type_, req, r_date, link
        )
        await connect.close()

    async def select_all_exp(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT exp FROM vacancy_values WHERE exp != 'Не указано'")
        exp_list = [row['exp'].strip() for row in data]
        await connect.close()
        return exp_list

    async def select_work_type(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT type FROM vacancy_values WHERE type != 'Не указано'")
        data_list = [row[0].replace('Формат работы: ', '') for row in data]
        await connect.close()
        return data_list

    async def select_all_from_work(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT * FROM vacancy_values")
        await connect.close()
        result = [
            {
                'name': row['v_name'],
                'company': row['v_company'],
                'salary': row['salary'],
                'experience': row['exp'],
                'work_type': row['type'].replace('Формат работы: ', '').strip(),
                'requirements': row['requirements'],
                'registration_date': row['reg_date'],
                'link': row['link']
            }
            for row in data
        ]

        return result

    async def select_lang_num(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT * FROM languages")
        ret_list = {row['lang_name']: row['vacancies_amt'] for row in data}
        await connect.close()
        return ret_list

    async def select_exp(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT * FROM experience")
        res_list = {row['lang_name']: {'None exp': row['no_exp'], '1-3': row['one_to_three_years'],
                                       '3-6': row['three_to_six_years'], '>6': row['six_years']} for row in data}
        await connect.close()
        return res_list

    async def reqs_cs(self):
        connect = await self.connect_db()
        data = await connect.fetch("SELECT req_name, vacancies_amt FROM secondary_requirements WHERE lang_name = 'C#'")
        res_dict = {row[0]: row[1] for row in data}
        return res_dict

    async def reqs_pyt(self):
        connect = await self.connect_db()
        data = await connect.fetch(
            "SELECT req_name, vacancies_amt FROM secondary_requirements WHERE lang_name = 'python'")
        res_dict = {row[0]: row[1] for row in data}
        return res_dict

    async def reqs_java(self):
        connect = await self.connect_db()
        data = await connect.fetch(
            "SELECT req_name, vacancies_amt FROM secondary_requirements WHERE lang_name = 'java'")
        res_dict = {row[0]: row[1] for row in data}
        return res_dict

    async def reqs_js(self):
        connect = await self.connect_db()
        data = await connect.fetch(
            "SELECT req_name, vacancies_amt FROM secondary_requirements WHERE lang_name = 'javascript'")
        #res_dict = {row[0]: row[1] for row in data}
        return data

    async def select_info_exp(self):
        connect = await self.connect_db()
        data = await connect.fetch(
            "SELECT v_name, v_company, salary, type, requirements, link FROM vacancy_values WHERE exp = '1–3 года'")
        res_data = [[row['v_name'], row['v_company'], row['salary'], row['type'], row['requirements'], row['link']] for row in data]
        return res_data


db = DB(password=PASSW, host=HOST, user=USER, port=PORT, dbname=DB)


"""async def main():
    data = await db.select_info_exp()
    print(data)


asyncio.run(main())"""
