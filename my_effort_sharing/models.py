from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
努力量の決定ゲーム（シェア有）
"""


class Constants(BaseConstants):
    name_in_url = 'my_effort_sharing'
    players_per_group = 4
    num_rounds = 5

    max_effort = c(100)

    #変数の定義
    random_numbers = 40 
    reward_low = 70
    reward_even = 50
    reward_high = 140
    endowment1 = 40
    endowment2 = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    effort_amount = models.CurrencyField()
    
    def set_payoffs(self):
        import random

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)

        p1_yeild = p1.effort_amount + Constants.endowment1 +  random.uniform(0,40) 
        p2_yeild = p2.effort_amount + Constants.endowment1 +  random.uniform(0,40) 
        p3_yeild = p3.effort_amount + Constants.endowment2 +  random.uniform(0,40) 
        p4_yeild = p4.effort_amount + Constants.endowment2 +  random.uniform(0,40) 

        team_type = random.randint(1,2)

        if team_type == 1 :
            team1_yeild = p1_yeild + p3_yeild
            team2_yeild = p2_yeild + p4_yeild


            if team1_yeild > team2_yeild :
                p1.payoff = Constants.reward_high - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_low - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_high - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_low - p4.effort_amount * p4.effort_amount * 0.01

            elif team1_yeild == team2_yeild :
                p1.payoff = Constants.reward_even - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_even - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_even - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_even - p4.effort_amount * p4.effort_amount * 0.01

            else :
                p1.payoff = Constants.reward_low - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_high - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_low - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_high - p4.effort_amount * p4.effort_amount * 0.01

        else :
            team1_yeild = p1_yeild + p4_yeild
            team2_yeild = p2_yeild + p3_yeild

            if team1_yeild > team2_yeild :
                p1.payoff = Constants.reward_high - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_low - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_low - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_high - p4.effort_amount * p4.effort_amount * 0.01

            elif team1_yeild == team2_yeild :
                p1.payoff = Constants.reward_even - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_even - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_even - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_even - p4.effort_amount * p4.effort_amount * 0.01

            else :
                p1.payoff = Constants.reward_low - p1.effort_amount * p1.effort_amount * 0.01
                p2.payoff = Constants.reward_high - p2.effort_amount * p2.effort_amount * 0.01
                p3.payoff = Constants.reward_high - p3.effort_amount * p3.effort_amount * 0.01
                p4.payoff = Constants.reward_low - p4.effort_amount * p4.effort_amount * 0.01



class Player(BasePlayer):
    effort_amount = models.CurrencyField()

    effort_amount = models.CurrencyField(
        choices=currency_range(0, Constants.max_effort, c(1)),
    )
