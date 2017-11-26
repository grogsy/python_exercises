import sys
def decrypt(cipher):
  """Feed individual words into the decrypt_letters function
  which performs the actual decrypting logic.
  
  input: single word
  returns: string
  """
  #We want to pair hexes together to be used in decrypt_letter.
  #The built-in zip() function helps to create pairs of every two items
  #from the input.
  
  return ' '.join([decrypt_word(word) for word in cipher.split()])
  
  #to decrypt a text the command is decrypt("the cipher text from the cipher file")
  #and the file appear on desktop. If not then search for it in file explorer.


def decrypt_word(word):
  #We want to pair hexes together to be used in decrypt_letter.
  #The built-in zip() function helps to create pairs of every two items
  #from the input.
                 #i and j here are strings, not numerical
  hex_chunks = [i+j for i,j in zip(word[0::2], word[1::2])]

  return decrypt_letters(hex_chunks)

  #one-line version that doesn't require decrypt_letters function:
  #''.join([chr(int(i+j, 16)) for i,j in list(zip(a[0::2], a[1::2]))[::4]]) why? because why not

def decrypt_letters(hex_chunks):
  """This function expects a list of hexadecimal pairs.
  Translates every pair to its ascii equivalent.
  Note: This function knows about skipping every 6 hex chars.
  
  input: a list of hexedecimal letters
  returns: string
  """
                                          #skip over every 3 pairs
  return ''.join([chr(int(pair, 16)) for pair in hex_chunks[::4]])

  
if __name__=='__main__':
  
  readfile = sys.argv[1]
  
  #trims the extension from the name of the file
  writefile = readfile.split('encrypt')[0] + "decrypted.txt"
  
  with open(readfile) as ciphertext, open(writefile, 'w+') as plaintext:
    
    encrypted_contents = ciphertext.readlines()
    
    decrypted_contents = []
    
    for line in encrypted_contents:
    
      decrypted_contents.append(decrypt(line))
    
    plaintext.write('\n'.join(decrypted_contents))

  print("decrypted: %s" % readfile)
  print("check directory.")
