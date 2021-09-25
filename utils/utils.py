
import requests
from confluent_kafka import avro


def get_teams():
    for x in requests.get('https://api.opendota.com/api/teams').json():
        yield x


def load_team_avro_schema_from_file(url: str) -> tuple:
    schema = '{"type": "int"}'
    key_s = avro.loads(schema)
    v_s = avro.load(f"{url}")

    return key_s, v_s
