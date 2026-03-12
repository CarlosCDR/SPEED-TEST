#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpeedTestPRO - Interface Avançada com Tkinter
Exibe velocidade, ping e servidor, salva histórico
"""

import tkinter as tk
from tkinter import ttk
import threading
import speedtest
from datetime import datetime
import os
import json

class SpeedTestPRO:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ SpeedTestPRO")
        self.root.geometry("750x900")
        self.root.resizable(True, True)

        # Cores
        self.bg_color = "#0f0f23"
        self.accent_color = "#00d4ff"
        self.bg_secondary = "#1f1f3d"
        self.success_color = "#10b981"
        self.warning_color = "#f59e0b"
        self.error_color = "#ef4444"
        self.text_color = "#ffffff"
        self.root.configure(bg=self.bg_color)

        # Variáveis
        self.testando = False
        self.historico = []
        self.servidor_info = ""
        self.carregar_historico()

        self.criar_interface()

    def criar_interface(self):
        header_frame = tk.Frame(self.root, bg=self.accent_color, height=100)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        tk.Label(header_frame, text="⚡ SPEED TEST PRO", font=("Arial", 32, "bold"),
                 bg=self.accent_color, fg=self.text_color).pack(pady=20)

        # Status
        self.status_var = tk.StringVar(value="Clique em 'Iniciar Teste'")
        tk.Label(self.root, textvariable=self.status_var, font=("Arial", 12),
                 bg=self.bg_color, fg=self.accent_color).pack(pady=10)

        # Progress
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TProgressbar", background=self.accent_color)
        self.progress = ttk.Progressbar(self.root, mode="determinate", length=500, maximum=100, style="TProgressbar")
        self.progress.pack(pady=10, padx=20, fill="x")

        # Resultados
        self.labels = {}
        frame = tk.Frame(self.root, bg=self.bg_secondary)
        frame.pack(fill="both", padx=20, pady=10)
        for icone, nome, key in [("📥","Download","download"), ("📤","Upload","upload"), ("⏱️","Ping","ping"), ("🌐","Servidor","servidor")]:
            self.criar_card(frame, icone, nome, key)

        # Botões
        self.botao_inicio = tk.Button(self.root, text="▶ INICIAR TESTE", font=("Arial",14,"bold"),
                                      bg=self.accent_color, fg=self.bg_color, padx=20, pady=10,
                                      relief="flat", cursor="hand2", command=self.iniciar_teste)
        self.botao_inicio.pack(pady=10, fill="x", padx=20)

        tk.Button(self.root, text="🗑️ Limpar", font=("Arial",12,"bold"),
                  bg=self.bg_secondary, fg=self.text_color, padx=10, pady=8,
                  relief="flat", cursor="hand2", command=self.limpar_resultados).pack(pady=5, fill="x", padx=20)

        # Histórico
        self.stats_var = tk.StringVar(value="Nenhum teste realizado")
        tk.Label(self.root, textvariable=self.stats_var, bg=self.bg_color, fg="#888888", font=("Arial",10),
                 justify="left", wraplength=500).pack(pady=10, padx=20)

    def criar_card(self, parent, icone, titulo, key):
        frame = tk.Frame(parent, bg=self.bg_secondary, relief="raised", bd=1)
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=f"{icone} {titulo}", font=("Arial",12,"bold"), bg=self.bg_secondary, fg=self.text_color).pack(anchor="w", padx=5)
        label = tk.Label(frame, text="--", font=("Arial",14,"bold"), bg=self.bg_secondary, fg=self.success_color)
        label.pack(anchor="w", padx=15, pady=5)
        self.labels[key] = label

    def iniciar_teste(self):
        if self.testando: return
        self.testando=True
        self.botao_inicio.config(state="disabled")
        self.progress["value"]=0
        self.status_var.set("Conectando aos servidores...")
        threading.Thread(target=self.executar_teste, daemon=True).start()

    def executar_teste(self):
        try:
            st = speedtest.Speedtest()
            self.status_var.set("🔍 Localizando melhor servidor...")
            self.progress["value"]=10
            self.root.update()
            servidor = st.get_best_server()
            self.servidor_info = f"{servidor['sponsor']}, {servidor['name']}, {servidor['country']}"
            self.labels["servidor"].config(text=self.servidor_info)

            self.status_var.set("📥 Testando Download...")
            self.progress["value"]=30
            self.root.update()
            download = st.download()/1_000_000
            self.labels["download"].config(text=f"{download:.2f} Mbps")

            self.status_var.set("📤 Testando Upload...")
            self.progress["value"]=60
            self.root.update()
            upload = st.upload()/1_000_000
            self.labels["upload"].config(text=f"{upload:.2f} Mbps")

            self.status_var.set("⏱️ Medindo Ping...")
            self.progress["value"]=90
            self.root.update()
            ping = st.results.ping
            self.labels["ping"].config(text=f"{ping:.2f} ms")

            self.salvar_historico(download, upload, ping, self.servidor_info)
            self.atualizar_stats()

            self.status_var.set("✅ Teste concluído!")
            self.progress["value"]=100
        except Exception as e:
            self.status_var.set(f"❌ Erro: {e}")
        finally:
            self.testando=False
            self.botao_inicio.config(state="normal")

    def limpar_resultados(self):
        for key in self.labels: self.labels[key].config(text="--")
        self.status_var.set("Clique em 'Iniciar Teste'")
        self.progress["value"]=0

    def salvar_historico(self, download, upload, ping, servidor):
        now=datetime.now().strftime('%d/%m/%Y %H:%M')
        self.historico.append({"timestamp":now,"download":download,"upload":upload,"ping":ping,"servidor":servidor})
        with open("historico_testes.json","w",encoding="utf-8") as f:
            json.dump(self.historico,f,indent=2)

    def carregar_historico(self):
        if os.path.exists("historico_testes.json"):
            with open("historico_testes.json","r",encoding="utf-8") as f:
                self.historico=json.load(f)
        else: self.historico=[]

    def atualizar_stats(self):
        if not self.historico:
            self.stats_var.set("Nenhum teste realizado")
            return
        downloads=[h['download'] for h in self.historico]
        uploads=[h['upload'] for h in self.historico]
        pings=[h['ping'] for h in self.historico]
        stats=f"Total de testes: {len(self.historico)}\nDownload: Min {min(downloads):.2f} | Max {max(downloads):.2f} | Média {sum(downloads)/len(downloads):.2f} Mbps\nUpload: Min {min(uploads):.2f} | Max {max(uploads):.2f} | Média {sum(uploads)/len(uploads):.2f} Mbps\nPing: Min {min(pings):.2f} | Max {max(pings):.2f} | Média {sum(pings)/len(pings):.2f} ms"
        self.stats_var.set(stats)

def main():
    root=tk.Tk()
    app=SpeedTestPRO(root)
    root.mainloop()

if __name__=="__main__":
    main()