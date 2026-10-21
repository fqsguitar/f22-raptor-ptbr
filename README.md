# F-22 Raptor — Tradução PT-BR 🇧🇷

Tradução para português brasileiro do clássico **F-22 Raptor (1997)**, desenvolvido pela **NovaLogic**.

Este projeto disponibiliza um **patch de tradução com instalador portátil para Windows**. Você não precisa instalar Python, configurar dependências nem editar arquivos manualmente.

> **Importante:** apenas os textos gravados dentro do jogo são escritos sem acentos e sem cedilha, por limitações de compatibilidade. Esta documentação utiliza português normal.


<img width="1680" height="1050" alt="Raptor Screenshot 2026 10 21 - 00 18 50 90" src="https://github.com/user-attachments/assets/e97c28d5-8fb2-4471-ba83-a9f5d6e69143" />

<img width="1680" height="1050" alt="Raptor Screenshot 2026 10 21 - 00 19 21 94" src="https://github.com/user-attachments/assets/052dcac4-ea32-4f39-b698-5b10c48700ed" />

<img width="1680" height="1050" alt="Raptor Screenshot 2026 10 21 - 00 19 30 34" src="https://github.com/user-attachments/assets/7945f4c3-1804-44ee-8134-adc42caf42c9" />

<img width="1680" height="1050" alt="Raptor Screenshot 2026 10 21 - 00 19 48 100" src="https://github.com/user-attachments/assets/ba3c1321-5e31-43bb-a25b-1772ed11abff" />

<img width="1680" height="1050" alt="Raptor Screenshot 2026 10 21 - 00 19 57 86" src="https://github.com/user-attachments/assets/bbabfadc-1391-4d06-b003-597c7277138e" />

## 📥 Download e instalação

**[⬇️ Baixar F-22 Raptor PT-BR v1.0 para Windows](https://github.com/fqsguitar/f22-raptor-ptbr/releases/download/v1.0.0/F22-Raptor-PTBR-Windows.zip)**

1. Tenha o **F-22 Raptor** instalado e **feche o jogo** antes de continuar.
2. Baixe o ZIP acima e extraia seu conteúdo.
3. Execute **`Instalar.cmd`**.
4. Quando solicitado, informe a **pasta onde o jogo está instalado**, por exemplo `G:\Jogos\F-22 Raptor`.
5. Aguarde a validação e aplicação. Pronto!

O pacote inclui o programa **`Traduzir_F22.exe`**, com tudo o que é necessário para aplicar a tradução. **Não é necessário instalar Python** nem ter conexão com a internet durante a aplicação.

### 🔐 Backup e segurança

- O instalador verifica a **integridade dos arquivos por SHA-256** antes de modificar o jogo.
- Cria backups verificados na pasta **`.ptbr_backups`**, dentro da instalação.
- **Recusa versões desconhecidas** para evitar alterações incompatíveis.
- Uma segunda execução identifica os arquivos já traduzidos.
- Há opções avançadas para simular, restaurar e limpar temporários de projeto de forma seletiva.

A tradução foi testada na aplicação a partir de uma instalação em inglês compatível, além do reconhecimento de uma instalação já traduzida. O comportamento em outras edições do jogo pode variar.

## 🎮 O que foi traduzido?

O patch v1.0 contempla textos de campanhas e missões, briefings, mensagens de rádio exibidas na tela, objetivos, menus, elementos do HUD, ajuda de controles e avisos selecionados do executável.

Na análise do arquivo `Raptor.pff`, foram catalogados **2.219 campos** em 12 tabelas RTXT ativas, com **1.836 campos modificados**. Nem todos os campos precisam de tradução: alguns contêm nomes próprios, siglas, números ou estão vazios.

**Limitação conhecida:** nem todos os briefings, situações de voo e ramificações das campanhas foram conferidos manualmente dentro do jogo. Consulte [PENDENCIAS.md](PENDENCIAS.md) para os pontos que ainda exigem revisão.

## 🛠️ Uso avançado (opcional)

Esta seção é destinada a desenvolvedores. Para instalar normalmente, **use o ZIP da seção de download**.

Com Python 3.8 ou superior e os arquivos do repositório:

```powershell
# Aplicar tradução
python aplicar.py "G:\Jogos\F-22 Raptor"

# Apenas validar, sem modificar arquivos
python aplicar.py "G:\Jogos\F-22 Raptor" --simular

# Restaurar arquivos anteriores à instalação
python aplicar.py "G:\Jogos\F-22 Raptor" --restaurar

# Limpeza seletiva de temporários identificados
python aplicar.py "G:\Jogos\F-22 Raptor" --limpar-temporarios
```

No pacote portátil, você também pode substituir `python aplicar.py` por `Traduzir_F22.exe` para usar essas opções.

A limpeza é opcional: remove apenas arquivos de projeto cujos nomes e hashes constam em `temporarios.json`, após arquivamento e verificação. Arquivos desconhecidos são preservados. A opção `--restaurar` restaura os arquivos do jogo, mas **não** reverte a limpeza de temporários, que permanecem no ZIP de backup.

### Detalhes técnicos

- O `Raptor.pff` analisado possui **113.493.525 bytes**.
- O patch suporta apenas as versões cujos **hashes exatos** estão catalogados em `patch.json`; nome e tamanho, sozinhos, não garantem compatibilidade.
- As substituições preservam tamanho, offsets e marcadores de controle necessários.
- `patch.json` contém os deltas e hashes para aplicação; `traducoes.json` documenta as traduções, offsets e capacidades.
- Veja [RELATORIO.md](RELATORIO.md) para o escopo técnico dos testes.

### 📦 Como o executável é gerado

O pacote Windows é compilado pelo [GitHub Actions](https://github.com/fqsguitar/f22-raptor-ptbr/actions/workflows/windows.yml) usando PyInstaller, que incorpora o interpretador e os dados do patch no executável. Isso elimina a necessidade de instalar Python no computador do jogador.

## 📜 Distribuição e direitos

Este repositório **não inclui o jogo original**, seu executável completo, `Raptor.pff` completo, saves ou bibliotecas originais. É necessário possuir uma instalação compatível.

A presença do jogo em sites de abandonware **não significa automaticamente que exista autorização para redistribuí-lo**.

A licença [MIT](LICENSE) se aplica às ferramentas originais deste projeto, não aos direitos sobre o jogo ou conteúdo de terceiros. Consulte [NOTICE.md](NOTICE.md).

---

**Projeto de tradução: Felipe Queiroz**  
Feito por fãs, para fãs dos clássicos de PC. 🛩️🇧🇷
