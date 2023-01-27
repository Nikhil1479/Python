alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  cipher_text = ''
  for i in text:
    if i not in alphabet:
      cipher_text += i
    else:
      shift_alphabet = (alphabet.index(i))
      cipher_text += alphabet[(shift_alphabet+shift)%25]
  print(f"Cipher Text: {cipher_text}")
    #TODO: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    


#TODO: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(ciphertext, shift):
  plaintext = ""
  for text in ciphertext:
    if text not in alphabet:
      plaintext += text
    else:
      position = alphabet.index(text)
      new_position = (position - shift)%25

      plaintext += alphabet[new_position]
  print(f"Decrypted Plain text: {plaintext}")


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().   
def caesar(text, shift, direction):
 
    end_text = ""
  
    for letter in text:
      if letter not in alphabet:
        end_text += letter
        
      else:
        position = alphabet.index(letter)
        if direction == "encode":
          new_position = (position + shift)%25
          end_text += alphabet[new_position]
        elif direction == "decode":
          new_position = (position - shift) %25
          end_text+= alphabet[new_position]
        else:
          print("Invalid Direction")
          return
    print(f"{direction} text is {end_text}")
   
    
    



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
quit = False
while not quit:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text=text, shift = shift, direction=direction)

  go_ahead = input("Do you want to go ahead [yes] or [no]")
  if go_ahead == 'no':
    print("Goodbye👋")
    quit = True