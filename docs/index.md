![logo_do_projeto](assets/logo.png){ width="300" .center}

# Notas Musicais

## Como usar?

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
poetry run escalas F#
```

Resultado em:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Alteração na tonalidade da escala

Você pode alterar a tonalidade da escala também! Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `D#` maior:

````bash
poetry run escala D# menor

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
````

## Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmetro. Um exemplo do uso do `help` nos campos harmônicos:

````bash
poetry run escalas --help
                                                                       
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE] 
                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico           │
│                                 [default: c]                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico       │
│                                 [default: maior]                    │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────╯
````