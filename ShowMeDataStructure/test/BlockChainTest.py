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
        self.assertEqual(bl.head.hash,"cf84e7a77f1fcdbe853ddcc815d1d8941b719ca5008774aaf15543773180941c")
        self.assertEqual(bl.head.next.hash,"c3c5be2b0d777480ea10162d07957a4d6ea529e363de58bc91d8a25b7caaa150")
        self.assertEqual(bl.head.next.next.hash,"1e4d332fbbea1a13afb54d563422c5c441e5f84834255d3c4acdc4cedf690358")

    def test_1block(self):
        print("*********** test -  block chains with 1 blocks")
        bl=BlockChain()
        bl.append( "One Data")
        print(bl.toList())
        self.assertEqual(bl.getSize(),1)
        self.assertEqual(bl.head.hash,"a65d859c791fe29aef75cb98ba38a00aa3d554db4ba7a961c0008405becc090e")
    def test_noblock(self):
        print("*********** test -  block chains with no blocks")
        bl=BlockChain()
        print(bl.toList())   
        self.assertEqual(bl.getSize(),0)
if __name__ == '__main__':
    BlockChainTest.main()