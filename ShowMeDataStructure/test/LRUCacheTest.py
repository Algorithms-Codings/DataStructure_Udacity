from src.LRU_Cache  import LRU_Cache
import unittest
class LRUCacheTest(unittest.TestCase):
    def test_3(self):
        print("******************TestCase 3***************")
        our_cache=LRU_Cache(3)
        our_cache.set(1,1)
        print("after adding 1,1 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2,2)
        print("after adding 2,2 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(3,3)
        print("after adding 3,3 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(4,4)
        print("after adding 4,4 ->")
        our_cache.print()
        print("\n**************")
        
        
        print("get 4 =",our_cache.get(4)) # Expected Value = 4
        print("after get 4 ->")
        our_cache.print()
        print("\n**************")
        
        print("get 1 =",our_cache.get(1)) # Expected Value = -1
        print("after get 1 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2,4)
        print("after set 2,4 =")
        our_cache.print()
        print("\n**************")
          
        print("get 2 ,",our_cache.get(2)) # Expected Value = 4
        print("after get 2 ->")
        our_cache.print()
        print("\n**************")
    def test_LRUCahce5(self):
        print("******************TestCase 1***************")
        our_cache = LRU_Cache(5)

        our_cache.set(1,1) #1
        print("after adding 1,1 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2,2) #1,2
        print("after adding 2,2 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(3,3) #1,2,3
        print("after adding 3,3 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(4,4);
        print("after adding 4,4 ->") #1,2,3,4
        our_cache.print()
        print("\n**************")
        
        print("get 1=",our_cache.get(1))       # returns 1
        print("after get 1 ->")       #2,3,4,1 
        our_cache.print()
        print("\n**************")
        
        print("get 2=",our_cache.get(2))       # returns 2
        print("after get 2 ->") #3,4,1,2
        our_cache.print()
        print("\n**************")
        
        print("get 9 =",our_cache.get(9))      # returns -1 because 9 is not present in the cache
        print("after get 9 ->") #3,4,1,2
        our_cache.print()
        print("\n**************")
        
        our_cache.set(5,5)
        print("after adding 5,5 ->") #3,4,1,2,5
        our_cache.print()
        print("\n**************")
        
        our_cache.set(6,6)        
        print("after adding 6,6 ->") #4,1,2,5,6
        our_cache.print()
        print("\n**************")
        
        print("get 3=",our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        print("after get 3 ->") #4,1,2,5,6
        our_cache.print()
        print("\n**************")


        print("get 2=",our_cache.get(2))       # returns 2
        print("after get 2 ->") #4,1,5,6,2
        our_cache.print()
        print("\n**************")



        print("get 6 =",our_cache.get(6))       # returns 6
        print("after get 6 ->") #4,1,5,2,6
        our_cache.print()
        print("\n**************")



        print("get 1 =",our_cache.get(1))       # returns 1
        print("after get 1 ->") #4,5,2,6,1
        our_cache.print()
        print("\n**************")
    def test_LRUCahce2(self):
        print("******************TestCase 2***************")
        our_cache = LRU_Cache(2)

        our_cache.set(1,1)
        print("after adding 1 ->") #1
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2,2)
        print("after adding 2 ->") #1,2
        our_cache.print()
        print("\n**************")
        
        our_cache.set(3,3)
        print("after adding 3 ->") #2,3
        our_cache.print()
        print("\n**************")

        print("get 2,",our_cache.get(2))       
        print("after get 2 ->") #3,2
        our_cache.print()
        print("\n**************")



        print("get 6 ,",our_cache.get(6))
        print("after get 6 ->") #3,2
        our_cache.print()
        print("\n**************")
        
        our_cache.set(6,6)
        print("after adding 6 ->") #2,6
        our_cache.print()
        print("\n**************")
        
        print("get 6 ,",our_cache.get(6))
        print("after get 6 ->") #2,6
        our_cache.print()
        print("\n**************")

if __name__ == '__main__':
    LRUCacheTest.main()