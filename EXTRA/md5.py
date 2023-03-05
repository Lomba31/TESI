import hashlib

def find_lowest_number(secret_key):
  num = 1
  while True:
    # Compute the hash of the secret key and the current number
    hash_input = secret_key + str(num)
    hash_output = hashlib.md5(hash_input.encode()).hexdigest()

    # Check if the hash starts with five zeroes
    if hash_output[:6] == '000000':
      return num

    # Increment the number and try again
    num += 1

# Example usage
secret_key = 'bgvyzdsv'
lowest_number = find_lowest_number(secret_key)
print(f'The lowest number for secret key "{secret_key}" is {lowest_number}')