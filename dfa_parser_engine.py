"""
-Q - states
-sigma - alfabetul
-Delta - tranzitiile
-S - start
-F - multimea de finish
"""
def citire(sigma, delta, St, F, Q):
    f = open("dfa_config_file.txt")
    linie = f.readline()
    while linie:
        linie=linie[:(len(linie)-1)]
        if linie[0] != "#":
            if linie == "Sigma:":
                linie = f.readline()
                while linie != "End\n" and linie != "End":
                    sigma.append(linie[0])
                    linie = f.readline()
            elif linie == "Transitions:":
                linie = f.readline()
                while linie != "End" and linie != "End\n":
                    linie = linie[:(len(linie) - 1)]
                    linie = linie.split(", ")
                    delta_key = linie[0]
                    if delta_key not in delta.keys():
                         delta[delta_key] = {}
                    state_key=linie[2]
                    delta[delta_key][state_key]=linie[1]
                    linie = f.readline()
            elif linie == "States:":
                linie = f.readline()
                while linie != "End" and linie != "End\n":
                    linie = linie[:(len(linie) - 1)]
                    linie = linie.split(", ")
                    if len(linie) != 1:
                        if linie[1] == 'S':
                            St.append(linie[0])

                        elif linie[1] == 'F':
                            F.append(linie[0])
                    Q.append(linie[0])
                    linie = f.readline()
        linie = f.readline()
"""CERINTE VALIDARE:        
    -daca exista S
    -daca F != None
    -existenta a cel putin unui lant de la S la F
    -daca intre 2 state-uri exista o litera care nu apartine lui sigma
    -daca exista un state care nu apartine lui Q
    -dintr-un state nu trb sa plece 2 tranzitii cu aceeasi litera
"""


def exista_lant(state, delta):
    global vizitati
    global ok
    if state in F:
        ok = 1
    else:
        for x in delta[state]:
            sti = int(state[1])
            xi = int(x[1])
            if ok == 0 and vizitati[sti][xi] == 0:
                vizitati[sti][xi] = 1
                exista_lant(x, delta)
    return ok

def apartententa():
    for dict in delta.values():
        for lit in dict.values():
            if lit not in sigma:
                return 0
    for states in delta.keys():
        if states not in Q:
            return 0
    for dict in delta.values():
        for states in dict.keys():
            if states not in Q:
                return 0
    return 1

def aceeasi_lit():
    for dict in delta.values():
        aux= set()
        for lit in dict.values():
            aux.add(lit)
        if len(aux) != len(dict):
            return 0
    return 1

def input_valid(S, F, Q, sigma, delta):
    vizitati = [[0 for x in delta] for y in delta]
    ok = 0
    if S == []:
        return 0
    elif F == None:
        return 0
    elif exista_lant(*S, delta) == 0:
        return 0
    elif apartententa() == 0:
        return 0
    elif aceeasi_lit() == 0:
        return 0
    return 1



sigma = []
delta = {}
S = []
F = []
Q = []
ok = 0

citire(sigma, delta, S, F, Q)
vizitati = [[0 for x in delta] for y in delta]
print(input_valid(S, F, Q, sigma, delta))