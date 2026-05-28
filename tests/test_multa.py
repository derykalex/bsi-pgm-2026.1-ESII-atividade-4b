from modelos.equipamento import Notebook
from modelos.equipamento import Projetor
from modelos.equipamento import Tablet


def test_calcular_multa_notebook():

    notebook = Notebook(
        1,
        "Dell",
        "notebook"
    )

    resultado = notebook.calcular_multa(3)

    assert resultado == 30.0


def test_calcular_multa_projetor():

    projetor = Projetor(
        2,
        "Epson",
        "projetor"
    )

    resultado = projetor.calcular_multa(2)

    assert resultado == 30.0


def test_calcular_multa_tablet():

    tablet = Tablet(
        3,
        "Samsung",
        "tablet"
    )

    resultado = tablet.calcular_multa(5)

    assert resultado == 40.0
