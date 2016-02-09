'''
URL: http://www.codewars.com/kata/dont-drink-the-water/train/python
Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]

The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.

'''
import numpy.testing.utils as Test
from itertools import chain

Density = {'H': 1.36, "W": 1.0, 'A': 0.87, 'O': 0.80}
def separate_liquids(glass):
    if not glass:
        return []
    
    flatRes = sorted(list(chain.from_iterable(glass)), key = lambda x: Density[x])
    step = int(len(flatRes) / len(glass))
    return [flatRes[x:x + step] for x in range(0, len(flatRes), step)]
    
#Test.describe("Sorting array by liquid density.")
#Test.it("Should be able to sort 3 liquids")
Test.assert_equal(separate_liquids([['H', 'H', 'W', 'O'],['W','W','O','W'],['H','H','O','O']]), [['O', 'O', 'O', 'O'],['W','W','W','W'],['H','H','H','H']], "")
#Test.it("Should be able to handle 4 liquids")
Test.assert_equal(separate_liquids([['A','A','O','H'],['A', 'H', 'W', 'O'],['W','W','A','W'],['H','H','O','O']]),                                       [['O','O','O','O'],['A', 'A', 'A', 'A'],['W','W','W','W'],['H','H','H','H']], "")
#Test.it("Should be able to handle one row")
Test.assert_equal(separate_liquids([['A','H','W','O']]),[['O','A','W','H']],"")
#Test.it("Should be able to handle one column")
Test.assert_equal(separate_liquids([['A'],['H'],['W'],['O']]),[['O'],['A'],['W'],['H']],"")
#Test.it("Should be able to handle empty array")
Test.assert_equal(separate_liquids([]), [], "Empty array should be returned if given.")