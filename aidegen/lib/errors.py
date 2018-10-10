#!/usr/bin/env python3
#
# Copyright 2018 - The Android Open Source Project
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
"""Define errors that are raised by AIDEgen."""


class AIDEgenError(Exception):
    """Base AIDEgen exception."""


class GenerateIDEProjectFileError(AIDEgenError):
    """Raised when IDE project files are not generated."""


class JsonFileNotExistError(AIDEgenError):
    """Raised when a json file does not exist."""


class EmptyModuleDependencyError(AIDEgenError):
    """Raised when the module dependency is empty. Note that even
    a standalone module without jar dependency shall have its src path as
    dependency.
    """
