import unittest
from src.HuffmanCoding import HuffmanCoding
class HuffmanEncodingTest(unittest.TestCase):

    def test_NormalCase(self):        
        print("****Test: Encode- normal Case *********")
        sentence = "The bird is the word"       
        print("Original String:",sentence) 
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)

    def test_RepeatWordCase(self):        
        print("****Test: Encode- Repeat Word *********")
        sentence = "Hello Hello Hello"       
        print("Original String:",sentence) 
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)


    def test_OneWord(self):
        print("****Test: Encode- One Word *********")
        sentence = "Rajeswari"       
        print("Original String:",sentence) 
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
       
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)
    
    def test_EmptyString(self):
        print("****Test: Encode- Empty String*********")

        sentence = ""  
        print("Original String:",sentence)     
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)
    def test_repeatChars(self):
        print("****Test: Encode- test_repeatCharsg*********")

        sentence = "ababaabccdddeeefffgggaacc"  
        print("Original String:",sentence)     
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string) 
    def test_oneChar(self):
        print("****Test: Encode- One char*********")

        sentence = "a"  
        print("Original String:",sentence)     
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)
    def test_repeatSameChar(self):
        print("****Test: Encode- test_repeatSameChar*********")

        sentence = "fff"  
        print("Original String:",sentence)     
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)    
    def test_twoChar(self):
        print("****Test: Encode- two char*********")

        sentence = "ab"  
        print("Original String:",sentence)     
        hc = HuffmanCoding(sentence)
        hc.huffman_encoding()
        encodedString=hc.encodedString
        print("Encoded String",encodedString)
        hc.huffman_decoding()
        decoded_string=hc.decodedString
        print("Decoded String:",decoded_string)
        self.assertEqual(sentence,decoded_string)    

if __name__ == '__main__':
    HuffmanEncodingTest.main()
    
