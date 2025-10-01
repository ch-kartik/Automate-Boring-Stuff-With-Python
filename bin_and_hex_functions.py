Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
>>> format(14, '#b')
'0b1110'
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}'
'0b1110'
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')
>>> help(bin)
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.

    >>> bin(2796202)
    '0b1010101010101010101010'

>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
