import random
import string

def code_generator(size=5, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#
def createshorturl(instance, size=5):
    new_code = code_generator(size=6)
    # print(instance)
    # print(instance.__class__)
    klass = instance.__class__
    qs_exist = klass.objects.filter(shorturl=new_code).exists()
    if qs_exist:
        return createshorturl(size = size)
    return new_code
