# RelatÃ³rio de validaÃ§Ã£o â€” PT-BR 1.0

## Resultado instalado

TraduÃ§Ã£o aplicada na instalaÃ§Ã£o local e limpeza seletiva concluÃ­da. O repositÃ³rio contÃ©m apenas o patch e as ferramentas.

- 751 entradas do diretÃ³rio PFF conferidas.
- 12 recursos RTXT ativos; 2.219 campos catalogados.
- 1.836 campos alterados em relaÃ§Ã£o ao PFF original.
- 33 avisos/erros selecionados do executÃ¡vel traduzidos.
- 51 temporÃ¡rios do projeto arquivados, verificados por hash e removidos da pasta do jogo.

## Integridade

Todos os bytes fora dos campos de texto RTXT foram restaurados ao original de referÃªncia e conferidos. Isso tambÃ©m reparou duas alteraÃ§Ãµes antigas indevidas em bytes de referÃªncias de modelos no recurso c34m3.orf. CabeÃ§alhos, diretÃ³rio, chaves de recursos, grÃ¡ficos, modelos e Ã¡udio foram preservados. CÃ³pias nÃ£o referenciadas no diretÃ³rio foram preservadas como no original e nÃ£o contadas como textos ativos.

O PFF mantÃ©m 113.493.525 bytes. Nenhuma posiÃ§Ã£o NUL difere do original. Foram reparados excessos antigos em NEW CAMPAIGN e OVERVIEW. Os prefixos de condiÃ§Ãµes removidos em etapas antigas foram restaurados. Cada campo foi conferido quanto a ASCII, capacidade, NUL e sequÃªncia de `<CR>`, `(CV ...)`, `~n` e formatos de substituiÃ§Ã£o.

No executÃ¡vel, as mudanÃ§as estÃ£o restritas aos intervalos de mensagens selecionadas, com comprimento e formatos preservados. Imports, nomes tÃ©cnicos e cÃ³digo fora desses intervalos nÃ£o fazem parte do delta.

## Testes

Passaram: aplicaÃ§Ã£o sobre o PFF original; aplicaÃ§Ã£o sobre a traduÃ§Ã£o recente; conferÃªncia dos hashes finais; reaplicaÃ§Ã£o sem mudanÃ§a; restauraÃ§Ã£o com hashes originais; limpeza dos 51 temporÃ¡rios em cÃ³pia; preservaÃ§Ã£o de arquivos desconhecidos; recusa de base corrompida sem alterar nenhum dos arquivos.

Depois disso, aplicaÃ§Ã£o e limpeza foram executadas na instalaÃ§Ã£o local, e os hashes foram conferidos novamente. Backups do PFF e executÃ¡vel anteriores e dos temporÃ¡rios estÃ£o em `.ptbr_backups` dentro da pasta do jogo. Backups antigos foram mantidos.

## Hashes finais SHA-256

- `Raptor.pff`: `d1ad80e75c0cfe8f2897a286da32acdc2042e30909a8d8da69600e76a1865c0c`
- `Raptor.exe`: `0d2eca849844a77fd19adbaff55fce3878b6de7ddc2ccc2442872684d57fb970`

## ValidaÃ§Ã£o visual

O usuÃ¡rio abriu o jogo manualmente apÃ³s o Windows exigir elevaÃ§Ã£o (erro 740). O menu principal foi capturado e inspecionado: traduÃ§Ã£o carregada, sem acentos e sem recorte observado. A janela elevada nÃ£o respondeu aos cliques/teclado da automaÃ§Ã£o, impedindo avanÃ§ar ao briefing e ao voo sem navegaÃ§Ã£o manual. Esses testes continuam pendentes; nÃ£o se afirma que todos os ramos de campanha foram jogados. Veja PENDENCIAS.md.
