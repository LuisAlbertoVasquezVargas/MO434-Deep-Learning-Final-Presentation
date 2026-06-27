# scripts/lwc.py

from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path


DEFAULT_OUTPUT_PATH = Path("output/lwc.txt")

INCLUDED_SUFFIXES = {
    ".tex",
    ".bib",
    ".cls",
    ".sty",
    ".md",
    ".py",
    ".yml",
    ".yaml",
    ".json",
    ".txt",
    ".sh",
}

EXCLUDED_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "output",
    "build",
    "dist",
}

EXCLUDED_SUFFIXES = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".zip",
    ".tar",
    ".gz",
    ".xz",
    ".7z",
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".nav",
    ".out",
    ".run.xml",
    ".snm",
    ".synctex.gz",
    ".toc",
    ".vrb",
}


def is_hidden_path(path: Path) -> bool:
    return any(part.startswith(".") and part != ".gitignore" for part in path.parts)


def should_skip_path(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return True

    if is_hidden_path(path):
        return True

    if path.name.endswith(".synctex.gz"):
        return True

    return path.suffix.lower() in EXCLUDED_SUFFIXES


def should_include_file(path: Path) -> bool:
    if not path.is_file():
        return False

    if should_skip_path(path):
        return False

    return path.suffix.lower() in INCLUDED_SUFFIXES


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def collect_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if should_include_file(path))


def build_lwc(root: Path, files: list[Path]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "LAST WORKING CODE",
        f"Generated at: {now}",
        f"Root: {root}",
        f"Files exported: {len(files)}",
        "",
    ]

    for path in files:
        relative_path = path.relative_to(root)
        content = read_text(path).rstrip()

        lines.extend(
            [
                "=" * 80,
                f"FILE: {relative_path}",
                "=" * 80,
                content,
                "",
            ]
        )

    return "\n".join(lines)


def parse_args() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    root = args.root.resolve()
    output_path = args.output

    files = collect_files(root)
    lwc = build_lwc(root, files)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(lwc, encoding="utf-8")

    print(f"Wrote {len(files)} files to {output_path}")


if __name__ == "__main__":
    main()
