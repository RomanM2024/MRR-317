
s = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
print(*filter(lambda s: s[::-1].lower() == s.lower(), s))
