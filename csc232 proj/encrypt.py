import random
import string
import sys

symbols = list(string.printable)[:94]


def encrypt(text):
  """Add three chars after every char in the plaintext(fuzz)
  After, substitue these chars with their hex equivalent(hexify)
  
  input: string sentence
  returns: string
  
  >>> encrypt('secret message')
  '733450606535326d63455b0723f4a7365383b5974396b78
  6d6378666564434573b3860733c2c296137416367317e72654f3e62'
  """

  cipher = fuzz(text)
  return hexify(cipher)

  
def fuzz(text):
  """Obfuscate a message by adding three letters after evey char in string.
  Input gets fed to the fuzz_word function which performs the actual
  fuzzing of words.
  input: string
  returns: string
  
  >>> fuzz('hello')
  'h0"Ze:~sl3~^l2a[o;D>'
  >>> fuzz('secret message')
  'sD6jeSH$c|\\erf7Fe^<%t4}k m_s(e*Sesgvtse2+a\\>@g$;YehW^'
  """

  return ' '.join([fuzz_word(word) for word in text.split()])

def fuzz_word(word):
  """Function which takes input from the fuzz function. This is where
  the actual obfuscating logic takes place. We take random ascii chars
  and symbols from the built-in string module's printable attribute. 
  Then we concatenate them to every letter in the word.
  
  input: single word string
  returns: string
  """
  res = []

  for c in word:
    for i in range(3):
      c += random.choice(symbols)
    res.append(c)

  return ''.join(res)

def hexify(text):
  """Sub all the chars in the string into its hex equivalent.
  This function feeds individual words to the hexify_word
  function which performs the actual logic.
  
  input: string
  returns: string
  
  >>> hexify('I am a secret message!!')
  '49 616d 61 736563726574 6d6d573736167652121'
  """
  return ' '.join([hexify_word(word) for word in text.split()])
  

def hexify_word(word):
  """Helper to the hexify function, translates words to their
  hex equivalent individually. Every word will be appended to
  a list of words to be joined into a sentence.
  
  input: string of hex characters
  returns: string
  """

  return ''.join([str(hex(ord(c))[2::]) for c in word])

  
if __name__=='__main__':
  #>>>sys.argv
  #   ['encrypt.py', <file_to_encrypt>]
  #so we'll set our readfile var to open as the actual file supplied in command line
  readfile = sys.argv[1]
  
  #trims the extension from the name of the file
  writefile = readfile.split('.')[0] + "_encrypt.txt"
  
  with open(readfile) as plaintext, open(writefile, 'w+') as ciphertext:
    
	#does not return single string, returns a list of lines from the file
    contents = plaintext.readlines()
    
    encrypted_contents = []
    
    for line in contents:
	  
      encrypted_contents.append(encrypt(line))
    
    ciphertext.write('\n'.join(encrypted_contents))

  print("encrypted file: %s" % readfile)
  print("check directory.")