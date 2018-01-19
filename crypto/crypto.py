class Crypto(object):
    decrypt_key_mapping = {
        '!': 'a',
        ')': 'b',
        '\"': 'c',
        '(': 'd',
        '£': 'e',
        '*': 'f',
        '%': 'g',
        '&': 'h',
        '>': 'i',
        '<': 'j',
        '@': 'k',
        'a': 'l',
        'b': 'm',
        'c': 'n',
        'd': 'o',
        'e': 'p',
        'f': 'q',
        'g': 'r',
        'h': 's',
        'i': 't',
        'j': 'u',
        'k': 'v',
        'l': 'w',
        'm': 'x',
        'n': 'y',
        'o': 'z'
    }

    def decrypt(self, message):
        decrypted_message = ''
        for letter in message:
            decrypted_message += self.decrypt_key_mapping[letter]
        return decrypted_message