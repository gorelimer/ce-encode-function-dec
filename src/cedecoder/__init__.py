import io
import zlib

from ..cebase85 import CEBase85


class CEFunctionDecoder:
    @staticmethod
    def decode(encoded: str) -> io.BytesIO:
        decoded_bytes = CEBase85.base85_to_bin(encoded)
        decompressed_fileio = io.BytesIO(zlib.decompress(decoded_bytes))
        return decompressed_fileio
