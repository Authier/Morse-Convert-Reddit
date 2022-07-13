class Tree_Node:
    def __init__(self, character=None, period=None, underscore=None):
        self.character = character
        self.period = period  # left
        self.underscore = underscore  # right

class Morse_Binary_Tree:
    def __init__(self):
        self.root = Tree_Node(None, Tree_Node('E', Tree_Node('I', Tree_Node('S', Tree_Node('H'), Tree_Node('V')), \
            Tree_Node('U', Tree_Node('F'))), Tree_Node('A', Tree_Node('R', Tree_Node('L')), Tree_Node('W', Tree_Node('P'), Tree_Node('J')))), \
                Tree_Node('T', Tree_Node('N', Tree_Node('D', Tree_Node('B'), Tree_Node('X')), Tree_Node('K', Tree_Node('C'), Tree_Node('Y'))), \
                    Tree_Node('M', Tree_Node('G', Tree_Node('Z'), Tree_Node('Q')), Tree_Node('O'))))
        
class Morse_B:
    def __init__(self, string):

        self.lazy_dict = {
            'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', \
                'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', \
                    'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', \
                        'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..',
        }

        self.root = Morse_Binary_Tree().root  # For simplicity

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
            
        curr_tree_node = Morse_Binary_Tree().root
        for index in range(len(morse)):
            char = morse[index]
            if char == '.' and curr_tree_node.period is not None:
                curr_tree_node = curr_tree_node.period
                continue
            elif char == '_' and curr_tree_node.underscore is not None:
                curr_tree_node = curr_tree_node.underscore
                continue
            print(f"INVALID: {morse} at index {index}")
            return False
        return curr_tree_node.character
    
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

