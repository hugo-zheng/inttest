#! /usr/bin/env python

import pykka, time, random

class PlainActor(pykka.ThreadingActor):
    def __init__(self, name):
        super(PlainActor, self).__init__()
        self.stored_messages = []
        self.name = name

    def on_receive(self, message):
        time.sleep(random.randint(1,5))
        print self.name, message, '\n'
        if message.get('command') == 'get_messages':
            return self.stored_messages
        else:
            self.stored_messages.append(message)


if __name__ == '__main__':
    actor1 = PlainActor.start('111')
    actor2 = PlainActor.start('222')

    print 1
    actor1.tell({'no': 'Norway', 'se': 'Sweden'})
    print 2
    actor1.tell({'a': 3, 'b': 4, 'c': 5})
    actor2.tell({'no': 'Norway', 'se': 'Sweden'})
    print 3
    actor2.tell({'a': 3, 'b': 4, 'c': 5})
    print 4
    #print(actor2.ask({'command': 'get_messages'}))
    #print(actor1.ask({'command': 'get_messages'}))

    actor1.stop()
    actor2.stop()

