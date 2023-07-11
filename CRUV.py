import random


class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

    @property
    def probability(self):
        return self.bowling * self.batting * self.fielding * self.running * self.experience

    def __repr__(self):
        return f"Player({self.name}, {self.probability})"


class Teams:
    def __init__(self, players):
        self.players = players

    def select_captain(self):
        return random.choice(self.players)

    def send_next_player_to_field(self):
        return random.choice(self.players)

    def choose_bowler_for_over(self):
        return random.choice(self.players)

    def decide_batting_order(self):
        return random.shuffle(self.players)


class Field:
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

    def __repr__(self):
        return f"Field({self.field_size}, {self.fan_ratio}, {self.pitch_conditions}, {self.home_advantage})"


class Umpire:
    def __init__(self, field):
        self.field = field

    def predict_outcome_of_ball(self, players):
        probabilities = []
        for player in players:
            probabilities.append(player.probability)
        return random.choice(probabilities)

    def keep_track_of_scores(self, runs, wickets, overs):
        self.runs = runs
        self.wickets = wickets
        self.overs = overs


class Commentator:
    def __init__(self, match):
        self.match = match

    def provide_commentary_for_ball(self, ball_number, outcome):
        print(f"Ball number {ball_number}: {outcome}")

    def provide_commentary_for_over(self, over_number, runs, wickets):
        print(f"Over number {over_number}: {runs} runs, {wickets} wickets")


class Match:
    def __init__(self, teams, field, umpire, commentator):
        self.teams = teams
        self.field = field
        self.umpire = umpire
        self.commentator = commentator

    def start_match(self):
        for over in range(1, 7):
            balls_count = 0  # Reset the ball count to 0 at the beginning of each over
            for ball in range(1, 7):
                balls_count += 1  # Increment the ball count
                outcome = self.umpire.predict_outcome_of_ball(self.teams.players)
                self.commentator.provide_commentary_for_ball(balls_count, outcome)  # Ball number starts from 1
                if balls_count % 6 == 0:  # Check if 6 balls are completed
                   
                    print("**************Over***************")  
                    print("\n")




if __name__ == "__main__":
    players = [
        Player("Virat Kohli", 0.2, 0.8, 0.99, 0.8, 0.29),
        Player("Hardik Pandya", 0.31, 0.9, 0.98, 0.7, 0.84),
        Player("Surya Kumar Yadav", 0.47, 0.80, 0.97, 0.61, 0.7),
    ]
    teams = Teams(players)
    field = Field(100, 50, "good", 0.5)
    umpire = Umpire(field)
    match = Match(teams, field, umpire, None)  # Passing None as commentator for now
    commentator = Commentator(match)  # Creating the commentator instance
    match.commentator = commentator  # Assigning the commentator to the match instance
    match.start_match()
