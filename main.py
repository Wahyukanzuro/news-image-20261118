# Rebuilds the entry picture from its bundled base64 payload.
from base64 import b64decode
from os import environ, makedirs, path


def _read_payload(payload_path):
    with open(payload_path, "rb") as source:
        return b64decode(source.read())


def decode_entry():
    base_dir = path.dirname(path.realpath(__file__))
    payload_path = path.join(base_dir, "image.b64")
    picture = _read_payload(payload_path)

    target_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(target_dir, exist_ok=True)
    target_path = path.join(target_dir, "entry.png")
    with open(target_path, "wb") as destination:
        destination.write(picture)


decode_entry()
