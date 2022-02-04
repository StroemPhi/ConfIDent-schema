# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-04T20:55:41
# Schema: ConfIDent-metadata-schema
#
# id: https://raw.githubusercontent.com/StroemPhi/ConfIDent_schema/main/model/schema/confident_schema.yaml
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
from linkml_runtime.linkml_model.types import Datetime, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
CONFID = CurieNamespace('confid', 'https://raw.githubusercontent.com/StroemPhi/ConfIDent_schema/main/model/schema/confident_schema.yaml')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = CONFID


# Types

# Class references
class PlannedProcessId(extended_str):
    pass


class AcademicEventId(PlannedProcessId):
    pass


class AcademicEventSeriesId(PlannedProcessId):
    pass


class PersonId(extended_str):
    pass


@dataclass
class PlannedProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.PlannedProcess
    class_class_curie: ClassVar[str] = "confid:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CONFID.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    official_name: str = None
    acronym: str = None
    alternative_name: str = None
    organizers: str = None
    landing_page: str = None
    social_links: Optional[str] = None
    logo: Optional[str] = None
    sponsors: Optional[str] = None
    contact: Optional[str] = None
    topics: Optional[str] = None
    subjects: Optional[str] = None
    summary: Optional[str] = None
    website: Optional[str] = None
    process_relations: Optional[str] = None
    outputs: Optional[str] = None
    metrics: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self._is_empty(self.acronym):
            self.MissingRequiredField("acronym")
        if not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self._is_empty(self.alternative_name):
            self.MissingRequiredField("alternative_name")
        if not isinstance(self.alternative_name, str):
            self.alternative_name = str(self.alternative_name)

        if self._is_empty(self.organizers):
            self.MissingRequiredField("organizers")
        if not isinstance(self.organizers, str):
            self.organizers = str(self.organizers)

        if self._is_empty(self.landing_page):
            self.MissingRequiredField("landing_page")
        if not isinstance(self.landing_page, str):
            self.landing_page = str(self.landing_page)

        if self.social_links is not None and not isinstance(self.social_links, str):
            self.social_links = str(self.social_links)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.sponsors is not None and not isinstance(self.sponsors, str):
            self.sponsors = str(self.sponsors)

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if self.topics is not None and not isinstance(self.topics, str):
            self.topics = str(self.topics)

        if self.subjects is not None and not isinstance(self.subjects, str):
            self.subjects = str(self.subjects)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if self.process_relations is not None and not isinstance(self.process_relations, str):
            self.process_relations = str(self.process_relations)

        if self.outputs is not None and not isinstance(self.outputs, str):
            self.outputs = str(self.outputs)

        if self.metrics is not None and not isinstance(self.metrics, str):
            self.metrics = str(self.metrics)

        super().__post_init__(**kwargs)


@dataclass
class AcademicEvent(PlannedProcess):
    """
    An academic event is part of the established instruments of science communication as a format for conveying the
    latest scientific outputs. It is defined by the meeting of researchers at a specific time and place (virtual or
    physical) and with a specific thematic focus to present, hear and discuss these outputs. In contrast to other
    forms of events, academic events should primarily serve the exchange of results and methods of scientific research
    and their didactic mediation. Furthermore, a significant participation of scientific organizations in the
    realization of an academic event is constitutive for this type of event; for example, to distinguish it from
    events in which researchers mainly act as external experts or with a purely legitimising function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000001"]
    class_class_curie: ClassVar[str] = "aeon:0000001"
    class_name: ClassVar[str] = "AcademicEvent"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEvent

    id: Union[str, AcademicEventId] = None
    official_name: str = None
    acronym: str = None
    alternative_name: str = None
    organizers: str = None
    landing_page: str = None
    start_date: Union[str, XSDDateTime] = None
    previous_start_date: Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]] = None
    end_date: Union[str, XSDDateTime] = None
    previous_end_date: Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]] = None
    event_format: Optional[Union[str, "EventFormat"]] = None
    ordinal: Optional[str] = None
    event_status: Optional[Union[str, "EventStatus"]] = None
    deadline: Optional[str] = None
    location: Optional[str] = None
    fee: Optional[Union[str, List[str]]] = empty_list()
    committee: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self._is_empty(self.previous_start_date):
            self.MissingRequiredField("previous_start_date")
        if not isinstance(self.previous_start_date, list):
            self.previous_start_date = [self.previous_start_date] if self.previous_start_date is not None else []
        self.previous_start_date = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.previous_start_date]

        if self._is_empty(self.end_date):
            self.MissingRequiredField("end_date")
        if not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if self._is_empty(self.previous_end_date):
            self.MissingRequiredField("previous_end_date")
        if not isinstance(self.previous_end_date, list):
            self.previous_end_date = [self.previous_end_date] if self.previous_end_date is not None else []
        self.previous_end_date = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.previous_end_date]

        if self.event_format is not None and not isinstance(self.event_format, EventFormat):
            self.event_format = EventFormat(self.event_format)

        if self.ordinal is not None and not isinstance(self.ordinal, str):
            self.ordinal = str(self.ordinal)

        if self.event_status is not None and not isinstance(self.event_status, EventStatus):
            self.event_status = EventStatus(self.event_status)

        if self.deadline is not None and not isinstance(self.deadline, str):
            self.deadline = str(self.deadline)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if not isinstance(self.fee, list):
            self.fee = [self.fee] if self.fee is not None else []
        self.fee = [v if isinstance(v, str) else str(v) for v in self.fee]

        if not isinstance(self.committee, list):
            self.committee = [self.committee] if self.committee is not None else []
        self.committee = [v if isinstance(v, str) else str(v) for v in self.committee]

        super().__post_init__(**kwargs)


@dataclass
class AcademicEventSeries(PlannedProcess):
    """
    An academic event series describes the set of academic events which take place on a regular basis and thus have an
    established common identity. This identity is constituted, for example, through institutional continuity in the
    hosting of a series (e.g. by a specialised society), thematic focuses and/or a common label under which a series
    is defined (particularly name and acronym). Nevertheless, it is possible that each of these criteria may change
    over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000002"]
    class_class_curie: ClassVar[str] = "aeon:0000002"
    class_name: ClassVar[str] = "AcademicEventSeries"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEventSeries

    id: Union[str, AcademicEventSeriesId] = None
    official_name: str = None
    acronym: str = None
    alternative_name: str = None
    organizers: str = None
    landing_page: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventSeriesId):
            self.id = AcademicEventSeriesId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    """
    Minimal information about a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Person
    class_class_curie: ClassVar[str] = "sdo:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = CONFID.Person

    id: Union[str, PersonId] = None
    first_name: Union[str, List[str]] = None
    last_name: str = None
    knows: Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.first_name):
            self.MissingRequiredField("first_name")
        if not isinstance(self.first_name, list):
            self.first_name = [self.first_name] if self.first_name is not None else []
        self.first_name = [v if isinstance(v, str) else str(v) for v in self.first_name]

        if self._is_empty(self.last_name):
            self.MissingRequiredField("last_name")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if not isinstance(self.knows, list):
            self.knows = [self.knows] if self.knows is not None else []
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


# Enumerations
class EventFormat(EnumDefinitionImpl):

    colloquium = PermissibleValue(text="colloquium",
                                           meaning=AEON["0010000"])
    conference = PermissibleValue(text="conference",
                                           meaning=AEON["0010001"])
    congress = PermissibleValue(text="congress",
                                       meaning=AEON["0010011"])
    forum = PermissibleValue(text="forum",
                                 meaning=AEON["0010002"])
    hackathon = PermissibleValue(text="hackathon",
                                         meaning=AEON["0010003"])
    seminar = PermissibleValue(text="seminar",
                                     meaning=AEON["0010004"])
    symposium = PermissibleValue(text="symposium",
                                         meaning=AEON["0010006"])
    tutorial = PermissibleValue(text="tutorial",
                                       meaning=AEON["0010009"])
    workshop = PermissibleValue(text="workshop",
                                       meaning=AEON["0010010"])

    _defn = EnumDefinition(
        name="EventFormat",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "event session",
                PermissibleValue(text="event session",
                                 meaning=AEON["0010000"]) )
        setattr(cls, "poster session",
                PermissibleValue(text="poster session",
                                 meaning=AEON["0010005"]) )
        setattr(cls, "event talk",
                PermissibleValue(text="event talk",
                                 meaning=AEON["0010012"]) )
        setattr(cls, "keynote speech",
                PermissibleValue(text="keynote speech",
                                 meaning=AEON["0010007"]) )
        setattr(cls, "event track",
                PermissibleValue(text="event track",
                                 meaning=AEON["0010008"]) )

class EventStatus(EnumDefinitionImpl):

    postponed = PermissibleValue(text="postponed")
    delayed = PermissibleValue(text="delayed")
    canceled = PermissibleValue(text="canceled")
    planned = PermissibleValue(text="planned")

    _defn = EnumDefinition(
        name="EventStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "as scheduled",
                PermissibleValue(text="as scheduled",
                                 description="This should be used as default to indicate that an academic event takes place as planned.") )

# Slots

