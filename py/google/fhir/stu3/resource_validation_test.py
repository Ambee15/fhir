#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test resource validation functionality."""

import os
from typing import Type

from google.protobuf import message
from absl.testing import absltest
from proto.google.fhir.proto.stu3 import resources_pb2
from google.fhir.core import fhir_errors
from google.fhir.core.testing import testdata_utils
from google.fhir.stu3 import resource_validation

_VALIDATION_DIR = os.path.join('testdata', 'stu3', 'validation')


class ResourceValidationTest(absltest.TestCase):
  """Basic unit test suite ensuring that resource validation works correctly."""

  def test_resource_validation_with_missing_required_field_raises(self):
    self._invalid_test('observation_invalid_missing_required',
                       resources_pb2.Observation)

  def test_resource_validation_with_invalid_primitive_raises(self):
    self._invalid_test('observation_invalid_primitive',
                       resources_pb2.Observation)

  def test_resource_validation_with_valid_reference_succeeds(self):
    self._valid_test('observation_valid_reference', resources_pb2.Observation)

  def test_resource_validation_with_invalid_reference_raises(self):
    self._invalid_test('observation_invalid_reference',
                       resources_pb2.Observation)

  # TODO(b/155795499): Implement FHIR-Path validation for Python API
  # def test_resource_validation_with_fhir_path_violation_raises(self):
  #   self._invalid_test('observation_invalid_fhirpath_violation',
  #                     resources_pb2.Observation)

  def test_resource_validation_with_valid_repeated_reference_succeeds(self):
    self._valid_test('encounter_valid_repeated_reference',
                     resources_pb2.Encounter)

  def test_resource_validation_with_invalid_repeated_reference_raies(self):
    self._invalid_test('encounter_invalid_repeated_reference',
                       resources_pb2.Encounter)

  def test_resource_validation_with_invalid_empty_oneof_raises(self):
    self._invalid_test('observation_invalid_empty_oneof',
                       resources_pb2.Observation)

  def test_resource_validation_with_valid_bundle_succeeds(self):
    self._valid_test('bundle_valid', resources_pb2.Bundle)

  def test_resource_validation_with_start_later_than_end_raises(self):
    self._invalid_test('encounter_invalid_start_later_than_end',
                       resources_pb2.Encounter)

  def test_resource_validation_with_start_later_than_end_with_end_precision_succeeds(
      self,
  ):
    self._valid_test('encounter_valid_start_later_than_end_day_precision',
                     resources_pb2.Encounter)

  def test_resource_validation_with_valid_encounter_succeeds(self):
    self._valid_test('encounter_valid', resources_pb2.Encounter)

  def test_resource_validation_with_valid_numeric_timezone_succeeds(self):
    self._valid_test('encounter_valid_numeric_timezone',
                     resources_pb2.Encounter)

  def _valid_test(self, name: str, message_cls: Type[message.Message]) -> None:
    msg = testdata_utils.read_protos(
        os.path.join(_VALIDATION_DIR, name + '.prototxt'), message_cls)[0]
    resource_validation.validate_resource(msg)

  def _invalid_test(self, name: str,
                    message_cls: Type[message.Message]) -> None:
    msg = testdata_utils.read_protos(
        os.path.join(_VALIDATION_DIR, name + '.prototxt'), message_cls)[0]

    with self.assertRaises(fhir_errors.InvalidFhirError) as fe:
      resource_validation.validate_resource(msg)

    self.assertIsInstance(fe.exception, fhir_errors.InvalidFhirError)


if __name__ == '__main__':
  absltest.main()
