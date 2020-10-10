# Read txt file with open
m_file = open(r'data\test.txt')
m_file.read()
m_file.seek(0)
m_file.readlines()
m_file.close()

# Use open statement
with open(r'data\test.txt', mode='r+') as my_file:
    text = my_file.write('Hey, it\'s me \n')
    print(text)
    print(my_file.readlines())

# mode: w for write
# mode: r+ for read and write
# mode: a for append


# File IO errors
try:
    with open(r'data\test2.txt', mode='x') as my_file:
        # text = my_file.write('Hey, it\'s me \n')
        # print(text)
        print(my_file.readlines())
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err

# Translate file
from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open(r'data\trans_original.txt', mode='r') as trans_orig:
        text = trans_orig.read()
        translation = translator.translate(text)
        print(translation)
        with open(r'data\trans_tras.txt', mode = 'w') as trans_trans:
            trans_trans.write(translation)
except FileNotFoundError as err:
    print('file not found')
    raise err