import requests
from const import *
import json
import sqlite3


def db_connect():

    con = sqlite3.connect('amrv11.db')
    return con


class DbOperations():

    def __init__(self, con):
        self.connection = con
        self.cursor = self.connection.cursor()

    def create_table(self, table_name):

        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}(Consumer UNIQUE, ImportC1 REAL, ImportC2 REAL, ImportC3 REAL, ImportC4 REAL, ImportC5 REAL, ExportC1 REAL, ExportC2 REAL, ExportC3 REAL, ExportC4 REAL, ExportC5 REAL, BankingC1 REAL, BankingC2 REAL, BankingC3 REAL, BankingC4 REAL, BankingC5 REAL, C001 REAL,    C002 REAL, C003 REAL, C004 REAL, C005 REAL, C006 REAL, C007 REAL)")
        self.connection.commit()

    def write_table(self, tableName, data):

        inject = ','.join('?', * len(data))
        insert_cmd = f"INSERT INTO {tableName} VALUES {inject}"
        self.cursor.execute(insert_cmd, data)

    def __dropTable(self, tableName):

        self.cursor.execute(f'DROP TABLE {tableName}')
        self.connection.commit()


def make_request(method, url, headers, payload=None):

    if method == 'get' and payload is None:
        resp = requests.get(url, headers=headers)
        return resp.json()

    elif method == 'get' and payload:
        resp = requests.get(url, params=payload, headers=headers)
        return resp.json()

    else:
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        return resp.json()


def get_reading(login_data=None, gen_data=None):

    headers = {"Accept": "application/json", "Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    get_auth = make_request('post', LOGIN_URL, headers, payload=login_data)
    token = get_auth['token']
    headers.update({'Authorization': token})
    get_genrep_id = make_request('get', GEN_STATEMENT_URL, headers, payload=gen_data)
    report_id = get_genrep_id[0]['id']
    reading = make_request('get', READINGS_URL.format(report_id), headers)
    return reading


def build_login_payload(serviceNumber, password=None):

    data = {"userName": serviceNumber, "password": os.environ.get('password'), "appClientId": "OA"}
    return data


def build_gen_payload(edc, serviceNumber, month, year):

    payload = {'dummy': '1', 'edc-id': edc, 'service-number': serviceNumber, "statement-month": month,
               'statement-year': year}
    return payload


def main(month, year):

    db = DbOperations(db_connect())
    db.create_table('y' + year)

    consumerList = [{'EDC': '472', 'id': ['079204720584', '079204720585']}]
    for consumer in consumerList:
        edc = consumer['EDC']
        for n in consumer['id']:
            login_data = build_login_payload(n)
            gen_data = build_gen_payload(edc, n, month, year)
            results = get_reading(login_data=login_data, gen_data=gen_data)
            print(results)
            print('----xxxx------')


main('08', '2019')
