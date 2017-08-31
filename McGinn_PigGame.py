import random

class Dice(object):
    """
    @Class: Dice
    @Description:
        Represents a single "die" with X number of sides.
    @Methods:
        Roll - Rolls the dice and returns a value between 1 and "number of sides"
    """
    def __init__(self, num_sides=6):
        self.NumSides = num_sides

    def Roll(self):
        return random.randint(1, self.NumSides)

##############################################################################
##############################################################################


class PigDice(object):
    """
    @Class: PigDice
    @Description:
        Represents the game of pig (dice game)
    @Methods:
        Roll - Rolls the "die" or "dice" and returns a list of rolled values
    """
    def __init__(self, num_dice=1, dice_sides=6, skunk_value=0):
        self.NumDice = num_dice
        self.DiceSides = dice_sides
        self.DiceList = []
        self.SkunkValue = skunk_value
        for i in range(self.NumDice):
            self.DiceList.append(Dice(self.DiceSides))

    def Roll(self):
        """
        @Method: Roll
        @Description:
            One roll in a pig game, with 1 to NumDice per roll
        @Returns: int: [0=skunk value occured, total of all dice otherwise]
        """
        scores = []
        for d in self.DiceList:
            scores.append(d.Roll())
            if self.SkunkValue in scores:
                return 0
        return sum(scores)

class LeaderBoard(object):
    """
    @Class: LeaderBoard
    @Description:
        A global list of all players
    @Methods:
    """
    __shared_state = {}

    def __init__(self, player=None):
        self.__dict__ = self.__shared_state

        if len(self.__shared_state.keys()) == 0:
            self.players = {}

        if not player is None:
            self.players[player.name] = player

    def __str__(self):
        s = ''
        for name, p in self.players.items():
            s += p.__str__()
            s += ',\n'

        return s

    def Find(self, name, key):
        """
        @Method: Find
        @Description:
          Retreive a key value from player.
          e.g. score = leaderboard.Find('Bob','Score)
               total_rolls = leaderbard.Find('Sue','tot_rolls')
      @Returns: Mixed (whatever type the value is from the player)
      """
        if not name in self.players:
            return None
        else:
            return self.players[name][key]

        return None

    def print_leaderBoard(self):
        pass

class Player(object):
    """
    @Class: Player
    @Description:
      Represents a single player for our pig game
    @Methods:

    """
    def __init__(self, name=None, rolls=6, strat = None):
        self.name = name                        # Players name
        self.score = 0                          # Players score
        self.avg_rolls_per_round = 0            # average rolls per round
        self.avg_score_per_round = 0            # average score per round
        self.tot_rolls = 0                      # total rolls
        self.round_score = 0                    # single (last) round score
        self.round_rolls = 0                    # single (last) round rolls
        self.strategy = strat                   # strategy name if any
        self.leaderBoard = LeaderBoard(self)    # global instance of all players
        self.dice = PigDice()                   # instance of dice class
        self.MaxRolls = rolls
        if self.strategy == "ChaosSprint":
            #chaos sprint may decide to sprint immediately or not at all
            self.sprintScore = random.randint(0, 100)
        else:
            self.sprintScore = 75
            

    def Roll(self):
        
        if not self.strategy:
            self.RandomRoll()
        else:
            self.StratRoll()

    def RandomRoll(self, max_rolls=None):
        self.round_score = 0
        self.round_rolls = 0
        if not max_rolls:
            max_rolls = self.MaxRolls
        for i in range(random.randint(1, max_rolls)):
            self.round_rolls += 1
            roll = self.dice.Roll()
            if roll == 0:
                self.round_rolls = 0
                break
            self.round_score += roll
        self.score += self.round_score
        self.tot_rolls += self.round_rolls

    def StratRoll(self):
        """
        Method: StratRoll
        Description: player will roll according to their strategy,
            -Aggressive players are shooting for a target score above 36 and below 60
                this ensures the aggresive player rolls more than 6 times but not too many
            -Conservative players will only roll a maximum of 6 times
            -Sprint to finish players will sprint to finish at their sprint score, playing conservatively
                otherwise
            -ChaosSprint players will randomly roll until they reach a random value and then they will attempt to
                sprint to finish.  I just thought this would be a fun strategy

        """
        self.round_score = 0
        self.round_rolls = 0

        #Aggresive strategy
        if self.strategy == "Aggressive":

            #ensures a slightly varied number of rolls
            while self.round_score < random.randint(36, 60):
                self.round_rolls += 1
                roll = self.dice.Roll()
                if roll == 0:
                    self.round_score = 0
                    break
                self.round_score += roll

        #Conservative strategy
        elif self.strategy == "Conservative":

            #varied number of rolls but never more than 6
            while self.round_rolls <= random.randint(1, 6):
                self.round_rolls += 1
                roll = self.dice.Roll()
                if roll == 0:
                    self.round_score = 0
                    break
                self.round_score += roll

        elif self.strategy == "Sprint":

            #will play conservatively until the score of 75 is reached
            if self.score < self.sprintScore:
                while self.round_rolls <= random.randint(1, 6):
                    self.round_rolls += 1
                    roll = self.dice.Roll()
                    if roll == 0:
                        self.round_score = 0
                        break
                    self.round_score += roll
            else:
                while self.score + self.round_score < 100:
                    self.round_rolls += 1
                    roll = self.dice.Roll()
                    if roll == 0:
                        self.round_score = 0
                        break
                    self.round_score += roll

        #ChaosSprint
        elif self.strategy == "ChaosSprint":

            #will roll in a randomly until a random score is reached
            if self.score < self.sprintScore:
                while self.round_score <= random.randint(1, 100):
                    self.round_rolls += 1
                    roll = self.dice.Roll()
                    if roll == 0:
                        self.round_score = 0
                        break
                    self.round_score += roll
            else:
                while self.score + self.round_score < 100:
                    self.round_rolls += 1
                    roll = self.dice.Roll()
                    if roll == 0:
                        self.round_score = 0
                        break
                    self.round_score += roll


        self.score += self.round_score
        self.tot_rolls += self.round_rolls



    def NewGame(self):
        self.round_score = 0
        self.round_rolls = 0
        self.score = 0
        self.tot_rolls = 0


    def __str__(self):
        return "[Name:%s, Score:%d, Arpr:%s Aspr:%s, Tr:%s, Rs:%s, Rr:%s, Strat:%s]" % (self.name, self.score, self.avg_score_per_round, self.avg_rolls_per_round, self.tot_rolls, self.round_score, self.round_rolls, self.strategy)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return None



"""
This Class represents one instance of a game with X players rolling X dice playing to a score of X.
"""
class PigGame(object):
    """
    @Method: Init
    @Description: Initializes a pig game instance
    @Params:
        list: Players - A list of player names
        int: NumDice - Number of dice per roll
        int: RandomRolls - Top value of random range for rolls
        int: TargetScore - Target score to trigger a winner
    @Returns: None
    """
    def __init__(self, **kwargs):
        self.Players = []                           # player dictionary
        self.NumDice = kwargs['num_dice']           # number of dice per roll
        self.RandomRollsMax = kwargs['random_roles']   # max num random rolls
        self.TargetScore = kwargs['target_score']   # game winning score
        self.WinnerName = None                      # no winner yet
        self.GameRounds = 0


        # initialize all players
        self.AddPlayers(kwargs['players'])


    def __str__(self):
        string = ""
        for obj in self.Players:
            string += obj.__str__() + "\n"
        return string


    def AddPlayers(self, players):
        """
        @Method: AddPlayers
        @Description: Adds a new player or players to the game
            Example: {
                       'bob':<player_object>
                       'sue':<player_object>
                     }
        @Params: [] - players
        @Returns: None
        """
        if not type(players) == list:
            self.Players.append(players)
        else:
            for p in players:
                self.Players.append(p)


    def RunGame(self):
        """
        @Method: WinnerExists
        @Description: Checks to see if a player has acheived the target score.
        @Params:None
        @Returns: bool
        """

        # Main game loop
        random.shuffle(self.Players)
        self.GameRounds = 0
        while not self.WinnerExists():
            for PlayerObj in self.Players:
                PlayerObj.Roll()
            self.GameRounds += 1
            #print(self)


    def WinnerExists(self):
        """
        @Method: WinnerExists
        @Description: Checks to see if a player has acheived the target score.
        @Params:None
        @Returns: bool
        """
        for p in self.Players:
            if p.score >= self.TargetScore:
                return True
            return False

    def NewGame(self):
        for p in self.Players:
            p.NewGame()


    def Winner(self):
        """
        @Method: Winner
        @Description: Returns the winner, if there is one.
        @Params:None
        @Returns: [string,None]: Players name or None
        """
        for p in self.Players:
            if p.score >= self.TargetScore:
                return p

            return None


players = [Player('Bob', 4, "Aggressive"), Player('Sue', 4, "Conservative"), Player('Dax', 4, "Sprint"), Player('Ann', 4, "ChaosSprint")]
kwargs = {'num_dice':1, 'random_roles':6, 'target_score':100, 'players':players}
pg = PigGame(**kwargs)

Winners = {}

runs = 1000
P = PigGame(**kwargs)
for i in range(runs):
    P.RunGame()
    winner = P.Winner()
    if not winner in Winners:
        Winners[winner] = []
    Winners[winner].append(P.GameRounds)
    P.NewGame()

print("(Name, Strategy, percent)")
for winner, wins in Winners.items():
    print(winner.name, winner.strategy, (len(wins)*100)/runs)