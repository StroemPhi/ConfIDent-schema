# Auto generated from confident_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-14T15:55:10
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
from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AEON = CurieNamespace('aeon', 'https://github.com/tibonto/aeon#AEON_')
CONFID = CurieNamespace('confid', 'https://raw.githubusercontent.com/StroemPhi/ConfIDent_schema/main/model/schema/confident_schema.yaml')
DBLP_SERIES = CurieNamespace('dblp_series', 'https://dblp.org/db/conf/')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
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
class NamedThingId(extended_str):
    pass


class PlannedProcessId(NamedThingId):
    pass


class AcademicEventSeriesId(PlannedProcessId):
    pass


class AcademicEventId(PlannedProcessId):
    pass


class CityId(NamedThingId):
    pass


class CountryId(NamedThingId):
    pass


class RegionId(NamedThingId):
    pass


class VenueId(NamedThingId):
    pass


class MetricId(NamedThingId):
    pass


class AcceptedPapersId(MetricId):
    pass


class OrganizerId(NamedThingId):
    pass


@dataclass
class CommonMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.CommonMetadata
    class_class_curie: ClassVar[str] = "confid:CommonMetadata"
    class_name: ClassVar[str] = "CommonMetadata"
    class_model_uri: ClassVar[URIRef] = CONFID.CommonMetadata

    website: Optional[str] = None
    logo: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.NamedThing
    class_class_curie: ClassVar[str] = "confid:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CONFID.NamedThing

    id: Union[str, NamedThingId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.PlannedProcess
    class_class_curie: ClassVar[str] = "confid:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CONFID.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    name: str = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    acronym: Optional[str] = None
    sponsors: Optional[Union[str, List[str]]] = empty_list()
    outputs: Optional[Union[str, List[str]]] = empty_list()
    topics: Optional[Union[str, List[str]]] = empty_list()
    academic_fields: Optional[Union[str, List[str]]] = empty_list()
    metrics: Optional[Union[Dict[Union[str, MetricId], Union[dict, "Metric"]], List[Union[dict, "Metric"]]]] = empty_dict()
    contact: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self._is_empty(self.organizers):
            self.MissingRequiredField("organizers")
        self._normalize_inlined_as_list(slot_name="organizers", slot_type=Organizer, key_name="id", keyed=True)

        if self.start_date is not None and not isinstance(self.start_date, str):
            self.start_date = str(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, str):
            self.end_date = str(self.end_date)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

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

        self._normalize_inlined_as_list(slot_name="metrics", slot_type=Metric, key_name="id", keyed=True)

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass
class AcademicEventSeries(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.AcademicEventSeries
    class_class_curie: ClassVar[str] = "confid:AcademicEventSeries"
    class_name: ClassVar[str] = "AcademicEventSeries"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEventSeries

    id: Union[str, AcademicEventSeriesId] = None
    name: str = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
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

    class_class_uri: ClassVar[URIRef] = CONFID.AcademicEvent
    class_class_curie: ClassVar[str] = "confid:AcademicEvent"
    class_name: ClassVar[str] = "AcademicEvent"
    class_model_uri: ClassVar[URIRef] = CONFID.AcademicEvent

    id: Union[str, AcademicEventId] = None
    name: str = None
    organizers: Union[Dict[Union[str, OrganizerId], Union[dict, "Organizer"]], List[Union[dict, "Organizer"]]] = empty_dict()
    at_location: Optional[str] = None
    in_series: Optional[Union[str, AcademicEventSeriesId]] = None
    committees: Optional[str] = None
    participants: Optional[str] = None
    ordinal: Optional[int] = None
    deadlines: Optional[Union[Union[dict, "Deadline"], List[Union[dict, "Deadline"]]]] = empty_list()
    event_type: Optional[Union[str, "EventType"]] = None
    event_status: Optional[Union[str, "EventStatus"]] = None
    event_mode: Optional[Union[str, "EventMode"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicEventId):
            self.id = AcademicEventId(self.id)

        if self.at_location is not None and not isinstance(self.at_location, str):
            self.at_location = str(self.at_location)

        if self.in_series is not None and not isinstance(self.in_series, AcademicEventSeriesId):
            self.in_series = AcademicEventSeriesId(self.in_series)

        if self.committees is not None and not isinstance(self.committees, str):
            self.committees = str(self.committees)

        if self.participants is not None and not isinstance(self.participants, str):
            self.participants = str(self.participants)

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if not isinstance(self.deadlines, list):
            self.deadlines = [self.deadlines] if self.deadlines is not None else []
        self.deadlines = [v if isinstance(v, Deadline) else Deadline(**as_dict(v)) for v in self.deadlines]

        if self.event_type is not None and not isinstance(self.event_type, EventType):
            self.event_type = EventType(self.event_type)

        if self.event_status is not None and not isinstance(self.event_status, EventStatus):
            self.event_status = EventStatus(self.event_status)

        if self.event_mode is not None and not isinstance(self.event_mode, EventMode):
            self.event_mode = EventMode(self.event_mode)

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
class City(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.City
    class_class_curie: ClassVar[str] = "confid:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = CONFID.City

    id: Union[str, CityId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Country(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Country
    class_class_curie: ClassVar[str] = "confid:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = CONFID.Country

    id: Union[str, CountryId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Region(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Region
    class_class_curie: ClassVar[str] = "confid:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = CONFID.Region

    id: Union[str, RegionId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionId):
            self.id = RegionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Venue(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Venue
    class_class_curie: ClassVar[str] = "confid:Venue"
    class_name: ClassVar[str] = "Venue"
    class_model_uri: ClassVar[URIRef] = CONFID.Venue

    id: Union[str, VenueId] = None
    name: str = None
    venue_url: Optional[Union[str, URIorCURIE]] = None
    address: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VenueId):
            self.id = VenueId(self.id)

        if self.venue_url is not None and not isinstance(self.venue_url, URIorCURIE):
            self.venue_url = URIorCURIE(self.venue_url)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

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
class Metric(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Metric
    class_class_curie: ClassVar[str] = "confid:Metric"
    class_name: ClassVar[str] = "Metric"
    class_model_uri: ClassVar[URIRef] = CONFID.Metric

    id: Union[str, MetricId] = None
    name: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetricId):
            self.id = MetricId(self.id)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class AcceptedPapers(Metric):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.AcceptedPapers
    class_class_curie: ClassVar[str] = "confid:AcceptedPapers"
    class_name: ClassVar[str] = "AcceptedPapers"
    class_model_uri: ClassVar[URIRef] = CONFID.AcceptedPapers

    id: Union[str, AcceptedPapersId] = None
    name: str = None
    value: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptedPapersId):
            self.id = AcceptedPapersId(self.id)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass
class Organizer(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFID.Organizer
    class_class_curie: ClassVar[str] = "confid:Organizer"
    class_name: ClassVar[str] = "Organizer"
    class_model_uri: ClassVar[URIRef] = CONFID.Organizer

    id: Union[str, OrganizerId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizerId):
            self.id = OrganizerId(self.id)

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
                                 description="This should be used as default to indicate that an academic event takes place as planned.") )

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

# Slots

