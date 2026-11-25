def scanner(qrcode):
    bits = []

    # рядки 20 -> 9
    for r in range(20, 8, -1):
        for c in (20, 19):
            bit = qrcode[r][c]
            if (r + c) % 2 == 0:
                bit = 1 - bit
            bits.append(bit)

    # рядки 9 -> 20
    for r in range(9, 21):
        for c in (18, 17):
            bit = qrcode[r][c]
            if (r + c) % 2 == 0:
                bit = 1 - bit
            bits.append(bit)

    # рядки 20 -> 9
    for r in range(20, 8, -1):
        for c in (16, 15):
            bit = qrcode[r][c]
            if (r + c) % 2 == 0:
                bit = 1 - bit
            bits.append(bit)

    # Останні 4 біти зверху вниз рядки 9 -> 10
    for r in range(9, 11):
        for c in (14, 13):
            bit = qrcode[r][c]
            if (r + c) % 2 == 0:
                bit = 1 - bit
            bits.append(bit)

    # Перетворюємо у суцільний рядок з '0' та '1'
    bit_str = "".join(str(b) for b in bits)

    # Перші 4 біти пропускаємо
    length = int(bit_str[4:12], 2)

    message = ""
    for i in range(length):
        start = 12 + i * 8
        byte = bit_str[start : start + 8]
        message += chr(int(byte, 2))

    return message
    
    
