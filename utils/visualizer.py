import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import os

def save_bar_chart(title, labels, values, filename):
    plt.figure(figsize=(10,6))
    sns.barplot(x=labels, y=values)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()

    filepath = f"static/charts/{filename}.png"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath)
    plt.close()
    return filepath
