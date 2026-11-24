"""Build a deterministic, public-assets-only ZIP for direct upload."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ASSETS = ("index.html", "style.css")


def package(output):
    root = Path(__file__).resolve().parent
    if any((root / name).is_symlink() for name in ASSETS):
        raise OSError("Storefront assets must be regular files in this repository.")
    assets = {name: (root / name).read_bytes() for name in ASSETS}
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        for name, content in assets.items():
            archive.writestr(ZipInfo(name), content, compress_type=ZIP_DEFLATED)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.suffix != ".zip":
        parser.error("Choose a new .zip output path.")
    try:
        package(args.output)
    except OSError as error:
        parser.exit(1, f"Could not package the storefront: {error}\n")
    print(args.output)


if __name__ == "__main__":
    main()
