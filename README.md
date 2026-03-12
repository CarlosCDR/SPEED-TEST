# 🚀 Speed Test Internet - Software de Medição de Velocidade

Um aplicativo Python completo com **3 versões** para medir a velocidade da sua conexão de internet!

## 📋 Funcionalidades Principais

- ✅ Mede velocidade de **Download** em Mbps
- ✅ Mede velocidade de **Upload** em Mbps  
- ✅ Mede **Ping** (latência) em ms
- ✅ Mostra informações do servidor de teste
- ✅ Classifica sua velocidade com emojis
- ✅ Salva histórico de resultados
- ✅ **NOVO**: Interface gráfica moderna com ícones
- ✅ **NOVO**: Versão PRO com gráficos e análises

## � Como usar

### 🎯 3 VERSÕES DISPONÍVEIS:

#### **Versão 1: INTERFACE GRÁFICA MODERNA** ⭐ (Recomendada)
Elegante interface visual com ícones e design moderno

**Opção 1 - Duplo Clique (Mais Fácil):**
```
Duplo clique em: executar_gui.bat
```

**Opção 2 - PowerShell:**
```powershell
cd "c:\teste python"
python speed_test_gui.py
```

---

#### **Versão 2: INTERFACE AVANÇADA (PRO)** 🌟
Com gráficos, histórico detalhado e análises

**Opção 1 - Duplo Clique:**
```
Duplo clique em: executar_pro.bat
```

**Opção 2 - PowerShell:**
```powershell
python speed_test_pro.py
```

---

#### **Versão 3: LINHA DE COMANDO** 💻
Versão completa em modo texto

**Opção 1 - Duplo Clique:**
```
Duplo clique em: executar.bat
```

**Opção 2 - PowerShell:**
```powershell
python speed_test.py
```

---

#### **Versão 4: SIMPLIFICADA** (Sem Dependências)
Usa apenas bibliotecas padrão do Python

```powershell
python speed_test_simples.py
```

## 📊 O que o programa faz

1. **Conecta aos servidores de teste** - Procura o melhor servidor Speedtest
2. **Teste de Download** - Mede a velocidade de download
3. **Teste de Upload** - Mede a velocidade de upload
4. **Teste de Ping** - Mede a latência da conexão
5. **Classifica sua velocidade** - Apresenta uma análise da qualidade

## 📈 Classificação de Velocidade

| Velocidade | Classificação | Uso |
|-----------|---------------|-----|
| ≥ 50 Mbps | EXCELENTE | 4K, múltiplos devices |
| 25-50 Mbps | BOA | Streaming 4K, jogos |
| 10-25 Mbps | ADEQUADA | Streaming HD, homeoffice |
| 5-10 Mbps | MÍNIMA | Navegação básica |
| < 5 Mbps | BAIXA | Considere mudar de provedor |

## 💾 Histórico de Resultados

Os resultados são salvos automaticamente em `resultado_velocidade.txt`:

```
11/03/2026 14:30:45 | Download: 85.45 Mbps | Upload: 25.32 Mbps | Ping: 12.50 ms
11/03/2026 15:45:10 | Download: 82.10 Mbps | Upload: 24.98 Mbps | Ping: 13.20 ms
```

## ⚠️ Observações Importantes

- O teste leva alguns minutos para ser concluído
- Feche outros programas que usem a internet para resultados mais precisos
- O teste usa dados de sua conexão
- Você precisa de conexão com a internet para rodar

## 🆘 Solução de Problemas

**Erro: "No module named 'speedtest'"**
- Execute: `pip install speedtest-cli`

**Teste muito lento**
- Tente desconectar outros dispositivos da rede
- Feche programas que usem internet (downloads, streaming)

**Erro de conexão**
- Verifique sua conexão de internet
- Tente novamente em alguns momentos

## 📝 Exemplo de Saída

```
============================================================
TESTE DE VELOCIDADE DA INTERNET
============================================================

Data/Hora: 11/03/2026 14:30:45

Conectando aos servidores de teste...
Por favor, aguarde...

► Localizando melhor servidor...
  Servidor selecionado: Virtua Telecomunicações
  Localização: Brazil
  Cidade: São Paulo

► Testando velocidade de DOWNLOAD...
  ✓ Concluído em 45.23s

► Testando velocidade de UPLOAD...
  ✓ Concluído em 30.12s

► Medindo PING (latência)...
  ✓ Concluído

============================================================
RESULTADOS DO TESTE
============================================================

📥 Velocidade de Download: 85.45 Mbps
📤 Velocidade de Upload:   25.32 Mbps
⏱️  Ping (Latência):        12.50 ms

============================================================

Classificação:
✓ Velocidade EXCELENTE para praticamente qualquer atividade

============================================================
✓ Resultados salvos em 'resultado_velocidade.txt'
```

---

**Criado em:** Março de 2026  
**Licença:** MIT
