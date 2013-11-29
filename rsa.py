
def gcd (a, b): #En Buyuk Ortak Bolen
  "Compute GCD of two numbers"

  if b == 0: return a
  else: return gcd(b, a % b)

def multiplicative_inverse(a, b):
  # b ile hangi sayiyi (d) carparsam a' ya gore mod' u 1 olur?

  origA = a
  X = 0
  prevX = 1
  Y = 1
  prevY = 0

  while b != 0:

      temp = b
      quotient = a/b
      b = a % b
      a = temp

      temp = X
      a = prevX - quotient * X
      prevX = temp

      temp = Y
      Y = prevY - quotient * Y
      prevY = temp

  return origA + prevY


def generateRSAKeys(p, q): # totient bulunuyor
  n = p * q
  m = (p - 1) * (q - 1) 


### e yi 3 ten baslat, m ile aralarinda asal bir sayi bulana kadar e yi artir...
  e = 3

  while 1:
    
      if gcd(m, e) == 1: break
      else: e = e + 2
###

### d * e = 1 (mod m) olacak sekilde bir d degeri uret...
  d = multiplicative_inverse(m, e) 
###

#####################################################################################
###### (d, e, n) UCLUSUNU A KULLANICISI VE B KULLANICISI ICIN AYRI AYRI OLUSTURALIM.#
#####################################################################################
#
#
#
#
#
#####################################################################################
  
### (n,e): ortak anahtar, (n,d): gizli anahtar 
  return ((n,e), (n,d))         
###

if __name__ == "__main__":

  print "RSA Encryption algorithm..."
  p = long(raw_input("Enter the value of p (prime number):"))
  q = long(raw_input("Enter the value of q (prime number):"))

  print "Generating public and private keys...."
  (publickey, privatekey) = generateRSAKeys(p, q)

  print "Public Key (n, e) =", publickey
  print "Private Key (n, d) =", privatekey

  n, e = publickey
  n, d = privatekey

  input_num = long(raw_input("Enter a number to be encrypted:"))
  encrypted_num = (input_num ** e) % n
  print "Encrypted number using public key =", encrypted_num
  decrypted_num = encrypted_num ** d % n
  print "Decrypted (Original) number using private key =", decrypted_num
