import unittest
from src.UnionAndIntersection import UnionAndInterSection
from src.UnionAndIntersection import LinkedList
class UnionAndIntersectionTest(unittest.TestCase):

    def test_NormalCase(self):        
        print("****test_NormalCasee *********")
        ui= UnionAndInterSection([3,2,4,35,6,65,6,4,3,21],[6,32,4,9,4,6,1,11,21,1])
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)

    def test_NormalCase2(self):        
        print("****test_NormalCase2 *********")
        ui= UnionAndInterSection([3,2,4,35,6,65,6,4,3,23],[1,7,8,9,11,21,1])
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)    
    def test_SecondListEmpty(self):        
        print("****test_SecondListEmpty *********")
        ui= UnionAndInterSection([3,2,4,35,6,65,6,4,3,23],[])
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)  
    def test_FirstListEmpty(self):        
        print("****test_FirstListEmpty *********")
        ui= UnionAndInterSection(None,[3,2,4,35,6,65,6,4,3,23])
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)    
    def test_BothListEmpty(self):        
        print("****test_BothListEmpty *********")
        ui= UnionAndInterSection(None,"")
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)       
        
    def test_IdenticalList(self):        
        print("****test_IdenticalList*********")
        ui= UnionAndInterSection([3,2,4,35,6,65,6,4,3,23],[3,2,4,35,6,65,6,4,3,23])
        result_list=ui.union()
        
        print("Union=",result_list)
        result_list=ui.intersection()
        print("intersection=",result_list)    


if __name__ == '__main__':
    UnionAndIntersectionTest.main()
    