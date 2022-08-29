from time import sleep

import big_o
from challenges.challenge_study_schedule import study_schedule

from tests.complexities import (
    NOTAÇÕES,
    DadosDeInferênciaDeComplexidade,
    inferir_complexidade,
    medir_tempos_de_execução,
)
from tests.geradores import gerar_cronogramas


def test_validar_melhor_horario_com_sucesso():
    permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    assert study_schedule(permanence_periods, 5) == 3
    assert study_schedule(permanence_periods, 4) == 3
    assert study_schedule(permanence_periods, 3) == 2
    assert study_schedule(permanence_periods, 2) == 4
    assert study_schedule(permanence_periods, 1) == 2


def test_validar_permanence_periods_com_entradas_invalidas():
    permanence_periods = [(4, None), ("0", 4)]
    target_time = 4
    assert study_schedule(permanence_periods, target_time) is None

    permanence_periods = [("A", 9), (None, 5)]
    target_time = 6
    assert study_schedule(permanence_periods, target_time) is None


def test_validar_target_time_com_vazio():
    permanence_periods = [(1, 5), (2, 4), (3, 3), (4, 4), (5, 5)]
    target_time = None
    assert study_schedule(permanence_periods, target_time) is None


def test_validar_tempo_schedule():
    assert (
        _algoritmo_está_correto()
    ), "O algoritmo precisa estar correto para passar na validação de tempo"

    maior_complexidade_aceitável = big_o.complexities.Linear

    # ! Tenta fazer o teste passar 3 vezes antes de confirmar que deu ruim
    for _ in range(3):
        dados = DadosDeInferênciaDeComplexidade(
            função_analisada=lambda valores: study_schedule(*valores),
            função_de_geração=gerar_cronogramas,
            # * Valores obtidos de forma empírica, por meio de testes robustos
            ordens_de_grandeza=5,
            ordem_inicial=3,
            base_de_grandeza=3,
            quantidade_de_execuções=6561,
            vezes_a_repetir=3,
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
        test_validar_melhor_horario_com_sucesso()
        test_validar_permanence_periods_com_entradas_invalidas()
        test_validar_target_time_com_vazio()
        permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
        algorithms_correct = study_schedule(permanence_periods, 5) == 3

        assert algorithms_correct
    except AssertionError:
        return False
    return True
