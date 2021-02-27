import string
import random

class string:

  def generate_uppercase_int(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

  def generate_lowercase_int(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

  def generate_lowercase(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  
  def generate_int(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  
  def generate_str_uppercase(size, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

  def generate_str_lowercase(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
