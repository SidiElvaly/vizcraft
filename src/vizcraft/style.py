from __future__ import annotations

from dataclasses import dataclass
import matplotlib as mpl

@dataclass(frozen=True)
class Theme:
    # Palette (cohérente partout)
    primary: str = "#2563EB"
    secondary: str = "#16A34A"
    accent: str = "#F59E0B"
    danger: str = "#DC2626"
    muted: str = "#64748B"
    grid: str = "#E2E8F0"
    bg: str = "#FFFFFF"

    font_family: str = "DejaVu Sans"
    title_size: int = 14
    label_size: int = 11
    tick_size: int = 10
    line_width: float = 2.2
    marker_size: int = 6

DEFAULT_THEME = Theme()

def apply_style(theme: Theme = DEFAULT_THEME) -> None:
    """Applique un style global Matplotlib (rcParams)."""
    mpl.rcParams.update({
        "figure.facecolor": theme.bg,
        "axes.facecolor": theme.bg,
        "axes.edgecolor": theme.grid,
        "axes.labelcolor": "#0F172A",
        "axes.titleweight": "bold",
        "axes.titlesize": theme.title_size,
        "axes.labelsize": theme.label_size,
        "xtick.labelsize": theme.tick_size,
        "ytick.labelsize": theme.tick_size,
        "xtick.color": "#0F172A",
        "ytick.color": "#0F172A",
        "grid.color": theme.grid,
        "grid.linestyle": "-",
        "grid.linewidth": 0.8,
        "axes.grid": True,
        "axes.axisbelow": True,
        "font.family": theme.font_family,
        "lines.linewidth": theme.line_width,
    })
