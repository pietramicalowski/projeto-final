import matplotlib.pyplot as plt

# Configura uma figura com 2 gráficos lado a lado (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.patch.set_facecolor('#F8FAFC')

# ==============================================================================
# GRÁFICO 1: Horas de Sono Recomendadas por Idade
# ==============================================================================
faixas_etarias = [
    'Crianças\n(6-12 anos)',
    'Adolescentes\n(13-17 anos)',
    'Jovens Adultos\n(18-25 anos)',
    'Adultos\n(26-64 anos)',
]
horas_minimas = [9, 8, 7, 7]
horas_maximas = [12, 10, 9, 9]
cores_g1 = ['#6366F1', '#F59E0B', '#94A3B8', '#94A3B8']  # Destaque para Adolescentes

ax1.bar(
    faixas_etarias,
    [mx - mn for mx, mn in zip(horas_maximas, horas_minimas)],
    bottom=horas_minimas,
    color=cores_g1,
    width=0.5,
    edgecolor='#1E1B4B',
    linewidth=1.2,
)

for i, (mn, mx) in enumerate(zip(horas_minimas, horas_maximas)):
    ax1.text(
        i,
        mx + 0.3,
        f'{mn}h a {mx}h',
        ha='center',
        va='bottom',
        fontweight='bold',
        fontsize=11,
        color='#1E1B4B',
    )

ax1.set_title(
    'Tempo de Sono Recomendado por Idade',
    fontsize=14,
    fontweight='bold',
    color='#1E1B4B',
    pad=15,
)
ax1.set_ylabel('Horas de Sono por Noite', fontsize=11, color='#1E1B4B')
ax1.set_ylim(0, 14)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# ==============================================================================
# GRÁFICO 2: Impacto do Celular Antes de Dormir (Duração Média)
# ==============================================================================
habitos = [
    'Sem telas 1h\nantes de dormir',
    'Uso moderado\n(15-30 min)',
    'Uso intenso\n(+1h na cama)',
]
media_horas = [8.5, 7.1, 5.8]
cores_g2 = ['#10B981', '#F59E0B', '#EF4444']

barras_g2 = ax2.bar(
    habitos,
    media_horas,
    color=cores_g2,
    width=0.5,
    edgecolor='#1E1B4B',
    linewidth=1.2,
)

ax2.axhline(
    8,
    color='#4F46E5',
    linestyle='--',
    linewidth=1.8,
    label='Mínimo Ideal (8h)',
)

for barra in barras_g2:
    altura = barra.get_height()
    ax2.text(
        barra.get_x() + barra.get_width() / 2.0,
        altura + 0.2,
        f'{altura:.1f}h',
        ha='center',
        va='bottom',
        fontweight='bold',
        fontsize=11,
        color='#1E1B4B',
    )

ax2.set_title(
    'Impacto das Telas no Sono dos Adolescentes',
    fontsize=14,
    fontweight='bold',
    color='#1E1B4B',
    pad=15,
)
ax2.set_ylabel('Média de Horas Dormidas', fontsize=11, color='#1E1B4B')
ax2.set_ylim(0, 10)
ax2.legend(loc='upper right')
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# Ajusta o espaçamento e salva a imagem combinada em alta resolução
plt.tight_layout(pad=3.0)
plt.savefig('graficos_sono_completos.png', dpi=300)
plt.show()