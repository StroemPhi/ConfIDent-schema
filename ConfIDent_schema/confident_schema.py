# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-13T14:49:33
# Schema: ConfIDent-schema
#
# id: https://raw.githubusercontent.com/StroemPhi/ConfIDent-schema/main/model/schema/confident-schema.yaml
# description: This is a schema for the ConfIDent project that describes the necessary metadata requirements of
#              academic events and event series.
# license: https://creativecommons.org/licenses/by/4.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
CONFID = CurieNamespace('confid', 'https://raw.githubusercontent.com/StroemPhi/ConfIDent_schema/main/model/schema/confident_schema.yaml')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROVO = CurieNamespace('provo', 'https://www.w3.org/TR/2013/REC-prov-o-20130430/#')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = CONFID


# Types

# Class references
class CommonMetadataId(extended_str):
    pass


class AcademicEventId(extended_str):
    pass


@dataclass
class CommonMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.CommonMetadata
    class_class_curie: ClassVar[str] = "confid:CommonMetadata"
    class_name: ClassVar[str] = "CommonMetadata"
    class_model_uri: ClassVar[URIRef] = CONFID.CommonMetadata

    id: Union[str, CommonMetadataId] = None
    name: str = None
    acronym: Optional[str] = None
    at_location: Optional[str] = None
    organizers: Optional[str] = None
    sponsors: Optional[str] = None
    contact: Optional[str] = None
    event_relation: Optional[str] = None
    output: Optional[str] = None
    topic: Optional[str] = None
    academic_field: Optional[str] = None
    website: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommonMetadataId):
            self.id = CommonMetadataId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.at_location is not None and not isinstance(self.at_location, str):
            self.at_location = str(self.at_location)

        if self.organizers is not None and not isinstance(self.organizers, str):
            self.organizers = str(self.organizers)

        if self.sponsors is not None and not isinstance(self.sponsors, str):
            self.sponsors = str(self.sponsors)

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if self.event_relation is not None and not isinstance(self.event_relation, str):
            self.event_relation = str(self.event_relation)

        if self.output is not None and not isinstance(self.output, str):
            self.output = str(self.output)

        if self.topic is not None and not isinstance(self.topic, str):
            self.topic = str(self.topic)

        if self.academic_field is not None and not isinstance(self.academic_field, str):
            self.academic_field = str(self.academic_field)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        super().__post_init__(**kwargs)


@dataclass
class AcademicEvent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.AcademicEvent
    class_class_curie: ClassVar[str] = "confid:AcademicEvent"
    class_name: ClassVar[str] = "AcademicEvent"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEvent

    id: Union[str, AcademicEventId] = None
    name: str = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    committees: Optional[str] = None
    participants: Optional[str] = None
    ordinal: Optional[str] = None
    logo: Optional[str] = None
    summary: Optional[str] = None
    metric: Optional[str] = None
    acronym: Optional[str] = None
    at_location: Optional[str] = None
    organizers: Optional[str] = None
    sponsors: Optional[str] = None
    contact: Optional[str] = None
    event_relation: Optional[str] = None
    output: Optional[str] = None
    topic: Optional[str] = None
    academic_field: Optional[str] = None
    website: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.start_date is not None and not isinstance(self.start_date, str):
            self.start_date = str(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, str):
            self.end_date = str(self.end_date)

        if self.committees is not None and not isinstance(self.committees, str):
            self.committees = str(self.committees)

        if self.participants is not None and not isinstance(self.participants, str):
            self.participants = str(self.participants)

        if self.ordinal is not None and not isinstance(self.ordinal, str):
            self.ordinal = str(self.ordinal)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.metric is not None and not isinstance(self.metric, str):
            self.metric = str(self.metric)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.at_location is not None and not isinstance(self.at_location, str):
            self.at_location = str(self.at_location)

        if self.organizers is not None and not isinstance(self.organizers, str):
            self.organizers = str(self.organizers)

        if self.sponsors is not None and not isinstance(self.sponsors, str):
            self.sponsors = str(self.sponsors)

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if self.event_relation is not None and not isinstance(self.event_relation, str):
            self.event_relation = str(self.event_relation)

        if self.output is not None and not isinstance(self.output, str):
            self.output = str(self.output)

        if self.topic is not None and not isinstance(self.topic, str):
            self.topic = str(self.topic)

        if self.academic_field is not None and not isinstance(self.academic_field, str):
            self.academic_field = str(self.academic_field)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

