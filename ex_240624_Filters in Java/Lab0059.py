# Filter in Python

vowels = ['a', 'e', 'i', 'o', 'u']

ip_str = ['m', 'a', 'n', 'g', 'e', 's', 'h', 'i', 'o', 'u']
new_vowel = set(vowels)
new_ip_str = set(ip_str)
consonants = new_vowel.difference(new_ip_str)
print(set(consonants))

def is_vowel(letter):
    return letter in vowels


def is_consonant(letter):
    return letter in consonants


new_vowels = filter(is_vowel, ip_str)
print(list(new_vowels))

new_consonants = filter(is_consonant, ip_str)
print(list(new_consonants))