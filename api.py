import requests
from const import *
import json
import sqlite3


def db():

    conn = sqlite3.connect('amr.db')


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


def get_reading():

    headers = {"Accept": "application/json", "Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    get_auth = make_request('post', LOGIN_URL, headers, payload=LOGIN_DATA)
    token = get_auth['token']
    headers.update({'Authorization': token})
    get_genrep_id = make_request('get', GEN_STATEMENT_URL, headers, payload=PAYLOAD_GEN_STAT)
    report_id = get_genrep_id[0]['id']
    reading = make_request('get', READINGS_URL.format(report_id), headers)
    return reading


db()
