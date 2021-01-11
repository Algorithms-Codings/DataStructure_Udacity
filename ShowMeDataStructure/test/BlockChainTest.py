from src.Blockchain  import BlockChain
import unittest

class BlockChainTest(unittest.TestCase):
    def test_3Blocks(self):
        print("*********** test -  block chains with 3 blocks")
        bl=BlockChain()
        bl.append( "First Data")
        bl.append("Second Data")
        bl.append( "Third Data")
        
        print(bl.toList())
        self.assertEqual(bl.getSize(),3)
        

    def test_1block(self):
        print("*********** test -  block chains with 1 blocks")
        bl=BlockChain()
        bl.append( "One Data")
        print(bl.toList())
        self.assertEqual(bl.getSize(),1)
        
    def test_noblock(self):
        print("*********** test -  block chains with no blocks")
        bl=BlockChain()
        print(bl.toList())   
        self.assertEqual(bl.getSize(),0)
if __name__ == '__main__':
    BlockChainTest.main()