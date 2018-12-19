def decor(func):
    def wrap():
        print("="*12)
        func()
        print("="*12)
    return wrap()

def decor2(f):
    def xxx():
        print('decor antes')
        f()
        print('decor2')
    return xxx

@decor2
@decor
def print_text():
    print('Hola mundo')

print_text()
