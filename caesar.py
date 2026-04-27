import sys

def caesar_cipher(message, shift):
  encoded = []
  for char in message:
    if char.isalpha():
      upper = char.upper()
      shifted = chr((ord(upper) - ord('A') + shift) % 26 + ord('A'))
      encoded.append(shifted)
  return encoded