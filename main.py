import base64
import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "image.b64"), "rb") as f:
        raw = base64.b64decode(f.read())
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.png"), "wb") as f:
        f.write(raw)


if __name__ == "__main__":
    main()
