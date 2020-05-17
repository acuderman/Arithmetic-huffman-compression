from generate_string import StringGenerator
from huffman import HuffmanCoding
from python.adaptive_arithmetic_compress import adaptiveArithmeticCompress
from python.arithmetic_compress import arithmeticCompress
from pathlib import Path

def generateStrings(stringLength):
    filePath = './files/text-{}.txt'.format(str(stringLength))
    stringGenerator = StringGenerator(stringLength)
    stringGenerator.generateRandomSequence()
    stringGenerator.saveString(filePath)

    return filePath


string100 = generateStrings(100)
string1000 = generateStrings(1000)
string10000 = generateStrings(10000)
string100000 = generateStrings(100000)
string1000000 = generateStrings(1000000)
string10000000 = generateStrings(10000000)

print('Huffman - Start')

huffmanCoding = HuffmanCoding(string100)
compressed_output_path = huffmanCoding.compress()

huffmanCoding = HuffmanCoding(string1000)
compressed_output_path = huffmanCoding.compress()

huffmanCoding = HuffmanCoding(string10000)
compressed_output_path = huffmanCoding.compress()

huffmanCoding = HuffmanCoding(string100000)
compressed_output_path = huffmanCoding.compress()

huffmanCoding = HuffmanCoding(string1000000)
compressed_output_path = huffmanCoding.compress()

huffmanCoding = HuffmanCoding(string10000000)
compressed_output_path = huffmanCoding.compress()

print('Huffman - Done')

print('Arithmetic - Start')

adaptiveArithmeticCompress(string100)
adaptiveArithmeticCompress(string1000)
adaptiveArithmeticCompress(string10000)
adaptiveArithmeticCompress(string100000)
adaptiveArithmeticCompress(string1000000)
adaptiveArithmeticCompress(string10000000)

print('Arithmetic - Done')

print('Compare - Start')

def compareFileSizes(stringLength):
    filePath = './files/text-{}.txt'.format(str(stringLength))
    huffmanCompressedFile = './files/text-{}_huffman_compressed.bin'.format(str(stringLength))
    arithmeticCompressedFile = './files/text-{}.txt_arithmetic_compressed.bin'.format(str(stringLength))

    print('Original / huffman %')
    print((Path(huffmanCompressedFile).stat().st_size / Path(filePath).stat().st_size) * 100)

    print('Original / arithmetic %')
    print((Path(arithmeticCompressedFile).stat().st_size / Path(filePath).stat().st_size) * 100)

    print('Huffman / Arithmetic %')
    print((Path(huffmanCompressedFile).stat().st_size / Path(arithmeticCompressedFile).stat().st_size) * 100)
    print('------------------------------------------------------------------------------------')

string100 = compareFileSizes(100)
string1000 = compareFileSizes(1000)
string10000 = compareFileSizes(10000)
string100000 = compareFileSizes(100000)
string1000000 = compareFileSizes(1000000)
string10000000 = compareFileSizes(10000000)