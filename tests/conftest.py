import pytest

from jer_cdm.concepts import Ontology, MeasurementConcept


@pytest.fixture(scope='session')
def ontology():
    return Ontology()


@pytest.fixture(params=[c for c in MeasurementConcept])
def measurement_concept(request):
    return request.param
