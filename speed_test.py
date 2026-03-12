#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Software para medir a velocidade da internet
Usa a biblioteca speedtest-cli para testes precisos
"""

import speedtest
import time
from datetime import datetime


def converter_para_megabits(bits):
    """Converte bits por segundo para megabits por segundo"""
    return bits / 1_000_000


def formatar_tempo(segundos):
    """Formata segundos em formato legível"""
    if segundos < 60:
        return f"{segundos:.2f}s"
    elif segundos < 3600:
        minutos = segundos / 60
        return f"{minutos:.2f}m"
    else:
        horas = segundos / 3600
        return f"{horas:.2f}h"


def medir_velocidade():
    """
    Mede a velocidade da internet
    """
    print("=" * 60)
    print("TESTE DE VELOCIDADE DA INTERNET")
    print("=" * 60)
    print(f"\nData/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\nConectando aos servidores de teste...")
    print("Por favor, aguarde...\n")
    
    try:
        # Criar objeto Speedtest
        st = speedtest.Speedtest()
        
        # Obter melhor servidor
        print("► Localizando melhor servidor...")
        st.get_best_server()
        print(f"  Servidor selecionado: {st.best['sponsor']}")
        print(f"  Localização: {st.best['country']}")
        print(f"  Cidade: {st.best['name']}")
        
        # Teste de Download
        print("\n► Testando velocidade de DOWNLOAD...")
        tempo_inicio = time.time()
        download_speed = st.download()
        tempo_download = time.time() - tempo_inicio
        
        print(f"  ✓ Concluído em {formatar_tempo(tempo_download)}")
        
        # Teste de Upload
        print("\n► Testando velocidade de UPLOAD...")
        tempo_inicio = time.time()
        upload_speed = st.upload()
        tempo_upload = time.time() - tempo_inicio
        
        print(f"  ✓ Concluído em {formatar_tempo(tempo_upload)}")
        
        # Teste de Ping
        print("\n► Medindo PING (latência)...")
        ping = st.results.ping
        print(f"  ✓ Concluído")
        
        # Exibir resultados
        print("\n" + "=" * 60)
        print("RESULTADOS DO TESTE")
        print("=" * 60)
        print(f"\n📥 Velocidade de Download: {converter_para_megabits(download_speed):.2f} Mbps")
        print(f"📤 Velocidade de Upload:   {converter_para_megabits(upload_speed):.2f} Mbps")
        print(f"⏱️  Ping (Latência):        {ping:.2f} ms")
        print("\n" + "=" * 60)
        
        # Classificação
        download_mb = converter_para_megabits(download_speed)
        print("\nClassificação:")
        if download_mb >= 50:
            print("✓ Velocidade EXCELENTE para praticamente qualquer atividade")
        elif download_mb >= 25:
            print("✓ Boa velocidade para streaming 4K e jogos")
        elif download_mb >= 10:
            print("◐ Velocidade adequada para streaming HD e homeoffice")
        elif download_mb >= 5:
            print("◑ Velocidade mínima - pode ter problemas com múltiplos dispositivos")
        else:
            print("✗ Velocidade muito baixa - considere mudar de provedor")
        
        print("\n" + "=" * 60)
        
        # Salvar resultados em arquivo
        salvar_resultados(download_speed, upload_speed, ping)
        
    except Exception as e:
        print(f"\n❌ Erro durante o teste: {str(e)}")
        print("\nCertifique-se de que:")
        print("  • Você tem conexão com a internet")
        print("  • A biblioteca speedtest está instalada")
        print("  • Tente novamente em alguns momentos")


def salvar_resultados(download, upload, ping):
    """Salva os resultados em um arquivo de log"""
    try:
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        download_mb = converter_para_megabits(download)
        upload_mb = converter_para_megabits(upload)
        
        with open('resultado_velocidade.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n{timestamp} | Download: {download_mb:.2f} Mbps | Upload: {upload_mb:.2f} Mbps | Ping: {ping:.2f} ms")
        
        print(f"✓ Resultados salvos em 'resultado_velocidade.txt'")
    except Exception as e:
        print(f"⚠️  Não foi possível salvar os resultados: {str(e)}")


if __name__ == "__main__":
    medir_velocidade()
    
    input("\nPressione ENTER para sair...")
