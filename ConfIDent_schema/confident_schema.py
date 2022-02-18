# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-18T13:27:20
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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#')
CONFID = CurieNamespace('confid', 'https://github.com/StroemPhi/ConfIDent-schema/')
DBLP_SERIES = CurieNamespace('dblp_series', 'https://dblp.org/db/conf/')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/OBI_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
PROVO = CurieNamespace('provo', 'https://www.w3.org/TR/2013/REC-prov-o-20130430/#')
ROR = CurieNamespace('ror', 'ror.org/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
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


class CityId(URIorCURIE):
    pass


class CountryId(URIorCURIE):
    pass


class RegionId(URIorCURIE):
    pass


class VenueId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class OrganisationId(URIorCURIE):
    pass


@dataclass
class ConfIDentRecord(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.ConfIDentRecord
    class_class_curie: ClassVar[str] = "confid:ConfIDentRecord"
    class_name: ClassVar[str] = "ConfIDentRecord"
    class_model_uri: ClassVar[URIRef] = CONFID.ConfIDentRecord

    events: Optional[Union[Dict[Union[str, AcademicEventId], Union[dict, "AcademicEvent"]], List[Union[dict, "AcademicEvent"]]]] = empty_dict()
    series: Optional[Union[Dict[Union[str, AcademicEventSeriesId], Union[dict, "AcademicEventSeries"]], List[Union[dict, "AcademicEventSeries"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="events", slot_type=AcademicEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="series", slot_type=AcademicEventSeries, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.PlannedProcess
    class_class_curie: ClassVar[str] = "confid:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CONFID.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    denoted_by: Union[dict, "ProcessName"] = None
    alternative_ids: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    start_date: Optional[Union[str, XSDDateTime]] = None
    end_date: Optional[Union[str, XSDDateTime]] = None
    organizers: Optional[Union[Union[dict, "Organizer"], List[Union[dict, "Organizer"]]]] = empty_list()
    sponsors: Optional[Union[str, List[str]]] = empty_list()
    outputs: Optional[Union[str, List[str]]] = empty_list()
    topics: Optional[Union[str, List[str]]] = empty_list()
    academic_fields: Optional[Union[str, List[str]]] = empty_list()
    metrics: Optional[Union[Union[dict, "Metric"], List[Union[dict, "Metric"]]]] = empty_list()
    contact: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    summary: Optional[str] = None
    in_series: Optional[str] = None
    series_of: Optional[str] = None
    related_to: Optional[Union[Union[dict, "ProcessRelation"], List[Union[dict, "ProcessRelation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self._is_empty(self.denoted_by):
            self.MissingRequiredField("denoted_by")
        if not isinstance(self.denoted_by, ProcessName):
            self.denoted_by = ProcessName(**as_dict(self.denoted_by))

        if not isinstance(self.alternative_ids, list):
            self.alternative_ids = [self.alternative_ids] if self.alternative_ids is not None else []
        self.alternative_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_ids]

        if self.start_date is not None and not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if not isinstance(self.organizers, list):
            self.organizers = [self.organizers] if self.organizers is not None else []
        self.organizers = [v if isinstance(v, Organizer) else Organizer(**as_dict(v)) for v in self.organizers]

        if not isinstance(self.sponsors, list):
            self.sponsors = [self.sponsors] if self.sponsors is not None else []
        self.sponsors = [v if isinstance(v, str) else str(v) for v in self.sponsors]

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, str) else str(v) for v in self.outputs]

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.academic_fields, list):
            self.academic_fields = [self.academic_fields] if self.academic_fields is not None else []
        self.academic_fields = [v if isinstance(v, str) else str(v) for v in self.academic_fields]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, Metric) else Metric(**as_dict(v)) for v in self.metrics]

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.in_series is not None and not isinstance(self.in_series, str):
            self.in_series = str(self.in_series)

        if self.series_of is not None and not isinstance(self.series_of, str):
            self.series_of = str(self.series_of)

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, ProcessRelation) else ProcessRelation(**as_dict(v)) for v in self.related_to]

        super().__post_init__(**kwargs)


@dataclass
class AcademicEventSeries(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON.AEON_0000002
    class_class_curie: ClassVar[str] = "aeon:AEON_0000002"
    class_name: ClassVar[str] = "AcademicEventSeries"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEventSeries

    id: Union[str, AcademicEventSeriesId] = None
    denoted_by: Union[dict, "ProcessName"] = None
    series_of: Optional[Union[str, AcademicEventId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventSeriesId):
            self.id = AcademicEventSeriesId(self.id)

        if self.series_of is not None and not isinstance(self.series_of, AcademicEventId):
            self.series_of = AcademicEventId(self.series_of)

        super().__post_init__(**kwargs)


@dataclass
class AcademicEvent(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON.AEON_0000001
    class_class_curie: ClassVar[str] = "aeon:AEON_0000001"
    class_name: ClassVar[str] = "AcademicEvent"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEvent

    id: Union[str, AcademicEventId] = None
    denoted_by: Union[dict, "ProcessName"] = None
    event_status: Union[str, "EventStatus"] = None
    start_date: Union[str, XSDDateTime] = None
    end_date: Union[str, XSDDateTime] = None
    event_mode: Optional[Union[str, "EventMode"]] = None
    at_location: Optional[Union[dict, "Location"]] = None
    ordinal: Optional[int] = None
    deadlines: Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]] = empty_list()
    type: Optional[Union[str, "EventType"]] = None
    in_series: Optional[Union[str, AcademicEventSeriesId]] = None
    organizers: Optional[Union[Union[dict, "Organizer"], List[Union[dict, "Organizer"]]]] = empty_list()
    sponsors: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self._is_empty(self.event_status):
            self.MissingRequiredField("event_status")
        if not isinstance(self.event_status, EventStatus):
            self.event_status = EventStatus(self.event_status)

        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self._is_empty(self.end_date):
            self.MissingRequiredField("end_date")
        if not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if self.event_mode is not None and not isinstance(self.event_mode, EventMode):
            self.event_mode = EventMode(self.event_mode)

        if self.at_location is not None and not isinstance(self.at_location, Location):
            self.at_location = Location(**as_dict(self.at_location))

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if not isinstance(self.deadlines, list):
            self.deadlines = [self.deadlines] if self.deadlines is not None else []
        self.deadlines = [v if isinstance(v, Deadline) else Deadline(**as_dict(v)) for v in self.deadlines]

        if self.type is not None and not isinstance(self.type, EventType):
            self.type = EventType(self.type)

        if self.in_series is not None and not isinstance(self.in_series, AcademicEventSeriesId):
            self.in_series = AcademicEventSeriesId(self.in_series)

        if not isinstance(self.organizers, list):
            self.organizers = [self.organizers] if self.organizers is not None else []
        self.organizers = [v if isinstance(v, Organizer) else Organizer(**as_dict(v)) for v in self.organizers]

        if not isinstance(self.sponsors, list):
            self.sponsors = [self.sponsors] if self.sponsors is not None else []
        self.sponsors = [v if isinstance(v, str) else str(v) for v in self.sponsors]

        super().__post_init__(**kwargs)


@dataclass
class ProcessName(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AEON.AEON_0000090
    class_class_curie: ClassVar[str] = "aeon:AEON_0000090"
    class_name: ClassVar[str] = "ProcessName"
    class_model_uri: ClassVar[URIRef] = CONFID.ProcessName

    official_name: str = None
    acronym: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.official_name):
            self.MissingRequiredField("official_name")
        if not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        super().__post_init__(**kwargs)


@dataclass
class Metric(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Metric
    class_class_curie: ClassVar[str] = "confid:Metric"
    class_name: ClassVar[str] = "Metric"
    class_model_uri: ClassVar[URIRef] = CONFID.Metric

    int_value: Optional[int] = None
    str_value: Optional[str] = None
    rate_value: Optional[float] = None
    truth_value: Optional[Union[bool, Bool]] = None
    other_metric: Optional[str] = None
    type: Optional[Union[str, "MetricType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.type is not None and not isinstance(self.type, MetricType):
            self.type = MetricType(self.type)

        super().__post_init__(**kwargs)


@dataclass
class ProcessRelation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.ProcessRelation
    class_class_curie: ClassVar[str] = "confid:ProcessRelation"
    class_name: ClassVar[str] = "ProcessRelation"
    class_model_uri: ClassVar[URIRef] = CONFID.ProcessRelation

    type: Optional[Union[str, "RelationType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, RelationType):
            self.type = RelationType(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Organizer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Organizer
    class_class_curie: ClassVar[str] = "confid:Organizer"
    class_name: ClassVar[str] = "Organizer"
    class_model_uri: ClassVar[URIRef] = CONFID.Organizer

    persons: Optional[Union[str, PersonId]] = None
    organisations: Optional[Union[str, OrganisationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.persons is not None and not isinstance(self.persons, PersonId):
            self.persons = PersonId(self.persons)

        if self.organisations is not None and not isinstance(self.organisations, OrganisationId):
            self.organisations = OrganisationId(self.organisations)

        super().__post_init__(**kwargs)


@dataclass
class Sponsor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Sponsor
    class_class_curie: ClassVar[str] = "confid:Sponsor"
    class_name: ClassVar[str] = "Sponsor"
    class_model_uri: ClassVar[URIRef] = CONFID.Sponsor

    persons: Optional[Union[str, PersonId]] = None
    organisations: Optional[Union[str, OrganisationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.persons is not None and not isinstance(self.persons, PersonId):
            self.persons = PersonId(self.persons)

        if self.organisations is not None and not isinstance(self.organisations, OrganisationId):
            self.organisations = OrganisationId(self.organisations)

        super().__post_init__(**kwargs)


@dataclass
class Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Contributor
    class_class_curie: ClassVar[str] = "confid:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = CONFID.Contributor

    persons: Optional[Union[str, PersonId]] = None
    type: Optional[Union[str, "ContributorType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.persons is not None and not isinstance(self.persons, PersonId):
            self.persons = PersonId(self.persons)

        if self.type is not None and not isinstance(self.type, ContributorType):
            self.type = ContributorType(self.type)

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
class Person(YAMLRoot):
    """
    A person (alive, dead, undead, or fictional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Person
    class_class_curie: ClassVar[str] = "sdo:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = CONFID.Person

    id: Union[str, PersonId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Organisation(YAMLRoot):
    """
    An organization such as a company or university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Organization
    class_class_curie: ClassVar[str] = "sdo:Organization"
    class_name: ClassVar[str] = "Organisation"
    class_model_uri: ClassVar[URIRef] = CONFID.Organisation

    id: Union[str, OrganisationId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationId):
            self.id = OrganisationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


# Enumerations
class EventType(EnumDefinitionImpl):

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
        name="EventType",
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

class ContributorType(EnumDefinitionImpl):

    presenter = PermissibleValue(text="presenter")
    moderator = PermissibleValue(text="moderator")
    attendee = PermissibleValue(text="attendee")

    _defn = EnumDefinition(
        name="ContributorType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "keynote speaker",
                PermissibleValue(text="keynote speaker") )

# Slots

