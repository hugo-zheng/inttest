#!/usr/bin/python

import os, sys, base64,time
import pykka
from pykka import ActorRegistry
from pykka.gevent import GeventActor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.misc import parse_message, generate_message

def get_player(pid):
    player = ActorRegistry.get_by_urn(pid)
    if player is None:
        player =  Player.start(pid)

    return player

def get_game(pid):
    player = get_player(pid)
    if player.game is None:
        player.game = Game.start(pid)
    return player.game


class BaseActor(pykka.ThreadingActor):
#class BaseActor(GeventActor()):

    def __init__(self, urn=None):
        super(BaseActor, self).__init__()
        if urn:
            self.actor_urn = urn

    def on_start(self):
        self.actor_ref.actor_urn = self.actor_urn
        ActorRegistry.unregister(self.actor_ref)
        ActorRegistry.register(self.actor_ref)
3


class Player(BaseActor):
    def __init__(self, pid=None):
        super(Player, self).__init__(pid)
        self.pid = pid

    def on_receive(self, message):
        mode, event = parse_message(message)
        if mode == 'game':
            g = Game.start()
            return g.ask({'event': event})
        return None



class Game(BaseActor):
    def __init__(self, urn=None):
        super(Game, self).__init__(urn)
        pass

    def on_receive(self, message):
        e = message.get('event')

        return generate_message(e)

    def sign_in(self, message):
        print ('game receive %s' % message)

        self.stop()

