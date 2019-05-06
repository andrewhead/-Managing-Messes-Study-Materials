import copy
import tabulate
from IPython.core.display import HTML

def display_rows(rows, n=None, hide=None):
    hide = hide if hide else []
    if n != None:
        rows = rows[:n]
    if hide != None:
        rows = copy.deepcopy(rows)
        for row in rows:
            for col in hide:
                del(row[col])
    display(HTML(tabulate.tabulate(rows, headers="keys", tablefmt="html")))
    
def count(categorical_list):
    counts = {}
    for i in categorical_list:
        if i is None:
            continue
        counts[i] = counts[i] + 1 if i in counts else 1
    return zip(*counts.items())