from modelos.equipamento import Notebook
from modelos.equipamento import Projetor
from modelos.equipamento import Tablet


def test_calcular_multa_notebook():
    notebook = Notebook(1, "Dell", "notebook")
    assert notebook.calcular_multa(3) == 30.0


def test_calcular_multa_projetor():
    projetor = Projetor(2, "Epson", "projetor")
    assert projetor.calcular_multa(2) == 30.0


def test_calcular_multa_tablet():
    tablet = Tablet(3, "Samsung", "tablet")
    assert tablet.calcular_multa(5) == 40.0


def test_multa_notebook_sem_atraso():
    notebook = Notebook(1, "Dell", "notebook")
    assert notebook.calcular_multa(0) == 0


def test_multa_projetor_sem_atraso():
    projetor = Projetor(2, "Epson", "projetor")
    assert projetor.calcular_multa(0) == 0


def test_multa_tablet_sem_atraso():
    tablet = Tablet(3, "Samsung", "tablet")
    assert tablet.calcular_multa(0) == 0


def test_multa_notebook_um_dia():
    notebook = Notebook(1, "Dell", "notebook")
    assert notebook.calcular_multa(1) > 0
