'''
This is Symbol class.
This class takes the symbol from players
'''
class Symbol:
    # declaring class variables
    symbol = ''
    default_symbols = ['X', 'O']
    selected_symbols = list()

    # constructor: takes valid symbol from player
    def __init__(self, symbol_index, player_name, selected_symbols):
        is_valid = False
        symbol = ''
        while not is_valid:
            symbol = input('Enter your preferred symbol ({0}): '.format(player_name))
            if not symbol:
                symbol = self.default_symbols[symbol_index]
            print(symbol, selected_symbols)
            if len(symbol) == 1:
                if symbol not in selected_symbols:
                    self.set_symbol(symbol)
                    selected_symbols.append(symbol)
                    self.set_selected_symbols(selected_symbols)
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

    # getter method to return selected_symbols from class variable
    def get_selected_symbols(self):
        return self.selected_symbols

    # setter method to set selected_symbols in class variable
    def set_selected_symbols(self, selected_symbols):
        self.selected_symbols = selected_symbols
