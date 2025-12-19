import random
import matplotlib.pyplot as plt
import vizcraft as vc

# 1) LINE
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
sales_2024 = [12, 15, 14, 18, 21, 19, 23, 25]
vc.styled_line(
    x=months, y=sales_2024,
    title="Monthly sales (2024)",
    xlabel="Month", ylabel="Sales (k$)",
    marker="o",
    show=False
)

# 2) LINE comparison (same axis)
sales_2025 = [14, 16, 15, 20, 24, 22, 26, 29]
fig, ax = vc.styled_line(
    x=months, y=sales_2025,
    title="Monthly sales comparison (2024 vs 2025)",
    xlabel="Month", ylabel="Sales (k$)",
    marker="s",
    show=False
)
ax.plot(months, sales_2024, marker="o")
ax.legend(["2025", "2024"], frameon=False)

# 3) SCATTER
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [45, 50, 55, 60, 66, 70, 78, 85]
vc.styled_scatter(
    x=hours, y=scores,
    title="Study hours vs exam score",
    xlabel="Hours", ylabel="Score",
    size=90,
    show=False
)

# 4) BAR
teams = ["Backend", "Frontend", "Data", "DevOps", "Design"]
tickets_closed = [28, 34, 22, 18, 25]
vc.styled_bar(
    categories=teams, values=tickets_closed,
    title="Tickets closed per team",
    xlabel="Team", ylabel="Tickets",
    show=False
)

# 5) HIST
random.seed(7)
latencies_ms = [max(20, int(random.gauss(180, 45))) for _ in range(250)]
vc.styled_hist(
    data=latencies_ms, bins=18,
    title="API latency distribution",
    xlabel="Latency (ms)", ylabel="Requests",
    show=False
)

# 6) PIE
sources = ["Direct", "Search", "Social", "Referral", "Email"]
traffic = [38, 27, 16, 12, 7]
vc.styled_pie(
    labels=sources, values=traffic,
    title="Website traffic sources",
    show=False
)

# ✅ Show all figures at once
plt.show()
