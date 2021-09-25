
from confluent_kafka.avro import AvroProducer
import json

from utils import utils


class TeamProducer:

    def __init__(self):
        self.config = {
            "bootstrap.servers": "localhost:9092",
            "schema.registry.url": "http://localhost:8081"
        }
        self.topic = "team-topic"
        key_schema, value_schema = utils.load_team_avro_schema_from_file("./schema/team_schema.avsc")
        self.producer = AvroProducer(
            self.config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )

    def send(self, key: str, val: json):
        self.producer.produce(topic=self.topic, key=key, value=val)

    def send_all(self, teams):
        for t in teams:
            self.send(t.team_id, t.to_json())
        self.producer.flush()
