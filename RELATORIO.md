# Relatório de validação — PT-BR 1.0

## Resultado instalado

Tradução aplicada na instalação local e limpeza seletiva concluída. O repositório contém apenas o patch e as ferramentas.

- 751 entradas do diretório PFF conferidas.
- 12 recursos RTXT ativos; 2.219 campos catalogados.
- 1.836 campos alterados em relação ao PFF original.
- 33 avisos/erros selecionados do executável traduzidos.
- 51 temporários do projeto arquivados, verificados por hash e removidos da pasta do jogo.

## Integridade

Todos os bytes fora dos campos de texto RTXT foram restaurados ao original de referência e conferidos. Isso também reparou duas alterações antigas indevidas em bytes de referências de modelos no recurso c34m3.orf. Cabeçalhos, diretório, chaves de recursos, gráficos, modelos e áudio foram preservados. Cópias não referenciadas no diretório foram preservadas como no original e não contadas como textos ativos.

O PFF mantém 113.493.525 bytes. Nenhuma posição NUL difere do original. Foram reparados excessos antigos em NEW CAMPAIGN e OVERVIEW. Os prefixos de condições removidos em etapas antigas foram restaurados. Cada campo foi conferido quanto a ASCII, capacidade, NUL e sequência de `<CR>`, `(CV ...)`, `~n` e formatos de substituição.

No executável, as mudanças estão restritas aos intervalos de mensagens selecionadas, com comprimento e formatos preservados. Imports, nomes técnicos e código fora desses intervalos não fazem parte do delta.

## Testes

Passaram: aplicação sobre o PFF original; aplicação sobre a tradução recente; conferência dos hashes finais; reaplicação sem mudança; restauração com hashes originais; limpeza dos 51 temporários em cópia; preservação de arquivos desconhecidos; recusa de base corrompida sem alterar nenhum dos arquivos.

Depois disso, aplicação e limpeza foram executadas na instalação local, e os hashes foram conferidos novamente. Backups do PFF e executável anteriores e dos temporários estão em `.ptbr_backups` dentro da pasta do jogo. Backups antigos foram mantidos.

## Hashes finais SHA-256

- `Raptor.pff`: `d1ad80e75c0cfe8f2897a286da32acdc2042e30909a8d8da69600e76a1865c0c`
- `Raptor.exe`: `0d2eca849844a77fd19adbaff55fce3878b6de7ddc2ccc2442872684d57fb970`

## Validação visual

O usuário abriu o jogo manualmente após o Windows exigir elevação (erro 740). O menu principal foi capturado e inspecionado: tradução carregada, sem acentos e sem recorte observado. A janela elevada não respondeu aos cliques/teclado da automação, impedindo avançar ao briefing e ao voo sem navegação manual. Esses testes continuam pendentes; não se afirma que todos os ramos de campanha foram jogados. Veja PENDENCIAS.md.
