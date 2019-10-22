import unittest

from functools import reduce

# add src to the python path
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[2]
sys.path.append(str(root))

from src.datatypes.Real import Real

from src.parser.SBMLTokenizer import SBMLTokenizer

class TokenizerTests(unittest.TestCase):

    tokenizer = SBMLTokenizer()

    def test_parse_reals(self):
        test_input = [
                "-3.14",
                "3.14",
                "0.3e1",
                "-17.02",
        ]
        expected = [
            (Real(-3.14),  'REAL'),
            (Real(3.14),   'REAL'),
            (Real(3.0),   'REAL'),
            (Real(-17.02), 'REAL'),
        ]
        results = reduce(lambda x,y : x+y,
                         map(lambda x: self.tokenizer.test(x),
                             test_input))
        # extract only the value and type
        results = list(map(lambda x: (x.value, x.type), results))
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()
