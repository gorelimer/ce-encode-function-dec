import subprocess
from pathlib import Path

from ..cedecoder import CEFunctionDecoder

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


class LuaDecompiler:
    @staticmethod
    def decompile_func(bytecode_fp: Path) -> None:
        result = subprocess.run(
            ["luadec.exe", bytecode_fp],
            capture_output=True,
            text=True
        )
        output = OUTPUT_DIR / "decomplied"
        with output.open("w") as f:
            f.write(result.stdout)

    @staticmethod
    def decompile_encoded_func(encoded: str) -> None:
        bytecode = CEFunctionDecoder.decode(encoded)
        output = OUTPUT_DIR / "decoded.luac"
        with output.open("wb"):
            output.write_bytes(bytecode.read())
        LuaDecompiler.decompile_func(output)
