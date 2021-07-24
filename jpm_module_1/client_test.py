import unittest
from client3 import getDataPoint
from client3 import getRatio
class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
    {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},  
    {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}]
    """ ------------ Add the assertion below ------------ """
    expected = []
    for i in range(4):
      expected.append((quotes[i]["stock"], quotes[i]["top_bid"]["price"], quotes[i]["top_ask"]["price"],(quotes[i]["top_bid"]["price"]+quotes[i]["top_ask"]["price"])/2))
      self.assertEqual(getDataPoint(quotes[i]), expected[i])

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    quotes = [
    {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},  
    {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}]
    pricelist = []
    for i in range(4):
      pricelist.append(getDataPoint(quotes[i])[3])
      if i > 0: 
        self.assertEqual(getRatio(pricelist[i-1], pricelist[i]), pricelist[i-1]/pricelist[i])


if __name__ == '__main__':
    unittest.main()
