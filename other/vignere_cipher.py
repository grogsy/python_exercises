'''Codewars challenge'''

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')

    def encode(self, text):
        text = text.decode('utf-8')

        key = ''
        while len(key) <= len(text):
            key += self.key
        key = key[:len(text)]
        out = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                out += text[i]
            else:
                mi = self.alphabet.index(text[i])
                ki = self.alphabet.index(key[i])
                out += self.alphabet[(mi + ki) % len(self.alphabet)]

        return out.encode('utf-8')

    def decode(self, text):
        text = text.decode('utf-8')
        key = ''
        while len(key) <= len(text):
            key += self.key
        key = key[:len(text)]
        out = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                out += text[i]
            else:
                mi = self.alphabet.index(text[i])
                ki = self.alphabet.index(key[i])
                out += self.alphabet[(mi - ki) % len(self.alphabet)]

        return out.encode('utf-8')
