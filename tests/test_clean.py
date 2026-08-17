from drifting_minsky.pipelines.clean import is_valid_quantity


def test_positivas_son_validas():
    assert is_valid_quantity(3) is True


def test_negativas_no_son_validas():
    assert is_valid_quantity(-1) is False


def test_cero_no_es_valida():
    assert is_valid_quantity(0) is False


def test_nula_no_es_valida():
    assert is_valid_quantity(None) is False
