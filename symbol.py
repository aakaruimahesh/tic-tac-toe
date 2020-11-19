'''
This is Symbol class.
This class takes the symbol from players
'''
class Symbol:
    # declaring class variables
    symbol = ''
    default_symbols = ['X', 'O']
    selected_symbol = list()

    # constructor: takes valid symbol from player
    def __init__(self, symbol_index, player_name):
        is_valid = False
        symbol = ''
        selected_symbol = list()
        while not is_valid:
            symbol = input('Enter your preferred symbol ({0}): '.format(player_name))
            if not symbol:
                symbol = self.default_symbols[symbol_index]
            if len(symbol) == 1:
                if symbol not in selected_symbol:
                    self.set_symbol(symbol)
                    selected_symbol.append(symbol)
                    self.set_selected_symbol(selected_symbol)
                    is_valid = True
                else:
                    print('This symbol is already taken. Please enter another character.')
            else:
                print('Please enter only one character for symbol.')

    # getter method to return symbol from class variable
    def get_symbol(self):
        return self.symbol

    # setter method to set symbol in class variable
    def set_symbol(self, symbol):
        self.symbol = symbol

    # getter method to return selected_symbol from class variable
    def get_selected_symbol(self):
        return self.selected_symbol

    # setter method to set selected_symbol in class variable
    def set_selected_symbol(self, selected_symbol):
        self.selected_symbol = selected_symbol
