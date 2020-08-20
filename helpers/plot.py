from matplotlib.patches import Rectangle
from tempfile import NamedTemporaryFile
from matplotlib.lines import Line2D
from matplotlib.image import imread
import matplotlib.pyplot as plt
import seaborn as sns

colors_cats = {
    "Art": [0.22352941, 0.23137255, 0.4745098, 1.],
    "Business": [0.32156863, 0.32941176, 0.63921569, 1.],
    "Government and Politics": [0.61176471, 0.61960784, 0.87058824, 1.],
    "Healthcare": [0.54901961, 0.63529412, 0.32156863, 1.],
    "Media": [0.70980392, 0.81176471, 0.41960784, 1.],
    "Non-Governmental Organization": [0.54901961, 0.42745098, 0.19215686, 1.],
    "Other": [0.90588235, 0.72941176, 0.32156863, 1.],
    "Outspoken Political Supporter": [0.90588235, 0.79607843, 0.58039216, 1.],
    "Porn": [0.67843137, 0.28627451, 0.29019608, 1.],
    "Public Services": [0.90588235, 0.58823529, 0.61176471, 1.],
    "Religion": [0.48235294, 0.25490196, 0.45098039, 1.],
    "Science": [0.80784314, 0.42745098, 0.74117647, 1.],
    "Sport": [0.87058824, 0.61960784, 0.83921569, 1.]
}


def boxplot_2d(x, y, ax, color, whis=1.5):
    xlimits = [np.percentile(x, q) for q in (25, 50, 75)]
    ylimits = [np.percentile(y, q) for q in (25, 50, 75)]

    ##the box
    box = Rectangle(
        (xlimits[0], ylimits[0]),
        (xlimits[2] - xlimits[0]),
        (ylimits[2] - ylimits[0]),
        ec='k',
        color=color,

        zorder=2
    )
    ax.add_patch(box)

    ##the x median
    vline = Line2D(
        [xlimits[1], xlimits[1]], [ylimits[0], ylimits[2]],
        color='k',
        zorder=2,
        lw=0.5
    )
    ax.add_line(vline)

    ##the y median
    hline = Line2D(
        [xlimits[0], xlimits[2]], [ylimits[1], ylimits[1]],
        color='k',
        zorder=2,
        lw=0.5
    )
    ax.add_line(hline)

    ##the central point
    ax.scatter([xlimits[1]], [ylimits[1]], facecolors=color, edgecolors="k", zorder=3)
    #     ax.scatter(
    #         x[mask],y[mask],
    #         facecolors='none', edgecolors=color, size=5
    #     )
    ##the x-whisker
    ##defined as in matplotlib boxplot:
    ##As a float, determines the reach of the whiskers to the beyond the
    ##first and third quartiles. In other words, where IQR is the
    ##interquartile range (Q3-Q1), the upper whisker will extend to
    ##last datum less than Q3 + whis*IQR). Similarly, the lower whisker
    ####will extend to the first datum greater than Q1 - whis*IQR. Beyond
    ##the whiskers, data are considered outliers and are plotted as
    ##individual points. Set this to an unreasonably high value to force
    ##the whiskers to show the min and max values. Alternatively, set this
    ##to an ascending sequence of percentile (e.g., [5, 95]) to set the
    ##whiskers at specific percentiles of the data. Finally, whis can
    ##be the string 'range' to force the whiskers to the min and max of
    ##the data.
    iqr = xlimits[2] - xlimits[0]

    ##left
    left = np.min(x[x > xlimits[0] - whis * iqr])
    whisker_line = Line2D(
        [left, xlimits[0]], [ylimits[1], ylimits[1]],
        color='k',
        zorder=2,
        lw=0.5
    )
    ax.add_line(whisker_line)
    whisker_bar = Line2D(
        [left, left], [ylimits[0], ylimits[2]],
        color='k',
        zorder=2,
        lw=1
    )
    ax.add_line(whisker_bar)

    ##right
    right = np.max(x[x < xlimits[2] + whis * iqr])
    whisker_line = Line2D(
        [right, xlimits[2]], [ylimits[1], ylimits[1]],
        color='k',
        zorder=2,
        lw=0.5
    )

    ax.add_line(whisker_line)
    whisker_bar = Line2D(
        [right, right], [ylimits[0], ylimits[2]],
        color='k',
        zorder=2,
        lw=1
    )
    ax.add_line(whisker_bar)

    ##the y-whisker
    iqr = ylimits[2] - ylimits[0]

    ##bottom
    bottom = np.min(y[y > ylimits[0] - whis * iqr])
    whisker_line = Line2D(
        [xlimits[1], xlimits[1]], [bottom, ylimits[0]],
        color='k',
        zorder=2,
        lw=0.5
    )

    ax.add_line(whisker_line)
    whisker_bar = Line2D(
        [xlimits[0], xlimits[2]], [bottom, bottom],
        color='k',
        zorder=2,
        lw=1
    )

    ax.add_line(whisker_bar)

    ##top
    top = np.max(y[y < ylimits[2] + whis * iqr])
    whisker_line = Line2D(
        [xlimits[1], xlimits[1]], [top, ylimits[2]],
        color='k',
        zorder=2,
        lw=0.5
    )
    ax.add_line(whisker_line)
    whisker_bar = Line2D(
        [xlimits[0], xlimits[2]], [top, top],
        color='k',
        zorder=2,
        lw=1
    )
    ax.add_line(whisker_bar)

    ##outliers
    mask = (x < left) | (x > right) | (y < bottom) | (y > top)
    ax.scatter(
        x[mask], y[mask],
        facecolors='none', edgecolors=color, s=5
    )


def get_size(fig, dpi=100):
    with NamedTemporaryFile(suffix='.png') as f:
        fig.savefig(f.name, bbox_inches='tight', dpi=dpi)
        height, width, _channels = imread(f.name).shape
        return width / dpi, height / dpi


def set_size(fig, size, dpi=100, eps=1e-2, give_up=2, min_size_px=10):
    target_width, target_height = size
    set_width, set_height = target_width, target_height  # reasonable starting point
    deltas = []  # how far we have
    while True:
        fig.set_size_inches([set_width, set_height])
        actual_width, actual_height = get_size(fig, dpi=dpi)
        set_width *= target_width / actual_width
        set_height *= target_height / actual_height
        deltas.append(abs(actual_width - target_width) + abs(actual_height - target_height))
        if deltas[-1] < eps:
            return True
        if len(deltas) > give_up and sorted(deltas[-give_up:]) == deltas[-give_up:]:
            return False
        if set_width * dpi < min_size_px or set_height * dpi < min_size_px:
            return False


def plot_categorical_balance(ylabels_func=None):
    fig, axs = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True, gridspec_kw={"wspace": 0.05})
    axs[0].xaxis.grid()
    axs[1].xaxis.grid()

    sns.barplot(y="index", x="val", hue="group", data=df_cats[df_cats.kind == "Source"], orient="h", ax=axs[0],
                zorder=2)
    sns.barplot(y="index", x="val", hue="group", data=df_cats[df_cats.kind == "Matched"], orient="h", ax=axs[1],
                zorder=2)
    axs[0].legend()
    axs[1].legend([], fancybox=False, frameon=False, shadow=False)
    labels = [ylabels_func(c.get_text()) for c in axs[0].get_yticklabels()]
    axs[0].set_yticklabels(labels)
    axs[0].set_title("Before Matching")
    axs[1].set_title("After Matching")
    for ax in axs:
        ax.set_ylabel("")
        ax.set_xlabel("")

    set_size(fig, (14, 5))
    return fig, axs
