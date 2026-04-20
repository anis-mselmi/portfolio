import base64
import io
from pathlib import Path

import streamlit as st

try:
    from PIL import Image, ImageDraw
except ImportError:
    Image = None
    ImageDraw = None


def load_profile_image(image_path: Path):
    if not image_path.exists():
        return None
    if Image is None or ImageDraw is None:
        return str(image_path)

    image = Image.open(image_path).convert("RGBA")
    size = min(image.size)
    left = (image.width - size) // 2
    top = (image.height - size) // 2
    image = image.crop((left, top, left + size, top + size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    image.putalpha(mask)
    return image


@st.cache_data(show_spinner=False)
def image_to_data_uri(image_path: Path, max_width: int = 900) -> str | None:
    if not image_path.exists():
        return None
    suffix = image_path.suffix.lower().lstrip(".")
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
        "svg": "image/svg+xml",
    }
    mime_type = mime_map.get(suffix, "image/png")

    if suffix == "svg":
        encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"

    if Image is not None:
        try:
            image = Image.open(image_path)
            if image.width > max_width:
                ratio = max_width / image.width
                new_size = (max_width, max(1, int(image.height * ratio)))
                image = image.resize(new_size)

            buffer = io.BytesIO()
            has_alpha = image.mode in {"RGBA", "LA"} or (
                image.mode == "P" and "transparency" in image.info
            )

            if has_alpha:
                image.save(buffer, format="PNG", optimize=True)
                encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
                return "data:image/png;base64," + encoded

            image = image.convert("RGB")
            image.save(buffer, format="JPEG", quality=80, optimize=True)
            encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded}"
        except Exception:
            pass

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def section_title(title: str, icon: str = "") -> None:
    with st.container():
        st.markdown(
            f"""
            <div class="section-title">{icon} {title}</div>
            <div class="section-divider"></div>
            """,
            unsafe_allow_html=True,
        )


def badge(text: str) -> None:
    st.markdown(f"<span class=\"pill\">{text}</span>", unsafe_allow_html=True)


def section_start(anchor: str, hero: bool = False) -> None:
    st.markdown(
        f"<span id='{anchor}' class='anchor-target anchor-section' data-anchor='{anchor}'></span>",
        unsafe_allow_html=True,
    )


def section_end() -> None:
    return
