from amplpy import AMPL

def run_ampl():
    ampl = AMPL()
    ampl.solve(solver="cplex")