from src.LRU_Cache  import LRU_Cache
import unittest
class LRUCacheTest(unittest.TestCase):
    def test_LRUCahce5(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1)
        print("after adding 1 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2)
        print("after adding 2 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(3)
        print("after adding 3 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(4);
        print("after adding 4 ->")
        our_cache.print()
        print("\n**************")
        
        print("get 1,",our_cache.get(1))       # returns 1
        print("after get 1 ->")        
        our_cache.print()
        print("\n**************")
        
        print("get 2,",our_cache.get(2))       # returns 2
        print("after get 2 ->")
        our_cache.print()
        print("\n**************")
        
        print("get 9",our_cache.get(9))      # returns -1 because 9 is not present in the cache
        print("after get 9 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(5)
        print("after adding 5 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(6)        
        print("after adding 6 ->")
        our_cache.print()
        print("\n**************")
        
        print("get 3,",our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        print("after get 3 ->")
        our_cache.print()
        print("\n**************")


        print("get 2,",our_cache.get(2))       # returns 2
        print("after get 2 ->")
        our_cache.print()
        print("\n**************")



        print("get 6 ,",our_cache.get(6))       # returns 6
        print("after get 6 ->")
        our_cache.print()
        print("\n**************")



        print("get 1 ,",our_cache.get(1))       # returns 1
        print("after get 1 ->")
        our_cache.print()
        print("\n**************")
    def test_LRUCahce2(self):
        our_cache = LRU_Cache(2)

        our_cache.set(1)
        print("after adding 1 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(2)
        print("after adding 2 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(3)
        print("after adding 3 ->")
        our_cache.print()
        print("\n**************")

        print("get 2,",our_cache.get(2))       
        print("after get 2 ->")
        our_cache.print()
        print("\n**************")



        print("get 6 ,",our_cache.get(6))
        print("after get 6 ->")
        our_cache.print()
        print("\n**************")
        
        our_cache.set(6)
        print("after adding 6 ->")
        our_cache.print()
        print("\n**************")
        
        print("get 6 ,",our_cache.get(6))
        print("after get 6 ->")
        our_cache.print()
        print("\n**************")
if __name__ == '__main__':
    LRUCacheTest.main()