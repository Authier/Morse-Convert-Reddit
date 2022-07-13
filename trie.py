class Trie_Node:
    def __init__(self, character=None):
        self.character = character
        self.children = {}

class Morse_Trie:
    def __init__(self):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = Trie_Node('A'), Trie_Node('B'), Trie_Node('C'), \
            Trie_Node('D'), Trie_Node('E'), Trie_Node('F'), Trie_Node('G'), Trie_Node('H'), Trie_Node('I'), Trie_Node('J'), Trie_Node('K'), \
                Trie_Node('L'), Trie_Node('M'), Trie_Node('N'), Trie_Node('O'), Trie_Node('P'), Trie_Node('Q'), Trie_Node('R'), Trie_Node('S'), \
                    Trie_Node('T'), Trie_Node('U'), Trie_Node('V'), Trie_Node('W'), Trie_Node('X'), Trie_Node('Y'), Trie_Node('Z')
        
        self.root = Trie_Node(None)
        self.root.children['.'] = E
        self.root.children['_'] = T
        T.children['_'] = M
        T.children['.'] = N
        N.children['_'] = K
        N.children['.'] = D
        K.children['_'] = Y
        K.children['.'] = C
        D.children['_'] = X
        D.children['.'] = B
        M.children['_'] = O
        M.children['.'] = G
        G.children['.'] = Z
        G.children['_'] = Q
        E.children['_'] = A
        E.children['.'] = I
        I.children['_'] = U
        I.children['.'] = S
        S.children['_'] = V
        S.children['.'] = H
        U.children['.'] = F
        A.children['_'] = W
        A.children['.'] = R
        R.children['.'] = L
        W.children['_'] = J
        W.children['.'] = P

class Morse_T:
    def __init__(self, string):
        self.lazy_dict = {
            'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', \
                'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', \
                    'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', \
                        'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..',
        }

        string.upper()
        self.valid_morse = set({'.', '_'})
        self.valid_space = set({'/'})
        self.valid_string = set({chr(char_i) for char_i in range(65, 91)})
        self.string = None
        self.morse = None
        is_morse = False
        is_string = False

        for char in string:
            if char in self.valid_morse or char in self.valid_space:
                is_morse = True
            elif char in self.valid_string:
                is_string = True
                continue
            print(f"INVALID CHARACTER: {char}")
            return

        if (is_morse and is_string) or (not is_morse and not is_string):
            print(f"INVALID: {string}")
            return
        
        if is_morse:
            self.morse = string
        else:
            self.string = string
    
    def find_letter(self, morse):
        if len(morse) == 0:
            return
            
        curr_trie_node = Morse_Trie().root
        for index in range(len(morse)):
            char = morse[index]
            if char in curr_trie_node.children:
                curr_trie_node = curr_trie_node.children[char]
                continue
            print(f"INVALID: {morse} at index {index}")
            return False
        return curr_trie_node.character
    
    def convert_to_string(self):
        if self.morse is None:
            print("INVALID: CURRENTLY STRING")
            return
        
        morse_seperate = self.morse.split("/")
        
        output = ''
        for morse in morse_seperate:
            if self.find_letter(morse):
                output += self.find_letter(morse)
                continue
            return

        print(f"THE TRANSLATED MESSAGE IS: {output}")
        self.string = output
        self.morse = None

    def convert_to_morse(self):
        if self.string is None:
            print("INVALID: CURRENTLY STRING")
            return
        
        to_morse = ''
        for index, char in enumerate(self.string):
            to_morse += f'{self.lazy_dict[char]}/' if index != len(self.string) - 1 else f'{self.lazy_dict[char]}'

        print(f"THE ENCODED MESSAGE IS: {to_morse}")
        self.morse = to_morse
        self.string = None
