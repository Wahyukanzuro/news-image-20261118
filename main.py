import base64, os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "image.b64"), "rb") as f:
        data = base64.b64decode(f.read())
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
