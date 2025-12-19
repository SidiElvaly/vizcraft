from __future__ import annotations

from typing import Iterable, Sequence, Optional
import matplotlib.pyplot as plt

from .style import apply_style, DEFAULT_THEME, Theme

def _base_ax(ax=None, theme: Theme = DEFAULT_THEME):
    apply_style(theme)
    if ax is None:
        fig, ax = plt.subplots(figsize=(7.2, 4.2))
    else:
        fig = ax.figure
    return fig, ax

def styled_line(
    x: Sequence[float],
    y: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    marker: str = "o",
    ax=None,
    theme: Theme = DEFAULT_THEME,
    show: bool = True,
):
    fig, ax = _base_ax(ax=ax, theme=theme)
    c = color or theme.primary
    ax.plot(x, y, color=c, marker=marker, markersize=theme.marker_size)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax

def styled_scatter(
    x: Sequence[float],
    y: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    size: int = 60,
    alpha: float = 0.85,
    ax=None,
    theme: Theme = DEFAULT_THEME,
    show: bool = True,
):
    fig, ax = _base_ax(ax=ax, theme=theme)
    c = color or theme.secondary
    ax.scatter(x, y, s=size, alpha=alpha, color=c, edgecolor=theme.bg, linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax

def styled_bar(
    categories: Sequence[str],
    values: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    ax=None,
    theme: Theme = DEFAULT_THEME,
    show: bool = True,
):
    fig, ax = _base_ax(ax=ax, theme=theme)
    c = color or theme.accent
    ax.bar(categories, values, color=c, edgecolor=theme.grid, linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax

def styled_hist(
    data: Sequence[float],
    bins: int = 10,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "Count",
    color: Optional[str] = None,
    ax=None,
    theme: Theme = DEFAULT_THEME,
    show: bool = True,
):
    fig, ax = _base_ax(ax=ax, theme=theme)
    c = color or theme.primary
    ax.hist(data, bins=bins, color=c, alpha=0.9, edgecolor=theme.bg)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax

def styled_pie(
    labels: Sequence[str],
    values: Sequence[float],
    title: str = "",
    colors: Optional[Sequence[str]] = None,
    ax=None,
    theme: Theme = DEFAULT_THEME,
    show: bool = True,
):
    fig, ax = _base_ax(ax=ax, theme=theme)
    # Palette par défaut cohérente
    if colors is None:
        colors = [theme.primary, theme.secondary, theme.accent, theme.muted, theme.danger][:len(values)]
    wedges, _ = ax.pie(values, labels=labels, colors=list(colors), startangle=90)
    ax.set_title(title)
    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax
