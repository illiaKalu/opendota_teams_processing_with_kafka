from time import sleep

from entities.team import Team

from producer.team_producer import TeamProducer
from utils import utils

if __name__ == '__main__':
    team_producer = TeamProducer()
    generator = utils.get_teams()
    for _ in range(0, 5):
        team_producer.send_all(Team.create_teams(generator))
        sleep(2)



