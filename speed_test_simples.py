#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Versão Simplificada - Teste de Velocidade da Internet
Usa apenas bibliotecas padrão do Python (sem dependências externas)
"""

import urllib.request
import time
from datetime import datetime


def testar_velocidade_simples():
    """
    Teste simples de velocidade usando urllib3
    Baixa um arquivo pequeno e mede a velocidade
    """
    print("=" * 60)
    print("TESTE SIMPLES DE VELOCIDADE DA INTERNET")
    print("=" * 60)
    print(f"\nData/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    # URLs de teste (servidores públicos)
    urls_teste = [
        "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",  # 10KB
        "http://ipv4.download.thinkbroadband.com/10MB.zip",  # 10MB
    ]
    
    try:
        print("\n📥 Testando velocidade de DOWNLOAD...")
        print("Aguarde...\n")
        
        for url in urls_teste:
            try:
                velocidades = []
                
                for tentativa in range(3):
                    print(f"  Tentativa {tentativa + 1}/3...", end=" ", flush=True)
                    
                    tempo_inicio = time.time()
                    
                    # Baixar arquivo
                    with urllib.request.urlopen(url, timeout=30) as response:
                        dados = response.read()
                    
                    tempo_decorrido = time.time() - tempo_inicio
                    
                    # Calcular velocidade
                    tamanho_bytes = len(dados)
                    tamanho_bits = tamanho_bytes * 8
                    velocidade_bps = tamanho_bits / tempo_decorrido
                    velocidade_mbps = velocidade_bps / 1_000_000
                    
                    velocidades.append(velocidade_mbps)
                    print(f"{velocidade_mbps:.2f} Mbps")
                
                # Média das velocidades
                media = sum(velocidades) / len(velocidades)
                
                print(f"\n  ✓ Velocidade média: {media:.2f} Mbps")
                
                print("\n" + "=" * 60)
                print("RESULTADO")
                print("=" * 60)
                print(f"\n📊 Velocidade estimada: {media:.2f} Mbps")
                
                # Classificação simples
                if media >= 50:
                    print("✓ Velocidade EXCELENTE")
                elif media >= 25:
                    print("✓ Boa velocidade")
                elif media >= 10:
                    print("◐ Velocidade adequada")
                elif media >= 5:
                    print("◑ Velocidade mínima")
                else:
                    print("✗ Velocidade baixa")
                
                print("\n" + "=" * 60)
                
                # Salvar resultado
                with open('resultado_velocidade_simples.txt', 'a', encoding='utf-8') as f:
                    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    f.write(f"\n{timestamp} | Velocidade: {media:.2f} Mbps")
                
                print("\n✓ Resultado salvo em 'resultado_velocidade_simples.txt'")
                break
                
            except Exception as e:
                print(f"Erro: {str(e)}")
                continue
    
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
        print("\nVerifique sua conexão com a internet e tente novamente.")


if __name__ == "__main__":
    try:
        testar_velocidade_simples()
    except KeyboardInterrupt:
        print("\n\nTeste cancelado pelo usuário.")
    finally:
        input("\nPressione ENTER para sair...")
