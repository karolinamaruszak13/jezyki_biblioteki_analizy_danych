import string


class FakeDFA:
    def __init__(self):
        self.counter = 0
        self.PUNCTUATIONS = string.ascii_lowercase + "~)|&01("
        self.fake_dfa = {0: {'~': 0, '(': self._add_parenthesis_counter, '0': 1, '1': 1, ')': 2, '|': 2, '&': 2},
                         1: {')': self._sub_parenthesis_counter, '|': 0, '&': 0},
                         2: {}}
        self._fill_state_0()
        self._fill_state_1()
        self._fill_state_2()
        self._initial_state = 0
        self._accepting_states = [1]



    def _fill_state_0(self):
        for letter in string.ascii_lowercase:
            self.fake_dfa[0][letter] = 1

    def _fill_state_1(self):
        punctuations = self.PUNCTUATIONS.replace(")|&", "")
        for letter in punctuations:
            self.fake_dfa[1][letter] = None

    def _fill_state_2(self):
        for letter in self.PUNCTUATIONS:
            self.fake_dfa[2][letter] = None

    def _add_parenthesis_counter(self):
        self.counter += 1
        return 0

    def _sub_parenthesis_counter(self):
        if self.counter == 0:
            return None
        else:
            self.counter -= 1

        return 1

    def _parser(self, input):
        input = input.replace(" ", "")
        for letter in input:
            if letter not in self.PUNCTUATIONS:
                return False, input
        return True, input

    @staticmethod
    def accepts(input):
        fake_DFA_object = FakeDFA()
        flag, input = fake_DFA_object._parser(input)
        if flag:
            state = fake_DFA_object._initial_state
            for c in input:
                state = fake_DFA_object.fake_dfa[state][c]
                if callable(state):
                    state = state()
                if state is None:
                    return False
            return state in fake_DFA_object._accepting_states if fake_DFA_object.counter == 0 else False
        else:
            return False


print(FakeDFA.accepts("a)|(b") == False)
print(FakeDFA.accepts("a") == True)
print(FakeDFA.accepts("a|b") == True)
print(FakeDFA.accepts("a & b | a") == True)
print(FakeDFA.accepts("(a &b) |c&~d") == True)
print(FakeDFA.accepts("~~a") == True)
print(FakeDFA.accepts("~(a|c)") == True)
print(FakeDFA.accepts("(a)") == True)
print(FakeDFA.accepts("~") == False)
print(FakeDFA.accepts("a|") == False)
print(FakeDFA.accepts("A|B") == False)
print(FakeDFA.accepts("a|&b") == False)
print(FakeDFA.accepts("b~") == False)
print(FakeDFA.accepts("(a|b") == False)
print(FakeDFA.accepts("a|b)") == False)









