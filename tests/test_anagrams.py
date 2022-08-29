from time import sleep

import big_o
from challenges.challenge_anagrams import is_anagram

from tests.complexities import (
    NOTAÇÕES,
    DadosDeInferênciaDeComplexidade,
    inferir_complexidade,
    medir_tempos_de_execução,
)
from tests.geradores import gerar_anagramas


class RequirementViolated(Exception):
    pass


def valida_se_nao_foi_usado_sort_padrao():
    with open("challenges/challenge_anagrams.py", "r") as python_file:
        source = python_file.read()
        if "sorted(" in source or ".sort(" in source or "Counter(" in source:
            raise RequirementViolated(
                "Você deve fazer sua própria implementação "
                "do algoritmo de ordenação!"
            )
        if "import" in source:
            raise RequirementViolated(
                "Você não pode importar nada no challenge_anagrams.py!"
            )


def test_validar_se_as_palavras_nao_sao_um_anagrama():
    valida_se_nao_foi_usado_sort_padrao()

    first_string = "pedra"
    second_string = "perdaaa"
    assert is_anagram(first_string, second_string) is False

    first_string = "pedrra"
    second_string = "pedraa"
    assert is_anagram(first_string, second_string) is False

    first_string = "pedra"
    second_string = "pedro"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_as_palavras_sao_um_anagrama():
    valida_se_nao_foi_usado_sort_padrao()
    test_validar_se_as_palavras_nao_sao_um_anagrama()

    first_string = "pedra"
    second_string = "perda"
    assert is_anagram(first_string, second_string) is True


def test_valida_palavra_em_branco_retorna_false():
    valida_se_nao_foi_usado_sort_padrao()

    first_string = ""
    second_string = "perda"
    assert is_anagram(first_string, second_string) is False

    first_string = "perda"
    second_string = ""
    assert is_anagram(first_string, second_string) is False


def test_validar_tempo_anagrama():
    assert (
        _algoritmo_está_correto()
    ), "O algoritmo precisa estar correto para passar na validação de tempo"

    maior_complexidade_aceitável = big_o.complexities.Linearithmic

    # ! Tenta fazer o teste passar 3 vezes antes de confirmar que deu ruim
    for _ in range(3):
        dados = DadosDeInferênciaDeComplexidade(
            função_analisada=lambda tupla_de_str: is_anagram(*tupla_de_str),
            função_de_geração=gerar_anagramas,
            # * Valores obtidos de forma empírica, por meio de testes robustos
            ordens_de_grandeza=6,
            ordem_inicial=3,
            base_de_grandeza=2,
            quantidade_de_execuções=243,
            vezes_a_repetir=9,
        )

        resultados = medir_tempos_de_execução(dados)
        complexidade_observada = inferir_complexidade(
            resultados.tamanhos, resultados.tempos
        )

        if complexidade_observada <= maior_complexidade_aceitável:
            break
        sleep(3)
    else:
        assert False, (
            "Seu algoritmo parece ser "
            f"{NOTAÇÕES[complexidade_observada.__class__]}, mas"  # type:ignore
            f" deveria ser no máximo {NOTAÇÕES[maior_complexidade_aceitável]}"
        )


def test_validar_se_as_palavras_sao_um_anagrama_case_insensitive():
    valida_se_nao_foi_usado_sort_padrao()
    test_validar_se_as_palavras_nao_sao_um_anagrama()

    first_string = "PEDRA"
    second_string = "Perda"
    assert is_anagram(first_string, second_string) is True

    first_string = "AmoR"
    second_string = "Roma"
    assert is_anagram(first_string, second_string) is True


def _algoritmo_está_correto():
    """Valida se o algoritmo está correto

    Roda as funções de teste que garantem que o algoritmo da função está
    correto

    Serve como uma função auxiliar para o cálculo de tempo, que necessita
    validar que o algoritmo está correto antes de validar o tempo de execução

    Returns
    -------
    bool
        True se todas as funções de teste passarem, False caso contrário
    """
    try:
        test_validar_se_as_palavras_nao_sao_um_anagrama()
        test_validar_se_as_palavras_sao_um_anagrama()
        test_valida_palavra_em_branco_retorna_false()
        test_validar_se_as_palavras_sao_um_anagrama_case_insensitive()
        first_string = (
            "Lorem ipsum dolor sit amet, consectetur "
            "adipiscing elit, do sed eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua."
        )

        second_string = (
            "incididunt ut labore et dolore magna aliqua."
            "adipiscing elit, do sed eiusmod tempor "
            "Lorem ipsum dolor sit amet, consectetur "
        )
        algorithms_correct = is_anagram(first_string, second_string) is True
        assert algorithms_correct
    except AssertionError:
        return False
    return True
