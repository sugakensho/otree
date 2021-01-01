from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Explanation(Page):
    def is_displayed(self):
        return self.round_number == 1


class Send(Page):
    
    form_model = 'player'
    form_fields = ['effort_amount']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def total_player_payoff(self):
        self.participant.payoff


page_sequence = [Explanation, Send, ResultsWaitPage, Results]

