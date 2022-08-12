# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for RemoveDirectory
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataform


# [START dataform_v1beta1_generated_Dataform_RemoveDirectory_sync]
from google.cloud import dataform_v1beta1


def sample_remove_directory():
    # Create a client
    client = dataform_v1beta1.DataformClient()

    # Initialize request argument(s)
    request = dataform_v1beta1.RemoveDirectoryRequest(
        workspace="workspace_value",
        path="path_value",
    )

    # Make the request
    client.remove_directory(request=request)


# [END dataform_v1beta1_generated_Dataform_RemoveDirectory_sync]
