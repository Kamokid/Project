from enum import Enum
import pygame
from models import *

class GameEngine:
    """ Game engine to coordinate the interactions between the models """
    def __init__(self):
        """ Initialize GameEngine settings """
        self.deck = Deck()
        self.deck.shuffle()
        self.stock = Stock()
        self.talon = Talon()
        self.foundation1 = Foundation()
        self.foundation2 = Foundation()
        self.foundation3 = Foundation()
        self.foundation4 = Foundation()
        self.tableau1 = Tableau()
        self.tableau2 = Tableau()
        self.tableau3 = Tableau()
        self.tableau4 = Tableau()
        self.tableau5 = Tableau()
        self.tableau6 = Tableau()
        self.tableau7 = Tableau()
        self.deal()
    
    def deal(self):
        # initial = self.deck.length()
        for i in range(24):
            self.stock.firstDealStock(self.deck)
        
        self.tableau1.firstDealTableau(self.deck)
        
        for i in range(2):
            self.tableau2.firstDealTableau(self.deck)
        for i in range(3):
            self.tableau3.firstDealTableau(self.deck) 
        for i in range(4):
            self.tableau4.firstDealTableau(self.deck)
        for i in range(5):
            self.tableau5.firstDealTableau(self.deck)
        for i in range(6):
            self.tableau6.firstDealTableau(self.deck) 
        for i in range(7):
            self.tableau7.firstDealTableau(self.deck)  
    
    def addToTableau(self, click):
        # Check if the top card of the talon can be added to tableau1
        if self.talon[-1].color == self.tableau1[-1].color:
            self.tableau1.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau1
        for tableau in [self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color == self.tableau1[-1].color:
                self.tableau1.add(tableau.moveTop())
    
        # Check if the top card of any foundation pile can be added to tableau1
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau1[-1].color:
              self.tableau1.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau2
        if self.talon[-1].color == self.tableau2[-1].color:
            self.tableau2.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau2
        for tableau in [self.tableau1, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color == self.tableau2[-1].color:
                self.tableau2.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau2
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau2[-1].color:
              self.tableau2.add(foundation.moveTop())
        
        # Check if the top card of the talon can be added to tableau3
        if self.talon[-1].color == self.tableau3[-1].color:
            self.tableau3.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau3
        for tableau in [self.tableau1, self.tableau2, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color == self.tableau3[-1].color:
                self.tableau3.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau3
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau3[-1].color:
              self.tableau3.add(foundation.moveTop())
        
        # Check if the top card of the talon can be added to tableau4
        if self.talon[-1].color == self.tableau4[-1].color:
            self.tableau4.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau4
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color == self.tableau4[-1].color:
                self.tableau4.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau4
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau4[-1].color:
              self.tableau4.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau5
        if self.talon[-1].color == self.tableau5[-1].color:
            self.tableau5.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau5
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau6, self.tableau7]:
            if tableau[-1].color == self.tableau5[-1].color:
                self.tableau5.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau5
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau5[-1].color:
              self.tableau5.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau6
        if self.talon[-1].color == self.tableau6[-1].color:
            self.tableau6.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau6
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau7]:
            if tableau[-1].color == self.tableau6[-1].color:
                self.tableau6.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau6
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau6[-1].color:
              self.tableau6.add(foundation.moveTop())
          
        # Check if the top card of the talon can be added to tableau7
        if self.talon[-1].color == self.tableau7[-1].color:
            self.tableau7.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau7
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6]:
            if tableau[-1].color == self.tableau7[-1].color:
                self.tableau7.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau7
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color == self.tableau7[-1].color:
              self.tableau7.add(foundation.moveTop())

    def addToEmptyTableau(self, click):
        
        # Check if the tableau1 is empty
        if not self.tableau1:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau1.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau1.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau1.add(foundation.moveTop())
      
        # Check if the tableau2 is empty
        if not self.tableau2:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau2.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau2.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau2.add(foundation.moveTop())

        # Check if the tableau3 is empty
        if not self.tableau3:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau3.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau2, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau3.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau3.add(foundation.moveTop())
          
        # Check if the tableau4 is empty
        if not self.tableau4:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau4.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau4.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau4.add(foundation.moveTop())

        # Check if the tableau5 is empty
        if not self.tableau5:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau5.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau5.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau5.add(foundation.moveTop())

        # Check if the tableau6 is empty
        if not self.tableau6:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau6.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau6.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau6.add(foundation.moveTop())

        # Check if the tableau1 is empty
        if not self.tableau7:
            # Check if the top card of the talon is a King
            if self.talon[-1].value == 13:
               self.tableau7.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6]:
                if tableau[-1].value == 13:
                  self.tableau7.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 13:
                 self.tableau7.add(foundation.moveTop())

    def addToEmptyFoundation(self, click):
        
        # Check if the foundation1 is empty
        if not self.foundation1:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation1.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation1.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].color == 1:
                 self.foundation1.add(foundation.moveTop())

        # Check if the foundation2 is empty
        if not self.foundation2:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation2.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation2.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self. foundation3, self.foundation4]:
              if foundation[-1].color == 1:
                 self.foundation2.add(foundation.moveTop())

          # Check if the foundation3 is empty
        if not self.foundation3:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation3.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation3.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self.foundation2, self.foundation4]:
              if foundation[-1].color == 1:
                 self.foundation3.add(foundation.moveTop())
        
        # Check if the foundation4 is empty
        if not self.foundation4:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation4.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation4.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self.foundation2, self. foundation3]:
              if foundation[-1].color == 1:
                 self.foundation4.add(foundation.moveTop())
        

        
