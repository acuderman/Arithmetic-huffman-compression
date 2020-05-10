from generate_string import StringGenerator
from huffman import HuffmanCoding

filePath = './files/text.txt'
stringGenerator = StringGenerator(100)
stringGenerator.generateRandomSequence()
stringGenerator.saveString(filePath)

huffmanCoding = HuffmanCoding(filePath)

compressed_output_path = huffmanCoding.compress()
print(compressed_output_path)

uncompressed_output_path = huffmanCoding.decompress(compressed_output_path)
print(uncompressed_output_path)

