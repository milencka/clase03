def decor(asterisco):
    def _decor(func):
        def wrap():
            if asterisco:
                print("*" * 12)
            else:
                print("=" * 12)
        func()
        if asterisco:
            print("*" * 12)
        else:
            print("=" * 12)
            return wrap
    return _decor

@decor(asterisco=True)
def print_text():
    print("Hola Mundo!!!")

print_text()