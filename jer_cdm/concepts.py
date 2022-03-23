from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from functools import cached_property
from typing import Dict, List, Tuple, Type

import pandas as pd
import pkg_resources


class Concept(IntEnum):
    @classmethod
    def get_all_concepts(cls) -> List[Concept]:
        concepts = []
        concepts += MeasurementConcept.get_concepts()
        concepts += UnitConcept.get_concepts()
        return concepts

    @classmethod
    def get_concepts(cls) -> List[Concept]:
        return [c for c in cls]


@dataclass
class Ontology():
    @cached_property
    def _concept_df(self,) -> pd.DataFrame:
        stream = pkg_resources.resource_stream(__name__, 'data/concept.csv')
        df = pd.read_csv(stream, sep='\t', index_col='concept_id')
        return df

    @cached_property
    def _concept_relationship_df(self,) -> pd.DataFrame:
        stream = pkg_resources.resource_stream(
            __name__, 'data/concept_relationship.csv')
        df = pd.read_csv(stream, sep='\t', index_col='concept_id_1')
        return df

    def is_valid(self, concept: Concept) -> bool:
        return concept.value in self._concept_df.index

    def get_concept_name(self, concept: Concept) -> str:
        assert self.is_valid(concept), 'concept not supported'
        return self._concept_df.loc[concept.value, 'concept_name']

    def get_concept_code(self, concept: Concept) -> str:
        assert self.is_valid(concept), 'concept not supported'
        return self._concept_df.loc[concept.value, 'concept_code']

    def get_standard_concept(self, concept: Concept) -> str:
        assert self.is_valid(concept), 'concept not supported'
        return self._concept_df.loc[concept.value, 'standard_concept']

    def get_concept_from_id(self, concept_id: int) -> Concept:
        all_concepts = Concept.get_all_concepts()
        concepts = [c for c in all_concepts if c.value == concept_id]
        assert len(concepts) == 1, f'no concept for id: {concept_id}'
        return concepts[0]

    def get_concept_name_from_id(self, concept_id) -> str:
        concept = self.get_concept_from_id(concept_id)
        return self.get_concept_name(concept)

    def maps_to(self, concept: Concept) -> Concept:
        maps_to_df = self._concept_relationship_df.loc[[concept.value], :]
        ans_ids = maps_to_df[maps_to_df.relationship_id ==
                             'Maps to'].concept_id_2
        assert len(ans_ids) == 1
        ans_id = ans_ids.iloc[0]
        return self.get_concept_from_id(ans_id)

    def mapped_from(self, concept: Concept) -> Concept:
        maps_to_df = self._concept_relationship_df.loc[[concept.value], :]
        ans_ids = maps_to_df[maps_to_df.relationship_id ==
                             'Mapped from'].concept_id_2
        assert len(ans_ids) == 1
        ans_id = ans_ids.iloc[0]
        return self.get_concept_from_id(ans_id)

    def get_unit(self, concept: Concept) -> Concept:
        maps_to_df = self._concept_relationship_df.loc[[concept.value], :]
        ans_ids = maps_to_df[maps_to_df.relationship_id ==
                             'Has unit'].concept_id_2
        assert len(ans_ids) == 1
        ans_id = ans_ids.iloc[0]
        return self.get_concept_from_id(ans_id)

    def get_domain_id(self, concept: Concept) -> str:
        assert self.is_valid(concept), 'concept not supported'
        return self._concept_df.loc[concept.value, 'domain_id']


class UnitConcept(Concept, IntEnum):
    POUND = 8739

    @classmethod
    def get_domain_id(cls,) -> str:
        return 'Unit'


class MeasurementConcept(Concept, IntEnum):
    BODY_WEIGHT = 4099154


class PhysicalConcept(Concept, IntEnum):
    DATETIME = 4041097
