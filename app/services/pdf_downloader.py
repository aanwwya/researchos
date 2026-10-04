from pathlib import Path

import httpx


def download_pdf(url: str, output_path: str) -> bool:
    response = httpx.get(
        url,
        follow_redirects=True,
        timeout=30,
    )

    response.raise_for_status()

    content = response.content

    if not content.startswith(b"%PDF-"):
        return False

    Path(output_path).write_bytes(content)

    return True