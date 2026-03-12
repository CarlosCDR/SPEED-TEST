#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpeedTest GUI - Medidor de Velocidade com Tkinter
Exibe Download, Upload, Ping e Servidor
"""

import tkinter as tk
from tkinter import ttk
import threading
import speedtest

class SpeedTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 SpeedTest GUI")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Cores
        self.bg_color = "#1e1e2e"
        self.accent_color = "#00d4ff"
        self.success_color = "#00ff88"
        self.warning_color = "#ffaa00"
        self.error_color = "#ff4444"
        self.text_color = "#ffffff"
        self.root.configure(bg=self.bg_color)

        self.testando = False
        self.labels = {}

        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.root, text="🚀 SPEED TEST", font=("Arial", 24, "bold"),
                 bg=self.accent_color, fg=self.bg_color).pack(fill="x", pady=10)

        # Status
        self.status_var = tk.StringVar(value="Pronto para testar")
        tk.Label(self.root, textvariable=self.status_var, font=("Arial", 12),
                 bg=self.bg_color, fg=self.accent_color).pack(pady=5)

        # Progress
        self.progress = ttk.Progressbar(self.root, mode="determinate", length=400, maximum=100)
        self.progress.pack(pady=10, padx=20)

        # Resultados
        for icone, nome, key in [("📥","Download","download"), ("📤","Upload","upload"),
                                  ("⏱️","Ping","ping"), ("🌐","Servidor","servidor")]:
            frame = tk.Frame(self.root, bg="#2d2d3d")
            frame.pack(fill="x", padx=20, pady=5)
            tk.Label(frame, text=f"{icone} {nome}", font=("Arial",12,"bold"),
                     bg="#2d2d3d", fg=self.text_color).pack(anchor="w", padx=5)
            label = tk.Label(frame, text="--", font=("Arial",14,"bold"),
                             bg="#2d2d3d", fg=self.success_color)
            label.pack(anchor="w", padx=15, pady=5)
            self.labels[key] = label

        # Botão
        self.botao_teste = tk.Button(self.root, text="▶ INICIAR TESTE", font=("Arial",14,"bold"),
                                     bg=self.accent_color, fg=self.bg_color, padx=20, pady=10,
                                     command=self.iniciar_teste)
        self.botao_teste.pack(pady=15, fill="x", padx=20)

        # Botão limpar
        tk.Button(self.root, text="🗑️ Limpar", font=("Arial",12,"bold"),
                  bg="#404050", fg=self.text_color, padx=10, pady=8,
                  command=self.limpar_resultados).pack(pady=5, fill="x", padx=20)

    def iniciar_teste(self):
        if self.testando: return
        self.testando = True
        self.botao_teste.config(state="disabled")
        self.progress["value"]=0
        self.status_var.set("Conectando aos servidores...")
        threading.Thread(target=self.executar_teste, daemon=True).start()

    def executar_teste(self):
        try:
            st = speedtest.Speedtest()
            self.status_var.set("🔍 Localizando melhor servidor...")
            self.progress["value"]=20
            self.root.update()

            servidor = st.get_best_server()
            servidor_info = f"{servidor['sponsor']}, {servidor['name']}, {servidor['country']}"
            self.labels["servidor"].config(text=servidor_info)

            self.status_var.set("📥 Testando Download...")
            self.progress["value"]=40
            self.root.update()
            download = st.download()/1_000_000
            self.labels["download"].config(text=f"{download:.2f} Mbps")

            self.status_var.set("📤 Testando Upload...")
            self.progress["value"]=70
            self.root.update()
            upload = st.upload()/1_000_000
            self.labels["upload"].config(text=f"{upload:.2f} Mbps")

            self.status_var.set("⏱️ Medindo Ping...")
            self.progress["value"]=90
            self.root.update()
            ping = st.results.ping
            self.labels["ping"].config(text=f"{ping:.2f} ms")

            self.status_var.set("✅ Teste concluído!")
            self.progress["value"]=100
        except Exception as e:
            self.status_var.set(f"❌ Erro: {e}")
            self.progress["value"]=0
        finally:
            self.testando=False
            self.botao_teste.config(state="normal")

    def limpar_resultados(self):
        for key in self.labels: self.labels[key].config(text="--")
        self.status_var.set("Pronto para testar")
        self.progress["value"]=0

def main():
    root = tk.Tk()
    app = SpeedTestGUI(root)
    root.mainloop()

if __name__=="__main__":
    main()