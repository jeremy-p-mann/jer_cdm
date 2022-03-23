import pytest

from jer_cdm.concepts import Concept, MeasurementConcept, UnitConcept


@pytest.fixture(params=Concept.get_all_concepts())
def concept(request):
    return request.param


@pytest.fixture(params=[c for c in UnitConcept])
def unit_concept(request):
    return request.param


def test_units_are_units(ontology, unit_concept):
    domain_id = ontology.get_domain_id(unit_concept)
    assert domain_id == UnitConcept.get_domain_id()


def test_get_concept_from_id(ontology, concept):
    assert concept == ontology.get_concept_from_id(concept.value)


def test_get_concept_id_from_name(ontology, concept):
    concept = ontology.get_concept_from_id(concept.value)
    expected = ontology.get_concept_name(concept)
    assert expected == ontology.get_concept_name_from_id(concept.value)


def test_concept_name_matches_enum_name(concept, ontology):
    concept_name = ontology.get_concept_name(concept)
    if ' ' in concept_name:
        actual_terms = {
            term.lower() for term in concept_name.split(' ')
        }
        expected_terms = {term.lower() for term in concept.name.split('_')}
        assert actual_terms.issubset(expected_terms) \
            or expected_terms.issubset(actual_terms)
    else:
        assert concept_name.lower() == concept.name.lower()


def test_measurement_concepts_have_units(
        measurement_concept, ontology):
    assert isinstance(ontology.get_unit(measurement_concept), UnitConcept)
