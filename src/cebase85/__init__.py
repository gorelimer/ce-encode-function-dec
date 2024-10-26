class CEBase85:
    custom_base85 = (
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "!#$%()*+,-./:;=?@[]^_{}"
    )
    powers_of_85 = (52200625, 614125, 7225, 85, 1)

    @staticmethod
    def base85_to_bin(input_string_base85):
        result = bytearray()
        size = len(input_string_base85)
        for i in range(0, size, 5):
            chunk = input_string_base85[i:i + 5]
            a = 0
            for j, char in enumerate(chunk):
                index = CEBase85.custom_base85.find(char)
                if index == -1:
                    msg = f"Invalid character '{char}' in input."
                    raise ValueError(msg)
                a += index * CEBase85.powers_of_85[j]
            if len(chunk) == 5:  # noqa: PLR2004
                result.extend(a.to_bytes(4, "big"))
                continue
            remainder = size % 5
            if remainder in (2, 3, 4):
                padding = 84 + CEBase85.powers_of_85[remainder - 1]
                a += padding
                result.extend(a.to_bytes(4, "big")[: remainder - 1])
        return result
