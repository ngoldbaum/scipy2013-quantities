import numpy as np
import yt.units.yt_array as yta

import base

class BenchYTUnits(base.BenchModule):
    facts = {
        'LOC': 2496,
        'First Release': "N/A",
        "Most recent release": "N/A",
        "Implementation": "Subclass",
        "URL": "http://yt-project.org",
        "PyPI": "yt",
    }

    @property
    def name(self):
        return yta.__name__

    @property
    def make_syntax(self):
        return "constructor"

    def make(self, ndarray, units):
         return yta.YTArray(ndarray, input_units=units)

if __name__ == '__main__':
    import warnings
    warnings.simplefilter('ignore')
    np.seterr(all='ignore')
    base.bench(BenchYTUnits)
