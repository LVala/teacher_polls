import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def create_plot(subject):
    choices = subject.choice_set.all()
    teacher_labels = [f"{str(i.teacher)} ({i.total_voters_number})" for i in choices]
    teacher_labels = [f"{i.split()[0][0]}. {i.split()[1]}" for i in teacher_labels]

    quality_values = [i.get_score('total_quality') for i in choices]
    friendliness_values = [i.get_score('total_friendliness') for i in choices]
    motivation_values = [i.get_score('total_motivation') for i in choices]
    ease_values = [i.get_score('total_ease') for i in choices]
    general_values = [i.get_score('total_general') for i in choices]
    
    x = np.arange(len(teacher_labels))
    width = 0.1

    fig, ax = plt.subplots(figsize=(10, 5), dpi=100, tight_layout=True)
    rects1 = ax.bar(x - 4*width/2, quality_values, width, label='Jakość nauczania')
    rects2 = ax.bar(x - 2*width/2, friendliness_values, width, label='Przyjazne podejście')
    rects3 = ax.bar(x, motivation_values, width, label='Motywowanie do nauki')
    rects4 = ax.bar(x + 2*width/2, ease_values, width, label='Łatowść zdania')
    rects5 = ax.bar(x + 4*width/2, general_values, width, label='Ogólna ocena')
    rects = [rects1, rects2, rects3, rects4, rects5]

    ax.set_ylabel("Ocena (1-10)")
    ax.set_title(f"Ocena prowadzących - {subject.name} {datetime.now().year}")
    ax.set_xticks(x, teacher_labels)
    ax.set_yticks(np.arange(1,12))
    ax.legend(loc='upper right', mode='expand', ncol=5)

    for i in rects: ax.bar_label(i, fmt='')
    
    plt.style.use('seaborn-darkgrid')

    plt.savefig(f".\polls\static\polls\images\{subject.id}_plot.png")