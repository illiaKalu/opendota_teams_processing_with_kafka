from utils import utils


class Team(object):
    def __init__(self, team_id, rating, wins, losses, last_match_time, name, tag, logo_url):
        self.team_id = team_id
        self.rating = rating
        self.wins = wins
        self.losses = losses
        self.last_match_time = last_match_time
        self.name = name
        self.tag = tag
        self.logo_url = logo_url

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    def create_teams(gen, n=5):
        teams = list()
        for _ in range(0, n):
            team = next(gen)
            teams.append(Team(
                team_id=team.get('team_id'),
                rating=team.get('rating'),
                wins=team.get('wins'),
                losses=team.get('losses'),
                last_match_time=team.get('last_match_time'),
                name=team.get('name'),
                tag=team.get('tag'),
                logo_url=team.get('logo_url')
            ))
        return teams
