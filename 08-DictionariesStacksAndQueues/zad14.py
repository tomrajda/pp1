# 14.	Write a program that spells any text entered from the keyboard, 
# using ICAO spelling alphabet 
# (https://en.wikipedia.org/wiki/NATO_phonetic_alphabet).
# Create a dictionary where you put all the letters and the corresponding words. 
# Then try to spell your name and three other words. Sample result:
#   Enter text: uek
#   Spelled text: Uniform Echo Kilo

alphabet = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu"
}

text = "Tomasz"

spelled_text = ""
for l in text:
    spelled_text += alphabet[l.upper()] + " "

print(f"Enter text: {text}\nSpelled text: {spelled_text}")