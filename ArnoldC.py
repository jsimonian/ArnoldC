# A python3 interperator for ArnoldC

def eval(expr, env):
    return

def evalLine(expr):
    parsed = parse(expr)
    if parsed[1] is None:
        parsed[0]
    else:
        parsed[0](parsed[1])

def truth():
    return
def falsehood():
    return
def ifForm():
    return
def elseForm():
    return
def endIfForm():
    return
def whileForm():
    return
def endWhileForm():
    return
def addOperator():
    return
def subtractOperator():
    return
def multiplyOperator():
    return
def divideOperator():
    return
def moduloOperator():
    return
def equalsOperator():
    return
def greaterThanOperator():
    return
def orOperator():
    return
def andOperator():
    return
def declareMethod():
    return
def declareMethodNonVoid():
    return
def declareParameters():
    return
def returnStatment():
    return
def endDeclareMethod():
    return
def callMethod():
    return
def assignVariableFromMethodCall():
    return
def declareInt():
    return
def setInitialValue():
    return
def beginMain():
    return
def endMain():
    return
def printCommand():
    return
def parseInteger():
    return
def assignVariable():
    return
def setValue():
    return
def endVariableAssignment():
    return
def ParseError():
    return

commands = {
    "I LIED": truth,
    "NO PROBLEMO": falsehood,
    "BECAUSE I'M GOING TO SAY PLEASE": ifForm,
    "BULLSHIT": elseForm,
    "YOU HAVE NO RESPECT FOR LOGIC": endIfForm,
    "STICK AROUND": whileForm,
    "CHILL": endWhileForm,
    "GET UP": addOperator,
    "GET DOWN": subtractOperator,
    "YOU'RE FIRED": multiplyOperator,
    "HE HAD TO SPLIT": divideOperator,
    "I LET HIM GO": moduloOperator,
    "YOU ARE NOT YOU YOU ARE ME": equalsOperator,
    "LET OFF SOME STEAM BENNET": greaterThanOperator,
    "CONSIDER THAT A DIVORCE": orOperator,
    "KNOCK KNOCK": andOperator,
    "LISTEN TO ME VERY CAREFULLY": declareMethod,
    "GIVE THESE PEOPLE AIR": declareMethodNonVoid,
    "I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE": declareParameters,
    "I'LL BE BACK": returnStatment,
    "HASTA LA VISTA, BABY": endDeclareMethod,
    "DO IT NOW": callMethod,
    "GET YOUR ASS TO MARS": assignVariableFromMethodCall,
    "HEY CHRISTMAS TREE": declareInt,
    "YOU SET US UP": setInitialValue,
    "IT'S SHOWTIME": beginMain,
    "YOU HAVE BEEN TERMINATED": endMain,
    "TALK TO THE HAND": printCommand,
    "I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY": parseInteger,
    "GET TO THE CHOPPER": assignVariable,
    "HERE IS MY INVITATION": setValue,
    "ENOUGH TALK": endVariableAssignment,
    "WHAT THE FUCK DID I DO WRONG": ParseError
}

_end = '_end_'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = commands[word]
    return root

t = make_trie(commands.keys())

def parse(cmd):
    current_dict = t
    for i in range(len(cmd)):
        if _end in current_dict:
            return current_dict[_end], cmd[i+1:]
        if cmd[i] in current_dict:
            current_dict = current_dict[cmd[i]]
        else:
            return False
    if _end in current_dict:
        return current_dict[_end], None
    return False
