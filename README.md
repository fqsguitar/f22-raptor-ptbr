# F-22 Raptor PT-BR

Patch de tradução de textos do NovaLogic F-22 Raptor para português do Brasil, sem acentos ou cedilha nos arquivos do jogo.

A versão 1.0 cobre os 2.219 campos identificados nas 12 tabelas RTXT ativas do PFF analisado: campanhas, briefings, rádio escrito, objetivos, menus, HUD e ajuda de teclas. Foram alterados 1.836 campos; os demais incluem nomes próprios, siglas, números, termos já usados em português e campos vazios. O patch também traduz avisos selecionados do executável.

## Instalação

1. Tenha sua própria instalação do jogo e Python 3.8 ou superior.
2. Feche o jogo. Extraia os arquivos deste projeto em uma pasta separada.
3. Abra `Instalar.cmd` e informe a pasta do jogo, ou execute:

```powershell
python aplicar.py "G:\Jogos\F-22 Raptor"
```

O instalador verifica os hashes antes de gravar, cria backups verificados em `.ptbr_backups` dentro da pasta do jogo e aplica somente as diferenças. Versões desconhecidas são recusadas. Uma segunda execução reconhece a instalação já traduzida.

Para apenas validar:

```powershell
python aplicar.py "G:\Jogos\F-22 Raptor" --simular
```

Para voltar aos arquivos existentes antes da instalação:

```powershell
python aplicar.py "G:\Jogos\F-22 Raptor" --restaurar
```

A restauração preserva os backups e recusa arquivos modificados depois do patch.

## Versões aceitas

O `Raptor.pff` tem 113.493.525 bytes. O patch aceita o original identificado neste projeto, a versão de tradução de 20/10/2026 às 23:01 e o primeiro patch incremental deste projeto. O executável é aceito apenas pelo hash exato em `patch.json`. O nome do arquivo e o tamanho sozinhos não bastam.

## Limpeza dos temporários antigos

```powershell
python aplicar.py "G:\Jogos\F-22 Raptor" --limpar-temporarios
```

A limpeza é opcional. Só remove os 51 nomes de projeto registrados em `temporarios.json`, e apenas se o conteúdo tiver o hash esperado. Todos são arquivados e conferidos antes de remover. Arquivos originais, configurações, saves, arquivos desconhecidos, arquivos alterados e backups anteriores são preservados. A limpeza não é revertida por `--restaurar`; os temporários permanecem recuperáveis no ZIP de backup.

## Limites e validação

Tamanho de arquivo, offsets, NUL, `<CR>`, condições `(CV ...)` e formatos de substituição são verificados. Gráficos, áudio, modelos, tabelas de recursos e nomes internos permanecem iguais ao original de referência. Textos longos usam redação compacta e campos curtos podem usar abreviações.

Os testes de aplicação, reaplicação, restauração, limpeza seletiva e recusa de base desconhecida passaram. Veja `RELATORIO.md` e `PENDENCIAS.md` para o alcance e os limites da validação visual.

`traducoes.json` contém apenas os campos alterados em português, com seus offsets, capacidades e recursos. `patch.json` contém os deltas e hashes, sem os arquivos completos do jogo.

## Distribuição

Este projeto não inclui o jogo, executável completo, PFF completo, saves ou bibliotecas. É necessário possuir uma instalação própria. A disponibilidade em sites de abandonware não demonstra licença livre; este projeto não afirma autorização para redistribuir o jogo.

A licença MIT em `LICENSE` se aplica às ferramentas originais deste repositório. Os direitos do jogo, marcas e conteúdo subjacente continuam com seus titulares. Consulte `NOTICE.md`.
