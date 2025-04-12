import pandas as pd
import matplotlib.pyplot as plt

# === CONFIGURE AQUI CADA CURVA QUE QUISER PLOTAR ===
curvas = [
    # {"arquivo": "1000-simbolos/ofdm.csv", "label": "OFDM", "cor": "blue"},
    # {"arquivo": "ofdm-ref.csv", "label": "OFDM-REF", "cor": "green"},
    {"arquivo": "100000-simbolos/pam-2.csv", "label": "PAM-2", "cor": "orange"},
    {"arquivo": "100000-simbolos/pam-4.csv", "label": "PAM-4", "cor": "green"},
    {"arquivo": "100000-simbolos/pam-8.csv", "label": "PAM-8", "cor": "red"},
    {"arquivo": "100000-simbolos/pam-16.csv", "label": "PAM-16", "cor": "purple"},
    {"arquivo": "pam-2-ref.csv", "label": "PAM-2-REF", "cor": "brown"},
    {"arquivo": "pam-4-ref.csv", "label": "PAM-4-REF", "cor": "black"},
    {"arquivo": "pam-8-ref.csv", "label": "PAM-8-REF", "cor": "gold"},
    {"arquivo": "pam-16-ref.csv", "label": "PAM-16-REF", "cor": "navy"},
]

plt.figure(figsize=(10, 6))

# === LOOP PARA PLOTAR CADA CURVA ===
for curva in curvas:
    df = pd.read_csv(curva["arquivo"])  # Leitura do CSV
    df = df.sort_values(by=df.columns[0])  # Ordena pelo eixo X (SNR)
    x = df.iloc[:, 0]  # Primeira coluna = SNR
    y = df.iloc[:, 1]  # Segunda coluna = BER
    plt.plot(x, y, label=curva["label"], color=curva["cor"])

# === CONFIGURAÇÕES DO GRÁFICO ===
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.title("BER vs SNR")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.legend()
plt.tight_layout()
plt.show()
