import tkinter as tk
import speedtest
import matplotlib.pyplot as plt
from datetime import datetime

# Listas para o gráfico
tentativas = []
historico_download = []

def rodar_teste():
    teste = speedtest.Speedtest()
    teste.get_best_server()
    
    # Fazendo os cálculos
    v_download = teste.download() / 10**6
    v_upload = teste.upload() / 10**6
    v_ping = teste.results.ping
    
    # Atualizando a tela
    res_download.config(text=f"{v_download:.2f} Mbps")
    res_upload.config(text=f"{v_upload:.2f} Mbps")
    res_ping.config(text=f"{v_ping} ms")
    
    # Salvando no arquivo de texto
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("historico_internet.txt", "a") as arquivo:
        arquivo.write(f"{agora} - Download: {v_download:.2f} Mbps | Upload: {v_upload:.2f} Mbps\n")
    
    # Guardando dados para o gráfico desta sessão
    tentativas.append(len(tentativas) + 1)
    historico_download.append(v_download)

def mostrar_grafico():
    if not historico_download:
        return
    plt.plot(tentativas, historico_download, marker='o', color='blue')
    plt.title('Desempenho da Sessão')
    plt.xlabel('Vezes que você testou')
    plt.ylabel('Velocidade (Mbps)')
    plt.grid(True)
    plt.show()

app = tk.Tk()
app.title("Speedtest")
app.geometry("250x450")

tk.Label(app, text="DOWNLOAD").pack(pady=10)
res_download = tk.Label(app, text="0.00", font=("Arial", 12, "bold"))
res_download.pack()

tk.Label(app, text="UPLOAD").pack(pady=10)
res_upload = tk.Label(app, text="0.00", font=("Arial", 12, "bold"))
res_upload.pack()

tk.Label(app, text="PING").pack(pady=10)
res_ping = tk.Label(app, text="0", font=("Arial", 12, "bold"))
res_ping.pack()

tk.Button(app, text="START TEST", command=rodar_teste, bg="green", fg="white").pack(pady=15)
tk.Button(app, text="VER GRÁFICO", command=mostrar_grafico).pack(pady=5)

app.mainloop()