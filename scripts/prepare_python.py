import io
import requests
import tarfile
import zstandard

LAST_RELEASE = "https://github.com/indygreg/python-build-standalone/releases/download/20220318/"
IMPLEMENTATION = "cpython"
VERSION = "3.10.3+20220318"
ARCH = "x86_64"
PLATFORM = "unknown"
SYSTEM = "linux-gnu"
KIND = "install_only"

ASSET_NAME = "-".join([
    IMPLEMENTATION,
    VERSION,
    ARCH,
    PLATFORM,
    SYSTEM,
    KIND
])
ASSET_LINK = LAST_RELEASE + ASSET_NAME + ".tar.gz"

response = requests.get(ASSET_LINK)
buffer = io.BytesIO(response.content)

def unpack_zstandard(buffer):
    dctx = zstandard.ZstdDecompressor()
    with dctx.stream_reader(buffer) as reader:
        with tarfile.open(mode="r|", fileobj=reader) as tf:
            tf.extractall()

def unpack_gzip(buffer):
    with tarfile.open(mode="r|gz", fileobj=buffer) as tf:
        tf.extractall()

unpack_gzip(buffer)
