from src.FileRecursion import FileRecursion
import unittest
class FileRecursionTest(unittest.TestCase):
    def test_NormalScenario(self):
        
        print("**************************test_NormalScenario ************************************")
        fr=FileRecursion()
        files=fr.find_files("c","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir")
        for f in files:
            print(f)
        self.assertEqual(len(files),4)
    def test_emptyPath(self):
        
        print("**************************test_emptyPath ************************************")
        fr=FileRecursion()
        files=fr.find_files("c",None)
        self.assertTrue(files is None)
    
    def test_emptySuffix(self):        
        print("**************************test_emptySuffix ************************************")
        fr=FileRecursion()
        files=fr.find_files("","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir")
        self.assertTrue(files is None)
        
    def test_invalidSuffix(self):        
        print("**************************test_invalidSuffix ************************************")
        fr=FileRecursion()
        files=fr.find_files("xyh","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir")
        self.assertTrue(files is None)    
    
    def test_invalidPath(self):        
        print("**************************test_invalidPath ************************************")
        fr=FileRecursion()
        files=fr.find_files("c","E:/Udacity_DataStr\DataStructure_Udacity\ShowMeDataStructure\testdir")
        self.assertEqual(files , None)
    def test_unknowPath(self):        
        print("**************************test_unknowPath ************************************")
        fr=FileRecursion()
        files=fr.find_files("c","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir123")
        self.assertEqual(files ,None)       
    def test_fileasPath(self):
        print("**************************assertEqual ************************************")
        fr=FileRecursion()
        files=fr.find_files("c","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir/subdir5/a.c")
        self.assertEqual(len(files) ,1)  
        
 
if __name__ == '__main__':
    FileRecursionTest.main()
