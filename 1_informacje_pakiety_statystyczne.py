import pkgutil as pu
import numpy as np
import matplotlib as mpl
import scipy as sp
import pydoc

print("NumPy version:", np.__version__)
print("SciPy version:", sp.__version__)
print("MatPlotLib version:", mpl.__version__)


def clean(astr):
    s = astr
    s = " ".join(s.split())
    s = s.replace('=', '')

    return s
# wypisuje opis poszczególnych elementów pakietu


def print_desc(prefix, pkg_path):
    for pkg in pu.iter_modules(path=pkg_path):  # iteruje przez kolejne elementy wchodzące w skład modułu
        name = prefix + "." + pkg[1]

        if pkg[2] is True:
            try:
                docstr = pydoc.plain(pydoc.render_doc(name))  # zwraca opis poszczególnych modułów
                docstr = clean(docstr)
                start = docstr.find("DESCRIPTION")
                docstr = docstr[start: start + 440]
                print(name, docstr)
            except:
                continue


print_desc("numpy", np.__path__)
print()
print()
print()
print_desc("scipy", sp.__path__)
print()
print()
print()
print_desc("matplotlib", mpl.__path__)