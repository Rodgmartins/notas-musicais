from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = "c"
    tonalidade = "maior"

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_error_dizendo_nota_nao_existe():

    tonica = "X"
    tonalidade = "maior"

    mensagem_error = f"Essa nota não existe, tente uma dessas: {NOTAS}"

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_error == error.value.args[0]


def test_deve_retornar_um_error_dizendo_escala_nao_existe():
    tonica = "c"
    tonalidade = "tonalidade"

    mensagem_error = f"Essa escala não existe ou nao foi implementada, tente uma dessas: {list(ESCALAS.keys())}"

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_error == error.value.args[0]


@mark.parametrize(
    "tonica,tonalidade, esperado",
    [
        ("C", "maior", ["C", "D", "E", "F", "G", "A", "B"]),
        ("C#", "maior", ["C#", "D#", "F", "F#", "G#", "A#", "C"]),
        ("D", "maior", ["D", "E", "F#", "G", "A", "B", "C#"]),
        ("D#", "maior", ["D#", "F", "G", "G#", "A#", "C", "D"]),
        ("E", "maior", ["E", "F#", "G#", "A", "B", "C#", "D#"]),
        ("F", "maior", ["F", "G", "A", "A#", "C", "D", "E"]),
        ("F#", "maior", ["F#", "G#", "A#", "B", "C#", "D#", "F"]),
        ("G", "maior", ["G", "A", "B", "C", "D", "E", "F#"]),
        ("G#", "maior", ["G#", "A#", "C", "C#", "D#", "F", "G"]),
        ("A", "maior", ["A", "B", "C#", "D", "E", "F#", "G#"]),
        ("A#", "maior", ["A#", "C", "D", "D#", "F", "G", "A"]),
        ("B", "maior", ["B", "C#", "D#", "E", "F#", "G#", "A#"]),
        ("C", "menor", ["C", "D", "D#", "F", "G", "G#", "A#"]),
        ("C#", "menor", ["C#", "D#", "E", "F#", "G#", "A", "B"]),
        ("F", "menor", ["F", "G", "G#", "A#", "C", "C#", "D#"]),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado["notas"] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = "c"
    tonalidade = "maior"
    esperado = ["I", "II", "III", "IV", "V", "VI", "VII"]

    resultado = escala(tonica, tonalidade)

    assert resultado["graus"] == esperado
