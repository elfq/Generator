import string
import random

class string:

  def uppercase(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

  def lowercase(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  
  def int(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  
  def str_uppercase(size, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

  def str_lowercase(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
