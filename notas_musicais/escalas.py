NOTAS = "C C# D D# E F F# G G# A A# B".split()
ESCALAS = {"maior": (0, 2, 4, 5, 7, 9, 11), "menor": (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict:
    """
    Gera uma escala a partir de uma tônica e de uma tonalidade.

    Args:
        tonica (str): Nota que será a tônica da escala.
        tonalidade (str): Tonalidade da escala (por exemplo, 'maior', 'menor').

    Returns:
        dict: Um dicionário contendo as notas e os graus da escala.

    Raises:
        ValueError : Caso a tônica não seja uma nota válida.
        KeyError: Caso a escala não exista ou não foi implementada.

    Examples:
        >>> escala("C", "maior")
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala("a", "maior")
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f"Essa nota não existe, tente uma dessas: {NOTAS}")
    except KeyError:
        raise KeyError(
            f"Essa escala não existe ou nao foi implementada, tente uma dessas: {list(ESCALAS.keys())}"
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {"notas": temp, "graus": ["I", "II", "III", "IV", "V", "VI", "VII"]}
