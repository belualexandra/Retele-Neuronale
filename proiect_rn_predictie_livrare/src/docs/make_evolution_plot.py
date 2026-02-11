import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Datele proiectului 
stages = ['Etapa 4\n(Schelet)', 'Etapa 5\n(Baseline)', 'Etapa 6\n(Optimizat)']
accuracy = [0.20, 0.72, 0.825] 
f1_score = [0.15, 0.68, 0.793] 

x = np.arange(len(stages))
width = 0.35

# 2. Creare grafic
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, accuracy, width, label='Accuracy', color='#3498db', edgecolor='white')
rects2 = ax.bar(x + width/2, f1_score, width, label='F1-Score (Macro)', color='#2ecc71', edgecolor='white')

# 3. Estetică și Labels
ax.set_ylabel('Scor (0.0 - 1.0)', fontsize=12)
ax.set_title('Evoluția Performanței Modelului: Etapa 4 → Etapa 6', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(stages, fontsize=11)
ax.set_ylim(0, 1.0)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left')

# Adăugare etichete procentuale deasupra barelor
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1%}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold', fontsize=10)

autolabel(rects1)
autolabel(rects2)

# 4. Salvare în docs/results
out_dir = "docs/results"
os.makedirs(out_dir, exist_ok=True) 
out_path = os.path.join(out_dir, "metrics_evolution.png")

plt.tight_layout()
plt.savefig(out_path, dpi=300)
plt.close()

print(f" Graficul evoluției a fost salvat în: {out_path}")