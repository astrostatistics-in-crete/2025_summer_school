import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore

# Set seaborn style
sns.set_theme(style="darkgrid")  # Options: "white", "dark", "whitegrid", "darkgrid", "ticks"

# Global settings for Matplotlib
plt.rcParams.update({
    "figure.figsize": (8, 4),   # Default figure size (width, height)
    "axes.titlesize": 14,       # Title font size
    "axes.labelsize": 12,       # Label font size
    "xtick.labelsize": 10,      # X-axis tick font size
    "ytick.labelsize": 10,      # Y-axis tick font size
    "legend.fontsize": 10,      # Legend font size
    "font.size": 10,            # General font size
    "figure.autolayout": True,  # Auto-layout for better spacing
    "axes.grid": True,          # Show grid
    "grid.alpha": 0.3,          # Grid transparency
    "lines.linewidth": 2,       # Default line width
    "lines.markersize": 6,      # Default marker size
    "figure.dpi": 100,          # Resolution of figures
    "savefig.dpi": 300,         # Resolution for saved figures
    "axes.spines.top": False,   # Remove top spine
    "axes.spines.right": False, # Remove right spine
    "text.color": "gray",   # Set all text color
    "axes.labelcolor": "gray",  # Set axis labels color
    "xtick.color": "gray",  # Set x-axis tick labels color
    "ytick.color": "gray",  # Set y-axis tick labels color
    "legend.edgecolor": "gray",  # Set legend edge color
    "legend.labelcolor": "gray"  # Set legend text color    
})