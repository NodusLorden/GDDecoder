import base64
import gzip


# bytes string -> bytes
def xor(by: bytes) -> bytes:
    return bytearray(map(lambda x: x ^ 11, by))


# bytes -> base64 bytes
def frombase64(by: bytes) -> bytes:
    return base64.b64decode(by.decode().replace("_", "/").replace("-", "+"))


# bytes base64 -> bytes
def tobase64(by: bytes) -> bytes:
    return base64.b64encode(by).decode().replace("/", "_").replace("+", "-").encode()


# bytes -> string
def fromgzip(by: bytes) -> str:
    return gzip.decompress(by).decode()


# string -> bytes
def togzip(st: str) -> bytes:
    return gzip.compress(st.encode())


# k4 string -> blocks
def blockdecoder(st: str) -> str:
    return fromgzip(frombase64(st.encode()))


# k34 string -> string
def k34decoder(st: str) -> str:
    return fromgzip(frombase64(st.encode()))


# k3 string -> text string
def descriptiondecoder(st: str) -> str:
    return frombase64(st.encode()).decode()
