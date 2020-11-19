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
    name_in_url = 'my_effort_sharing_MIN_v50'
    players_per_group = 4
    num_rounds = 5

    max_effort = (100)

    #変数の定義
    random_numbers = 40 
    reward_low = 70
    reward_even = 50
    reward_high = 140
    endowment1 = 40
    endowment2 = 0


class Subsession(BaseSubsession):
        def creating_session(self):
        
            self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    effort_amount = models.CurrencyField()
    
    def set_payoffs(self):
        import random

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)

        team_type = random.randint(1,2)

        if team_type == 1 :
            p1.yeild = p1.effort_amount*0.5 + Constants.endowment1 +  random.uniform(0,40) 
            p2.yeild = p2.effort_amount*0.5 + Constants.endowment1 +  random.uniform(0,40) 
            p3.yeild = p3.effort_amount + p1.effort_amount*0.5 + Constants.endowment2 +  random.uniform(0,40) 
            p4.yeild = p4.effort_amount + p2.effort_amount*0.5 + Constants.endowment2 +  random.uniform(0,40) 

            team1_yeild = min(p1.yeild,p3.yeild)
            team2_yeild = min(p2.yeild,p4.yeild)
        
            p1.team = 1
            p2.team = 2
            p3.team = 1
            p4.team = 2

            p1.team_member = 3
            p2.team_member = 4
            p3.team_member = 1
            p4.team_member = 2

            p1.team_members_yeild = p3.yeild
            p2.team_members_yeild = p4.yeild
            p3.team_members_yeild = p1.yeild
            p4.team_members_yeild = p2.yeild

            p1.effort_sharing_amount = p1.effort_amount*0.5
            p2.effort_sharing_amount = p2.effort_amount*0.5
            p3.effort_sharing_amount = p1.effort_amount*0.5
            p4.effort_sharing_amount = p2.effort_amount*0.5

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
            p1.yeild = p1.effort_amount*0.5 + Constants.endowment1 +  random.uniform(0,40) 
            p2.yeild = p2.effort_amount*0.5 + Constants.endowment1 +  random.uniform(0,40) 
            p3.yeild = p3.effort_amount + p2.effort_amount*0.5 + Constants.endowment2 +  random.uniform(0,40) 
            p4.yeild = p4.effort_amount + p1.effort_amount*0.5 + Constants.endowment2 +  random.uniform(0,40) 
            
            team1_yeild = min(p1.yeild,p4.yeild)
            team2_yeild = min(p2.yeild,p3.yeild)

            p1.team = 1
            p2.team = 2
            p3.team = 2
            p4.team = 1

            p1.team_member = 4
            p2.team_member = 3
            p3.team_member = 2
            p4.team_member = 1

            p1.team_members_yeild = p4.yeild
            p2.team_members_yeild = p3.yeild
            p3.team_members_yeild = p2.yeild
            p4.team_members_yeild = p1.yeild

            p1.effort_sharing_amount = p1.effort_amount*0.5
            p2.effort_sharing_amount = p2.effort_amount*0.5
            p3.effort_sharing_amount = p2.effort_amount*0.5
            p4.effort_sharing_amount = p1.effort_amount*0.5

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
    effort_amount = models.IntegerField(min=0, max=100)
    yeild = models.FloatField(initial=0)

    effort_sharing_amount = models.FloatField(initial=0)

    team = models.IntegerField(initial=0)
    team_member = models.IntegerField(initial=0)
    team_members_yeild = models.FloatField(initial=0)
