"""
File:  dakshhub_python_abc.py
Created By:  Deepak K Gupta (www.CodesBay.com)
Social Handle: @DakshHub @CodesBay
"""
# Abstract Base Classes(ABC) and Abstract Methods in Python
# template of states and events

from abc import ABC, abstractmethod

# The base State
# A template for all states
class State(ABC):

    @abstractmethod
    def in_state(self):
        pass

# Happy State implements in_state()
class HappyState(State):

    def in_state(self):
        print("I am in Happy State")

# Sad State implements in_state()
class SadState(State):

    def in_state(self):
        print("I am in SAD State")

# The base Event
# A template for all Events
class Event(ABC):

    @abstractmethod
    def in_event(self):
        pass

# Lost Money Event
class LostMoney(Event):

    def in_event(self):
        print("I LOST MONEY")

# Received Money Event
class RecvMoney(Event):

    def in_event(self):
        print("I GOT MONEY")

# The Statemachine which is using all the declared
# States and Events
class StateMachine():

    def __init__(self):
        self.currstate = HappyState()

    def current_state(self):
        print(self.currstate.in_state())

    def recv_event(self, event):
        if isinstance(event, LostMoney):
            self.currstate = SadState()
        else:
            self.currstate = HappyState()

# The Test Code to check the State Machine
sm = StateMachine()
sm.current_state()
sm.recv_event(LostMoney())
sm.current_state()
sm.recv_event(RecvMoney())
sm.current_state()
