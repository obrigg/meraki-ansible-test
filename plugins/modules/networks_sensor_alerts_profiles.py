#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_sensor_alerts_profiles
short_description: Resource module for networks _sensor _alerts _profiles
description:
- Manage operations create, update and delete of the resource networks _sensor _alerts _profiles.
- Creates a sensor alert profile for a network.
- Deletes a sensor alert profile from a network.
- Updates a sensor alert profile for a network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  conditions:
    description: List of conditions that will cause the profile to send an alert.
    elements: dict
    suboptions:
      direction:
        description: If 'above', an alert will be sent when a sensor reads above the
          threshold. If 'below', an alert will be sent when a sensor reads below the
          threshold. Only applicable for temperature and humidity thresholds.
        type: str
      duration:
        description: Length of time in seconds that the triggering state must persist
          before an alert is sent. Available options are 0 seconds, 1 minute, 2 minutes,
          3 minutes, 4 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, and 1
          hour. Default is 0.
        type: int
      metric:
        description: The type of sensor metric that will be monitored for changes. Available
          metrics are door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc,
          and water.
        type: str
      threshold:
        description: Threshold for sensor readings that will cause an alert to be sent.
          This object should contain a single property key matching the condition's
          'metric' value.
        suboptions:
          door:
            description: Door open threshold. 'open' must be provided and set to true.
            suboptions:
              open:
                description: Alerting threshold for a door open event. Must be set to
                  true.
                type: bool
            type: dict
          humidity:
            description: Humidity threshold. One of 'relativePercentage' or 'quality'
              must be provided.
            suboptions:
              quality:
                description: Alerting threshold as a qualitative humidity level.
                type: str
              relativePercentage:
                description: Alerting threshold in %RH.
                type: int
            type: dict
          indoorAirQuality:
            description: Indoor air quality score threshold. One of 'score' or 'quality'
              must be provided.
            suboptions:
              quality:
                description: Alerting threshold as a qualitative indoor air quality
                  level.
                type: str
              score:
                description: Alerting threshold as indoor air quality score.
                type: int
            type: dict
          noise:
            description: Noise threshold. 'ambient' must be provided.
            suboptions:
              ambient:
                description: Ambient noise threshold. One of 'level' or 'quality' must
                  be provided.
                suboptions:
                  level:
                    description: Alerting threshold as adjusted decibels.
                    type: int
                  quality:
                    description: Alerting threshold as a qualitative ambient noise level.
                    type: str
                type: dict
            type: dict
          pm25:
            description: PM2.5 concentration threshold. One of 'concentration' or 'quality'
              must be provided.
            suboptions:
              concentration:
                description: Alerting threshold as PM2.5 parts per million.
                type: int
              quality:
                description: Alerting threshold as a qualitative PM2.5 level.
                type: str
            type: dict
          temperature:
            description: Temperature threshold. One of 'celsius', 'fahrenheit', or 'quality'
              must be provided.
            suboptions:
              celsius:
                description: Alerting threshold in degrees Celsius.
                type: float
              fahrenheit:
                description: Alerting threshold in degrees Fahrenheit.
                type: float
              quality:
                description: Alerting threshold as a qualitative temperature level.
                type: str
            type: dict
          tvoc:
            description: TVOC concentration threshold. One of 'concentration' or 'quality'
              must be provided.
            suboptions:
              concentration:
                description: Alerting threshold as TVOC micrograms per cubic meter.
                type: int
              quality:
                description: Alerting threshold as a qualitative TVOC level.
                type: str
            type: dict
          water:
            description: Water detection threshold. 'present' must be provided and set
              to true.
            suboptions:
              present:
                description: Alerting threshold for a water detection event. Must be
                  set to true.
                type: bool
            type: dict
        type: dict
    type: list
  id:
    description: Id path parameter.
    type: str
  name:
    description: Name of the sensor alert profile.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  recipients:
    description: List of recipients that will recieve the alert.
    suboptions:
      emails:
        description: A list of emails that will receive information about the alert.
        elements: str
        type: list
      httpServerIds:
        description: A list of webhook endpoint IDs that will receive information about
          the alert.
        elements: str
        type: list
      smsNumbers:
        description: A list of SMS numbers that will receive information about the alert.
        elements: str
        type: list
    type: dict
  schedule:
    description: The sensor schedule to use with the alert profile.
    suboptions:
      id:
        description: ID of the sensor schedule to use with the alert profile. If not
          defined, the alert profile will be active at all times.
        type: str
    type: dict
  serials:
    description: List of device serials assigned to this sensor alert profile.
    elements: str
    type: list
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for sensor createNetworkSensorAlertsProfile
  description: Complete reference of the createNetworkSensorAlertsProfile API.
  link: https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile
- name: Cisco Meraki documentation for sensor deleteNetworkSensorAlertsProfile
  description: Complete reference of the deleteNetworkSensorAlertsProfile API.
  link: https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile
- name: Cisco Meraki documentation for sensor updateNetworkSensorAlertsProfile
  description: Complete reference of the updateNetworkSensorAlertsProfile API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile
notes:
  - SDK Method used are
    sensor.Sensor.create_network_sensor_alerts_profile,
    sensor.Sensor.delete_network_sensor_alerts_profile,
    sensor.Sensor.update_network_sensor_alerts_profile,

  - Paths used are
    post /networks/{networkId}/sensor/alerts/profiles,
    delete /networks/{networkId}/sensor/alerts/profiles/{id},
    put /networks/{networkId}/sensor/alerts/profiles/{id},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_sensor_alerts_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    conditions:
    - direction: above
      duration: 60
      metric: temperature
      threshold:
        door:
          open: true
        humidity:
          quality: inadequate
          relativePercentage: 65
        indoorAirQuality:
          quality: fair
          score: 80
        noise:
          ambient:
            level: 120
            quality: poor
        pm25:
          concentration: 90
          quality: fair
        temperature:
          celsius: 20.5
          fahrenheit: 70
          quality: good
        tvoc:
          concentration: 400
          quality: poor
        water:
          present: true
    name: My Sensor Alert Profile
    networkId: string
    recipients:
      emails:
      - miles@meraki.com
      httpServerIds:
      - aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      smsNumbers:
      - '+15555555555'
    schedule:
      id: '5'
    serials:
    - Q234-ABCD-0001
    - Q234-ABCD-0002
    - Q234-ABCD-0003

- name: Update by id
  cisco.meraki.networks_sensor_alerts_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    conditions:
    - direction: above
      duration: 60
      metric: temperature
      threshold:
        door:
          open: true
        humidity:
          quality: inadequate
          relativePercentage: 65
        indoorAirQuality:
          quality: fair
          score: 80
        noise:
          ambient:
            level: 120
            quality: poor
        pm25:
          concentration: 90
          quality: fair
        temperature:
          celsius: 20.5
          fahrenheit: 70
          quality: good
        tvoc:
          concentration: 400
          quality: poor
        water:
          present: true
    id: string
    name: My Sensor Alert Profile
    networkId: string
    recipients:
      emails:
      - miles@meraki.com
      httpServerIds:
      - aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      smsNumbers:
      - '+15555555555'
    schedule:
      id: '5'
    serials:
    - Q234-ABCD-0001
    - Q234-ABCD-0002
    - Q234-ABCD-0003

- name: Delete by id
  cisco.meraki.networks_sensor_alerts_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: absent
    id: string
    networkId: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "profileId": "string",
      "name": "string",
      "schedule": {
        "id": "string",
        "name": "string"
      },
      "conditions": [
        {
          "metric": "string",
          "threshold": {
            "temperature": {
              "celsius": 0,
              "fahrenheit": 0,
              "quality": "string"
            },
            "humidity": {
              "relativePercentage": 0,
              "quality": "string"
            },
            "water": {
              "present": true
            },
            "door": {
              "open": true
            },
            "tvoc": {
              "concentration": 0,
              "quality": "string"
            },
            "pm25": {
              "concentration": 0,
              "quality": "string"
            },
            "noise": {
              "ambient": {
                "level": 0,
                "quality": "string"
              }
            },
            "indoorAirQuality": {
              "score": 0,
              "quality": "string"
            }
          },
          "direction": "string",
          "duration": 0
        }
      ],
      "recipients": {
        "emails": [
          "string"
        ],
        "smsNumbers": [
          "string"
        ],
        "httpServerIds": [
          "string"
        ]
      },
      "serials": [
        "string"
      ]
    }
"""
