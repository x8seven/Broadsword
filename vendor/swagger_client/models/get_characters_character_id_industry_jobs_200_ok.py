# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCharactersCharacterIdIndustryJobs200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'job_id': 'int',
        'installer_id': 'int',
        'facility_id': 'int',
        'station_id': 'int',
        'activity_id': 'int',
        'blueprint_id': 'int',
        'blueprint_type_id': 'int',
        'blueprint_location_id': 'int',
        'output_location_id': 'int',
        'runs': 'int',
        'cost': 'float',
        'licensed_runs': 'int',
        'probability': 'float',
        'product_type_id': 'int',
        'status': 'str',
        'duration': 'int',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'pause_date': 'datetime',
        'completed_date': 'datetime',
        'completed_character_id': 'int',
        'successful_runs': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'installer_id': 'installer_id',
        'facility_id': 'facility_id',
        'station_id': 'station_id',
        'activity_id': 'activity_id',
        'blueprint_id': 'blueprint_id',
        'blueprint_type_id': 'blueprint_type_id',
        'blueprint_location_id': 'blueprint_location_id',
        'output_location_id': 'output_location_id',
        'runs': 'runs',
        'cost': 'cost',
        'licensed_runs': 'licensed_runs',
        'probability': 'probability',
        'product_type_id': 'product_type_id',
        'status': 'status',
        'duration': 'duration',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'pause_date': 'pause_date',
        'completed_date': 'completed_date',
        'completed_character_id': 'completed_character_id',
        'successful_runs': 'successful_runs'
    }

    def __init__(self, job_id=None, installer_id=None, facility_id=None, station_id=None, activity_id=None, blueprint_id=None, blueprint_type_id=None, blueprint_location_id=None, output_location_id=None, runs=None, cost=None, licensed_runs=None, probability=None, product_type_id=None, status=None, duration=None, start_date=None, end_date=None, pause_date=None, completed_date=None, completed_character_id=None, successful_runs=None):
        """
        GetCharactersCharacterIdIndustryJobs200Ok - a model defined in Swagger
        """

        self._job_id = None
        self._installer_id = None
        self._facility_id = None
        self._station_id = None
        self._activity_id = None
        self._blueprint_id = None
        self._blueprint_type_id = None
        self._blueprint_location_id = None
        self._output_location_id = None
        self._runs = None
        self._cost = None
        self._licensed_runs = None
        self._probability = None
        self._product_type_id = None
        self._status = None
        self._duration = None
        self._start_date = None
        self._end_date = None
        self._pause_date = None
        self._completed_date = None
        self._completed_character_id = None
        self._successful_runs = None
        self.discriminator = None

        self.job_id = job_id
        self.installer_id = installer_id
        self.facility_id = facility_id
        self.station_id = station_id
        self.activity_id = activity_id
        self.blueprint_id = blueprint_id
        self.blueprint_type_id = blueprint_type_id
        self.blueprint_location_id = blueprint_location_id
        self.output_location_id = output_location_id
        self.runs = runs
        if cost is not None:
          self.cost = cost
        if licensed_runs is not None:
          self.licensed_runs = licensed_runs
        if probability is not None:
          self.probability = probability
        if product_type_id is not None:
          self.product_type_id = product_type_id
        self.status = status
        self.duration = duration
        self.start_date = start_date
        self.end_date = end_date
        if pause_date is not None:
          self.pause_date = pause_date
        if completed_date is not None:
          self.completed_date = completed_date
        if completed_character_id is not None:
          self.completed_character_id = completed_character_id
        if successful_runs is not None:
          self.successful_runs = successful_runs

    @property
    def job_id(self):
        """
        Gets the job_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Unique job ID

        :return: The job_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Unique job ID

        :param job_id: The job_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")

        self._job_id = job_id

    @property
    def installer_id(self):
        """
        Gets the installer_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the character which installed this job

        :return: The installer_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._installer_id

    @installer_id.setter
    def installer_id(self, installer_id):
        """
        Sets the installer_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the character which installed this job

        :param installer_id: The installer_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if installer_id is None:
            raise ValueError("Invalid value for `installer_id`, must not be `None`")

        self._installer_id = installer_id

    @property
    def facility_id(self):
        """
        Gets the facility_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the facility where this job is running

        :return: The facility_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """
        Sets the facility_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the facility where this job is running

        :param facility_id: The facility_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")

        self._facility_id = facility_id

    @property
    def station_id(self):
        """
        Gets the station_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the station where industry facility is located

        :return: The station_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        """
        Sets the station_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the station where industry facility is located

        :param station_id: The station_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if station_id is None:
            raise ValueError("Invalid value for `station_id`, must not be `None`")

        self._station_id = station_id

    @property
    def activity_id(self):
        """
        Gets the activity_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Job activity ID

        :return: The activity_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Job activity ID

        :param activity_id: The activity_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")

        self._activity_id = activity_id

    @property
    def blueprint_id(self):
        """
        Gets the blueprint_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        blueprint_id integer

        :return: The blueprint_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._blueprint_id

    @blueprint_id.setter
    def blueprint_id(self, blueprint_id):
        """
        Sets the blueprint_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        blueprint_id integer

        :param blueprint_id: The blueprint_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if blueprint_id is None:
            raise ValueError("Invalid value for `blueprint_id`, must not be `None`")

        self._blueprint_id = blueprint_id

    @property
    def blueprint_type_id(self):
        """
        Gets the blueprint_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        blueprint_type_id integer

        :return: The blueprint_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._blueprint_type_id

    @blueprint_type_id.setter
    def blueprint_type_id(self, blueprint_type_id):
        """
        Sets the blueprint_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        blueprint_type_id integer

        :param blueprint_type_id: The blueprint_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if blueprint_type_id is None:
            raise ValueError("Invalid value for `blueprint_type_id`, must not be `None`")

        self._blueprint_type_id = blueprint_type_id

    @property
    def blueprint_location_id(self):
        """
        Gets the blueprint_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility

        :return: The blueprint_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._blueprint_location_id

    @blueprint_location_id.setter
    def blueprint_location_id(self, blueprint_location_id):
        """
        Sets the blueprint_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility

        :param blueprint_location_id: The blueprint_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if blueprint_location_id is None:
            raise ValueError("Invalid value for `blueprint_location_id`, must not be `None`")

        self._blueprint_location_id = blueprint_location_id

    @property
    def output_location_id(self):
        """
        Gets the output_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility

        :return: The output_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._output_location_id

    @output_location_id.setter
    def output_location_id(self, output_location_id):
        """
        Sets the output_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility

        :param output_location_id: The output_location_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if output_location_id is None:
            raise ValueError("Invalid value for `output_location_id`, must not be `None`")

        self._output_location_id = output_location_id

    @property
    def runs(self):
        """
        Gets the runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of runs for a manufacturing job, or number of copies to make for a blueprint copy

        :return: The runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """
        Sets the runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of runs for a manufacturing job, or number of copies to make for a blueprint copy

        :param runs: The runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if runs is None:
            raise ValueError("Invalid value for `runs`, must not be `None`")

        self._runs = runs

    @property
    def cost(self):
        """
        Gets the cost of this GetCharactersCharacterIdIndustryJobs200Ok.
        The sume of job installation fee and industry facility tax

        :return: The cost of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this GetCharactersCharacterIdIndustryJobs200Ok.
        The sume of job installation fee and industry facility tax

        :param cost: The cost of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: float
        """

        self._cost = cost

    @property
    def licensed_runs(self):
        """
        Gets the licensed_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of runs blueprint is licensed for

        :return: The licensed_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._licensed_runs

    @licensed_runs.setter
    def licensed_runs(self, licensed_runs):
        """
        Sets the licensed_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of runs blueprint is licensed for

        :param licensed_runs: The licensed_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """

        self._licensed_runs = licensed_runs

    @property
    def probability(self):
        """
        Gets the probability of this GetCharactersCharacterIdIndustryJobs200Ok.
        Chance of success for invention

        :return: The probability of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """
        Sets the probability of this GetCharactersCharacterIdIndustryJobs200Ok.
        Chance of success for invention

        :param probability: The probability of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: float
        """

        self._probability = probability

    @property
    def product_type_id(self):
        """
        Gets the product_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Type ID of product (manufactured, copied or invented)

        :return: The product_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """
        Sets the product_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        Type ID of product (manufactured, copied or invented)

        :param product_type_id: The product_type_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """

        self._product_type_id = product_type_id

    @property
    def status(self):
        """
        Gets the status of this GetCharactersCharacterIdIndustryJobs200Ok.
        status string

        :return: The status of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this GetCharactersCharacterIdIndustryJobs200Ok.
        status string

        :param status: The status of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["active", "cancelled", "delivered", "paused", "ready", "reverted"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def duration(self):
        """
        Gets the duration of this GetCharactersCharacterIdIndustryJobs200Ok.
        Job duration in seconds

        :return: The duration of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this GetCharactersCharacterIdIndustryJobs200Ok.
        Job duration in seconds

        :param duration: The duration of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")

        self._duration = duration

    @property
    def start_date(self):
        """
        Gets the start_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job started

        :return: The start_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job started

        :param start_date: The start_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job finished

        :return: The end_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job finished

        :param end_date: The end_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")

        self._end_date = end_date

    @property
    def pause_date(self):
        """
        Gets the pause_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)

        :return: The pause_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: datetime
        """
        return self._pause_date

    @pause_date.setter
    def pause_date(self, pause_date):
        """
        Sets the pause_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)

        :param pause_date: The pause_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: datetime
        """

        self._pause_date = pause_date

    @property
    def completed_date(self):
        """
        Gets the completed_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job was completed

        :return: The completed_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """
        Sets the completed_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        Date and time when this job was completed

        :param completed_date: The completed_date of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def completed_character_id(self):
        """
        Gets the completed_character_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the character which completed this job

        :return: The completed_character_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._completed_character_id

    @completed_character_id.setter
    def completed_character_id(self, completed_character_id):
        """
        Sets the completed_character_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        ID of the character which completed this job

        :param completed_character_id: The completed_character_id of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """

        self._completed_character_id = completed_character_id

    @property
    def successful_runs(self):
        """
        Gets the successful_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of successful runs for this job. Equal to runs unless this is an invention job

        :return: The successful_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :rtype: int
        """
        return self._successful_runs

    @successful_runs.setter
    def successful_runs(self, successful_runs):
        """
        Sets the successful_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        Number of successful runs for this job. Equal to runs unless this is an invention job

        :param successful_runs: The successful_runs of this GetCharactersCharacterIdIndustryJobs200Ok.
        :type: int
        """

        self._successful_runs = successful_runs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetCharactersCharacterIdIndustryJobs200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
