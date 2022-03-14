# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-14T16:13:47
# Schema: ConfIDent-schema
#
# id: https://github.com/StroemPhi/ConfIDent-schema/
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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CONFID = CurieNamespace('confid', 'https://github.com/StroemPhi/ConfIDent-schema/')
DBLP_SERIES = CurieNamespace('dblp_series', 'https://dblp.org/db/conf/')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EX = CurieNamespace('ex', 'https://example.com/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
PROVO = CurieNamespace('provo', 'https://www.w3.org/TR/2013/REC-prov-o-20130430/#')
ROR = CurieNamespace('ror', 'https://ror.org/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WIKIDATA = CurieNamespace('wikidata', 'https://www.wikidata.org/wiki/')
DEFAULT_ = CONFID


# Types

# Class references
class PlannedProcessId(URIorCURIE):
    pass


class AcademicEventSeriesId(PlannedProcessId):
    pass


class AcademicEventId(PlannedProcessId):
    pass


class ProcessNameId(URIorCURIE):
    pass


class IdentifierId(URIorCURIE):
    pass


class EventFormatSpecificationId(URIorCURIE):
    pass


class CityId(URIorCURIE):
    pass


class CountryId(URIorCURIE):
    pass


class RegionId(URIorCURIE):
    pass


class VenueId(URIorCURIE):
    pass


class ContributorId(URIorCURIE):
    pass


class SponsorId(ContributorId):
    pass


class AttendeeId(ContributorId):
    pass


class ModeratorId(ContributorId):
    pass


class ReviewerId(ContributorId):
    pass


class OrganizerId(ContributorId):
    pass


class ContactPersonId(OrganizerId):
    pass


class CommitteeMemberId(OrganizerId):
    pass


class CommitteeChairId(CommitteeMemberId):
    pass


class PresenterId(ContributorId):
    pass


class KeynoteSpeakerId(PresenterId):
    pass


@dataclass
class SchemaBasedValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.SchemaBasedValue
    class_class_curie: ClassVar[str] = "confid:SchemaBasedValue"
    class_name: ClassVar[str] = "SchemaBasedValue"
    class_model_uri: ClassVar[URIRef] = CONFID.SchemaBasedValue

    scheme_name: str = None
    value: Optional[str] = None
    scheme_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.scheme_name):
            self.MissingRequiredField("scheme_name")
        if not isinstance(self.scheme_name, str):
            self.scheme_name = str(self.scheme_name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.scheme_uri is not None and not isinstance(self.scheme_uri, URIorCURIE):
            self.scheme_uri = URIorCURIE(self.scheme_uri)

        super().__post_init__(**kwargs)


@dataclass
class CommonMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.CommonMetadata
    class_class_curie: ClassVar[str] = "confid:CommonMetadata"
    class_name: ClassVar[str] = "CommonMetadata"
    class_model_uri: ClassVar[URIRef] = CONFID.CommonMetadata

    website: Optional[Union[str, URI]] = None
    logo: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "obi:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CONFID.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    denoted_by: Union[dict, "ProcessName"] = None
    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    landing_page: Optional[Union[str, URIorCURIE]] = None
    alternative_ids: Optional[Union[Dict[Union[str, IdentifierId], Union[dict, "Identifier"]], List[Union[dict, "Identifier"]]]] = empty_dict()
    contact: Optional[Union[dict, "ContactPerson"]] = None
    sponsors: Optional[Union[Dict[Union[str, SponsorId], Union[dict, "Sponsor"]], List[Union[dict, "Sponsor"]]]] = empty_dict()
    outputs: Optional[Union[str, List[str]]] = empty_list()
    topics: Optional[Union[str, List[str]]] = empty_list()
    academic_fields: Optional[Union[Union[dict, "AcademicField"], List[Union[dict, "AcademicField"]]]] = empty_list()
    metrics: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    logo: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self._is_empty(self.denoted_by):
            self.MissingRequiredField("denoted_by")
        if not isinstance(self.denoted_by, ProcessName):
            self.denoted_by = ProcessName(**as_dict(self.denoted_by))

        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self._is_empty(self.end_date):
            self.MissingRequiredField("end_date")
        if not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if self._is_empty(self.organizers):
            self.MissingRequiredField("organizers")
        self._normalize_inlined_as_list(slot_name="organizers", slot_type=Organizer, key_name="id", keyed=True)

        if self.landing_page is not None and not isinstance(self.landing_page, URIorCURIE):
            self.landing_page = URIorCURIE(self.landing_page)

        self._normalize_inlined_as_list(slot_name="alternative_ids", slot_type=Identifier, key_name="id", keyed=True)

        if self.contact is not None and not isinstance(self.contact, ContactPerson):
            self.contact = ContactPerson(**as_dict(self.contact))

        self._normalize_inlined_as_list(slot_name="sponsors", slot_type=Sponsor, key_name="id", keyed=True)

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, str) else str(v) for v in self.outputs]

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.academic_fields, list):
            self.academic_fields = [self.academic_fields] if self.academic_fields is not None else []
        self.academic_fields = [v if isinstance(v, AcademicField) else AcademicField(**as_dict(v)) for v in self.academic_fields]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.metrics]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

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
    denoted_by: Union[dict, "ProcessName"] = None
    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    series_of: Optional[Union[Dict[Union[str, AcademicEventId], Union[dict, "AcademicEvent"]], List[Union[dict, "AcademicEvent"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventSeriesId):
            self.id = AcademicEventSeriesId(self.id)

        self._normalize_inlined_as_list(slot_name="series_of", slot_type=AcademicEvent, key_name="id", keyed=True)

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
    denoted_by: Union[dict, "ProcessName"] = None
    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    event_status: Union[str, "EventStatus"] = None
    event_format: Optional[Union[dict, "EventFormatSpecification"]] = None
    multiple_days: Optional[Union[bool, Bool]] = None
    event_mode: Optional[Union[str, "EventMode"]] = None
    at_location: Optional[Union[dict, "Location"]] = None
    in_series: Optional[Union[str, AcademicEventSeriesId]] = None
    ordinal: Optional[int] = None
    deadlines: Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]] = empty_list()
    related_to: Optional[Union[Union[dict, "ProcessRelation"], List[Union[dict, "ProcessRelation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self._is_empty(self.event_status):
            self.MissingRequiredField("event_status")
        if not isinstance(self.event_status, EventStatus):
            self.event_status = EventStatus(self.event_status)

        if self.event_format is not None and not isinstance(self.event_format, EventFormatSpecification):
            self.event_format = EventFormatSpecification(**as_dict(self.event_format))

        if self.multiple_days is not None and not isinstance(self.multiple_days, Bool):
            self.multiple_days = Bool(self.multiple_days)

        if self.event_mode is not None and not isinstance(self.event_mode, EventMode):
            self.event_mode = EventMode(self.event_mode)

        if self.at_location is not None and not isinstance(self.at_location, Location):
            self.at_location = Location(**as_dict(self.at_location))

        if self.in_series is not None and not isinstance(self.in_series, AcademicEventSeriesId):
            self.in_series = AcademicEventSeriesId(self.in_series)

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if not isinstance(self.deadlines, list):
            self.deadlines = [self.deadlines] if self.deadlines is not None else []
        self.deadlines = [v if isinstance(v, Deadline) else Deadline(**as_dict(v)) for v in self.deadlines]

        self._normalize_inlined_as_dict(slot_name="related_to", slot_type=ProcessRelation, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ProcessName(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000090"]
    class_class_curie: ClassVar[str] = "aeon:0000090"
    class_name: ClassVar[str] = "ProcessName"
    class_model_uri: ClassVar[URIRef] = CONFID.ProcessName

    official_name: str = None
    id: Union[str, ProcessNameId] = EX.ProcessName
    name: Optional[str] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()
    acronym: Optional[str] = None
    former_name: Optional[str] = None
    translated_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessNameId):
            self.id = ProcessNameId(self.id)

        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.former_name is not None and not isinstance(self.former_name, str):
            self.former_name = str(self.former_name)

        if self.translated_name is not None and not isinstance(self.translated_name, str):
            self.translated_name = str(self.translated_name)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Identifier
    class_class_curie: ClassVar[str] = "confid:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CONFID.Identifier

    id: Union[str, IdentifierId] = None
    scheme_name: str = None
    value: Optional[str] = None
    scheme_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifierId):
            self.id = IdentifierId(self.id)

        if self._is_empty(self.scheme_name):
            self.MissingRequiredField("scheme_name")
        if not isinstance(self.scheme_name, str):
            self.scheme_name = str(self.scheme_name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.scheme_uri is not None and not isinstance(self.scheme_uri, URIorCURIE):
            self.scheme_uri = URIorCURIE(self.scheme_uri)

        super().__post_init__(**kwargs)


@dataclass
class EventFormatSpecification(YAMLRoot):
    """
    An academic event format specification is a plan specification that classifies a planned gathering of people in an
    academic context according to some sociocultural format, which provides implicit and explicit details on how this
    gathing is to be carried out by its participants in terms of achieving certain objectives, fulfiling certain
    conditions and performing certain actions. It thus concretizes the expectations of the contributers of an academic
    event. While the explicit details are often provied as concrete parts (e.g. deadline or attendance fee
    specifications), the implicit details depend on the semantics encoded in the words used for the classification of
    academic events (e.g. "conference" or "workshop"). Depending on the sociocultural background these classifications
    can overlap or vary to a certain degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON["0000004"]
    class_class_curie: ClassVar[str] = "aeon:0000004"
    class_name: ClassVar[str] = "EventFormatSpecification"
    class_model_uri: ClassVar[URIRef] = CONFID.EventFormatSpecification

    specified_as: Union[str, "EventFormat"] = None
    id: Union[str, EventFormatSpecificationId] = EX.EventType
    other: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventFormatSpecificationId):
            self.id = EventFormatSpecificationId(self.id)

        if self._is_empty(self.specified_as):
            self.MissingRequiredField("specified_as")
        if not isinstance(self.specified_as, EventFormat):
            self.specified_as = EventFormat(self.specified_as)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        super().__post_init__(**kwargs)


@dataclass
class Deadline(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Deadline
    class_class_curie: ClassVar[str] = "confid:Deadline"
    class_name: ClassVar[str] = "Deadline"
    class_model_uri: ClassVar[URIRef] = CONFID.Deadline

    deadline_date: Union[str, XSDDateTime] = None
    type: Union[str, "DeadlineType"] = None
    deadline_other: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.deadline_date):
            self.MissingRequiredField("deadline_date")
        if not isinstance(self.deadline_date, XSDDateTime):
            self.deadline_date = XSDDateTime(self.deadline_date)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, DeadlineType):
            self.type = DeadlineType(self.type)

        if self.deadline_other is not None and not isinstance(self.deadline_other, str):
            self.deadline_other = str(self.deadline_other)

        super().__post_init__(**kwargs)


@dataclass
class Metric(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Metric
    class_class_curie: ClassVar[str] = "confid:Metric"
    class_name: ClassVar[str] = "Metric"
    class_model_uri: ClassVar[URIRef] = CONFID.Metric

    type: Union[str, "MetricType"] = None
    int_value: Optional[int] = None
    str_value: Optional[str] = None
    rate_value: Optional[float] = None
    truth_value: Optional[Union[bool, Bool]] = None
    other_metric: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, MetricType):
            self.type = MetricType(self.type)

        if self.int_value is not None and not isinstance(self.int_value, int):
            self.int_value = int(self.int_value)

        if self.str_value is not None and not isinstance(self.str_value, str):
            self.str_value = str(self.str_value)

        if self.rate_value is not None and not isinstance(self.rate_value, float):
            self.rate_value = float(self.rate_value)

        if self.truth_value is not None and not isinstance(self.truth_value, Bool):
            self.truth_value = Bool(self.truth_value)

        if self.other_metric is not None and not isinstance(self.other_metric, str):
            self.other_metric = str(self.other_metric)

        super().__post_init__(**kwargs)


@dataclass
class ProcessRelation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.ProcessRelation
    class_class_curie: ClassVar[str] = "confid:ProcessRelation"
    class_name: ClassVar[str] = "ProcessRelation"
    class_model_uri: ClassVar[URIRef] = CONFID.ProcessRelation

    type: Union[str, "RelationType"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, RelationType):
            self.type = RelationType(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Location(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Location
    class_class_curie: ClassVar[str] = "confid:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = CONFID.Location

    city: Optional[Union[str, CityId]] = None
    country: Optional[Union[str, CountryId]] = None
    region: Optional[Union[str, RegionId]] = None
    venue: Optional[Union[str, VenueId]] = None
    lattitude: Optional[float] = None
    longitude: Optional[float] = None
    meeting_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.city is not None and not isinstance(self.city, CityId):
            self.city = CityId(self.city)

        if self.country is not None and not isinstance(self.country, CountryId):
            self.country = CountryId(self.country)

        if self.region is not None and not isinstance(self.region, RegionId):
            self.region = RegionId(self.region)

        if self.venue is not None and not isinstance(self.venue, VenueId):
            self.venue = VenueId(self.venue)

        if self.lattitude is not None and not isinstance(self.lattitude, float):
            self.lattitude = float(self.lattitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.meeting_url is not None and not isinstance(self.meeting_url, URIorCURIE):
            self.meeting_url = URIorCURIE(self.meeting_url)

        super().__post_init__(**kwargs)


@dataclass
class City(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.City
    class_class_curie: ClassVar[str] = "confid:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = CONFID.City

    id: Union[str, CityId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Country(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Country
    class_class_curie: ClassVar[str] = "confid:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = CONFID.Country

    id: Union[str, CountryId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Region(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Region
    class_class_curie: ClassVar[str] = "confid:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = CONFID.Region

    id: Union[str, RegionId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionId):
            self.id = RegionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Venue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Venue
    class_class_curie: ClassVar[str] = "confid:Venue"
    class_name: ClassVar[str] = "Venue"
    class_model_uri: ClassVar[URIRef] = CONFID.Venue

    id: Union[str, VenueId] = None
    name: Optional[str] = None
    address: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VenueId):
            self.id = VenueId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        super().__post_init__(**kwargs)


@dataclass
class AcademicField(YAMLRoot):
    """
    An academic field is the scientific subject of the planned process according to some controlled vocabulary or
    thesaurus and as such requires the scheme URI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.AcademicField
    class_class_curie: ClassVar[str] = "confid:AcademicField"
    class_name: ClassVar[str] = "AcademicField"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicField

    scheme_name: str = None
    value: Optional[str] = None
    scheme_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.scheme_name):
            self.MissingRequiredField("scheme_name")
        if not isinstance(self.scheme_name, str):
            self.scheme_name = str(self.scheme_name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.scheme_uri is not None and not isinstance(self.scheme_uri, URIorCURIE):
            self.scheme_uri = URIorCURIE(self.scheme_uri)

        super().__post_init__(**kwargs)


@dataclass
class Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Contributor
    class_class_curie: ClassVar[str] = "confid:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = CONFID.Contributor

    id: Union[str, ContributorId] = None
    name: Optional[str] = None
    identifier: Optional[Union[dict, Identifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorId):
            self.id = ContributorId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, Identifier):
            self.identifier = Identifier(**as_dict(self.identifier))

        super().__post_init__(**kwargs)


@dataclass
class Sponsor(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Sponsor
    class_class_curie: ClassVar[str] = "confid:Sponsor"
    class_name: ClassVar[str] = "Sponsor"
    class_model_uri: ClassVar[URIRef] = CONFID.Sponsor

    id: Union[str, SponsorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SponsorId):
            self.id = SponsorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Attendee(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Attendee
    class_class_curie: ClassVar[str] = "confid:Attendee"
    class_name: ClassVar[str] = "Attendee"
    class_model_uri: ClassVar[URIRef] = CONFID.Attendee

    id: Union[str, AttendeeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttendeeId):
            self.id = AttendeeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Moderator(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Moderator
    class_class_curie: ClassVar[str] = "confid:Moderator"
    class_name: ClassVar[str] = "Moderator"
    class_model_uri: ClassVar[URIRef] = CONFID.Moderator

    id: Union[str, ModeratorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModeratorId):
            self.id = ModeratorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Reviewer(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Reviewer
    class_class_curie: ClassVar[str] = "confid:Reviewer"
    class_name: ClassVar[str] = "Reviewer"
    class_model_uri: ClassVar[URIRef] = CONFID.Reviewer

    id: Union[str, ReviewerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReviewerId):
            self.id = ReviewerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organizer(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Organizer
    class_class_curie: ClassVar[str] = "confid:Organizer"
    class_name: ClassVar[str] = "Organizer"
    class_model_uri: ClassVar[URIRef] = CONFID.Organizer

    id: Union[str, OrganizerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizerId):
            self.id = OrganizerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ContactPerson(Organizer):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.ContactPerson
    class_class_curie: ClassVar[str] = "confid:ContactPerson"
    class_name: ClassVar[str] = "ContactPerson"
    class_model_uri: ClassVar[URIRef] = CONFID.ContactPerson

    id: Union[str, ContactPersonId] = EX.ContactPerson
    email: Optional[str] = None
    telephone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContactPersonId):
            self.id = ContactPersonId(self.id)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.telephone is not None and not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        super().__post_init__(**kwargs)


@dataclass
class CommitteeMember(Organizer):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.CommitteeMember
    class_class_curie: ClassVar[str] = "confid:CommitteeMember"
    class_name: ClassVar[str] = "CommitteeMember"
    class_model_uri: ClassVar[URIRef] = CONFID.CommitteeMember

    id: Union[str, CommitteeMemberId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeMemberId):
            self.id = CommitteeMemberId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CommitteeChair(CommitteeMember):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.CommitteeChair
    class_class_curie: ClassVar[str] = "confid:CommitteeChair"
    class_name: ClassVar[str] = "CommitteeChair"
    class_model_uri: ClassVar[URIRef] = CONFID.CommitteeChair

    id: Union[str, CommitteeChairId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeChairId):
            self.id = CommitteeChairId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Presenter(Contributor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Presenter
    class_class_curie: ClassVar[str] = "confid:Presenter"
    class_name: ClassVar[str] = "Presenter"
    class_model_uri: ClassVar[URIRef] = CONFID.Presenter

    id: Union[str, PresenterId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PresenterId):
            self.id = PresenterId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KeynoteSpeaker(Presenter):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.KeynoteSpeaker
    class_class_curie: ClassVar[str] = "confid:KeynoteSpeaker"
    class_name: ClassVar[str] = "KeynoteSpeaker"
    class_model_uri: ClassVar[URIRef] = CONFID.KeynoteSpeaker

    id: Union[str, KeynoteSpeakerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeynoteSpeakerId):
            self.id = KeynoteSpeakerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ConfIDentRecords(YAMLRoot):
    """
    This is a container to be able to bundle academic event and series data in one data file (e.g. YAML or JSON).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.ConfIDentRecords
    class_class_curie: ClassVar[str] = "confid:ConfIDentRecords"
    class_name: ClassVar[str] = "ConfIDentRecords"
    class_model_uri: ClassVar[URIRef] = CONFID.ConfIDentRecords

    events: Optional[Union[Dict[Union[str, AcademicEventId], Union[dict, AcademicEvent]], List[Union[dict, AcademicEvent]]]] = empty_dict()
    series: Optional[Union[Dict[Union[str, AcademicEventSeriesId], Union[dict, AcademicEventSeries]], List[Union[dict, AcademicEventSeries]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="events", slot_type=AcademicEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="series", slot_type=AcademicEventSeries, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class EventFormat(EnumDefinitionImpl):
    """
    The permissible values defined in this enum class represent the most common minimal event format specifications.
    For event formats that are not in this list, you can use "other" and provide the label of this other event format
    as strind using [other_format](https://stroemphi.github.io/ConfIDent-schema/academicEvent__other_format/).
    """
    colloquium = PermissibleValue(text="colloquium",
                                           description="A colloquium is an academic meeting that usually lasts only a few hours and serves to discuss a specific topic. Colloquia are usually part of the academic exchange in everyday university life with only one speaker, but can also take place on special occasions (anniversaries, start or end of the lecture phase, etc.) and can have more than one speaker.")
    conference = PermissibleValue(text="conference",
                                           description="A conference is an academic event that lasts up to several days and serves as a forum for presentations on a specific topic or subject area. In addition to subject-specific conferences, there are also interdisciplinary conferences which allow both a broader focus and more specific questions on a particular (academic) problem. Conferences often have a highly formalized structure of parallel, clearly defined sessions with several short presentations and plenary sessions with invited (keynote) speakers who are considered multipliers in their (research) field. Ideally, the selection of the speakers and their contributions is subject to a review process.")
    congress = PermissibleValue(text="congress",
                                       description="A congress is a certain type of conference which is characterised by a larger number of participants (often several hundred) and is oftentimes organised jointly by large, established (e.g. specialised societies) and/or several institutions. Congresses have a broader thematic focus than simple conferences, take place in certain cycles, but can still target an exclusive group of participants (e.g. representatives of a single discipline).")
    session = PermissibleValue(text="session",
                                     description="A session is a clearly defined part of a academic event in which a small number of speakers (usually 2-5) focus on a specific topic. A session is usually formally accompanied by a session chair, who assumes the function of a moderator. ")
    talk = PermissibleValue(text="talk",
                               description="A talk is a central part of a larger academic event, at which a specific topic is being presented in a rather short way.")
    forum = PermissibleValue(text="forum",
                                 description="An academic event whose sociocultural format is determined in an academic event type specification that classifies the academic event as a forum.")
    hackathon = PermissibleValue(text="hackathon",
                                         description="A hackathon is a gathering of software developers with the goal to develop software collaboratively in a short timeframe.")
    seminar = PermissibleValue(text="seminar",
                                     description="A seminar can serve as a term for older conference series, but in current usage the term mainly describes a specific teaching format that serves to develop content and provides space for discussion. Participation from the audience is usually encouraged.")
    symposium = PermissibleValue(text="symposium",
                                         description="A symposium is a specific type of conference with a narrower thematic focus, with fewer participants and of shorter duration. The degree of structuring lies between a classic conference and a workshop, allows more discussion than the larger conference, but is usually more formalized than the workshop.")
    tutorial = PermissibleValue(text="tutorial",
                                       description="An academic event that has the function to educate the audience on a certain topic. A tutorial is often realized as an academic event talk or academic event session.")
    workshop = PermissibleValue(text="workshop",
                                       description="Workshops are smaller academic events that serve to exchange information on a specific topic or problem. They usually last one or two days and offer space for discussion and the development of content and solutions. Group work is often part of the event concept.")
    other = PermissibleValue(text="other",
                                 description="This value is to be used if the event format cannot be represented using one of the other permissible values defined in the [EventFormat](https://stroemphi.github.io/ConfIDent-schema/EventFormat/) enum. If this value is chosen the use of [other_format](https://stroemphi.github.io/ConfIDent-schema/academicEvent__other_format/) is mandatory. ")

    _defn = EnumDefinition(
        name="EventFormat",
        description="The permissible values defined in this enum class represent the most common minimal event format specifications. For event formats that are not in this list, you can use \"other\" and provide the label of this other event format as strind using [other_format](https://stroemphi.github.io/ConfIDent-schema/academicEvent__other_format/).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "poster session",
                PermissibleValue(text="poster session",
                                 description="A poster session is a session at which poster papers are presented.") )
        setattr(cls, "keynote speech",
                PermissibleValue(text="keynote speech",
                                 description="A keynote speech is a special talk that has the function to set the underlying tone and summarize the core message or most important revelation of the academic event at which it is given. ") )
        setattr(cls, "event track",
                PermissibleValue(text="event track",
                                 description="An academic event that, as a part of a larger academic event, has the function to group even smaller parts of the academic event, like sessions and talks, according to a shared theme or topic. It usually has dedicated chairs and program committees.") )

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
                                 description="Default: used to indicate that the event takes place as planned.") )

class EventMode(EnumDefinitionImpl):

    online = PermissibleValue(text="online",
                                   description="The event takes place in a virtual location.")
    hybrid = PermissibleValue(text="hybrid",
                                   description="The event takes place physically and virtually.")

    _defn = EnumDefinition(
        name="EventMode",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "on site",
                PermissibleValue(text="on site",
                                 description="The event takes place in a physical location.") )

class DeadlineType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DeadlineType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "submission deadline",
                PermissibleValue(text="submission deadline",
                                 meaning=AEON["0000067"]) )
        setattr(cls, "notification deadline",
                PermissibleValue(text="notification deadline",
                                 meaning=AEON["0000064"]) )
        setattr(cls, "abstract deadline",
                PermissibleValue(text="abstract deadline",
                                 meaning=AEON["0000061"]) )
        setattr(cls, "camera-ready deadline",
                PermissibleValue(text="camera-ready deadline",
                                 meaning=AEON["0000062"]) )
        setattr(cls, "demo deadline",
                PermissibleValue(text="demo deadline",
                                 meaning=AEON["0000063"]) )
        setattr(cls, "paper deadline",
                PermissibleValue(text="paper deadline",
                                 meaning=AEON["0000065"]) )
        setattr(cls, "poster deadline",
                PermissibleValue(text="poster deadline",
                                 meaning=AEON["0000066"]) )
        setattr(cls, "tutorial deadline",
                PermissibleValue(text="tutorial deadline",
                                 meaning=AEON["0000068"]) )
        setattr(cls, "workshop deadline",
                PermissibleValue(text="workshop deadline",
                                 meaning=AEON["0000069"]) )

class RelationType(EnumDefinitionImpl):

    isUmbrellaEventOf = PermissibleValue(text="isUmbrellaEventOf")
    hasUmbrellaEvent = PermissibleValue(text="hasUmbrellaEvent")
    isJointEventOf = PermissibleValue(text="isJointEventOf")
    isColocatedEventOf = PermissibleValue(text="isColocatedEventOf")
    isSubEventOf = PermissibleValue(text="isSubEventOf")
    hasSubEvent = PermissibleValue(text="hasSubEvent")

    _defn = EnumDefinition(
        name="RelationType",
    )

class MetricType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MetricType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "submitted papers",
                PermissibleValue(text="submitted papers") )
        setattr(cls, "accepted papers",
                PermissibleValue(text="accepted papers") )
        setattr(cls, "accepted short papers",
                PermissibleValue(text="accepted short papers") )
        setattr(cls, "number of attendees",
                PermissibleValue(text="number of attendees") )
        setattr(cls, "number of tracks",
                PermissibleValue(text="number of tracks") )
        setattr(cls, "has childcare options",
                PermissibleValue(text="has childcare options") )
        setattr(cls, "is accessible",
                PermissibleValue(text="is accessible",
                                 description="If true then accessible for people with impairments.") )

# Slots

