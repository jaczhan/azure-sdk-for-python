# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os

def _get_api_version(api_version=None, profile=None):
    if api_version:
        return api_version
    if profile:
        api_version = 'FIXME' # Figure out profile reading
    if not api_version:
        # FIXME load configuration file and set api_version
        api_version = os.environ.get('AZURE_RESOURCE_RESOURCES_API_VERSION')
        if api_version:
            return api_version
    # Default
    return 'latest'

def client(api_version=None, profile=None, **kwargs):
    api_version = _get_api_version(api_version, profile)

    if 'subscription_id' not in kwargs:
        kwargs['subscription_id'] = os.environ.get('AZURE_SUBSCRIPTION_ID')

    # Generated from here
    if api_version == 'latest' or api_version == '2016-07-01':
        from .v2016_07_01 import ResourceManagementClient
        return ResourceManagementClient(**kwargs)
    elif api_version == '2016-02-01':
        from .v2016_02_01 import ResourceManagementClient
        return ResourceManagementClient(**kwargs)
    raise ValueError("Unsupported API Version: {}".format(api_version))

def models(api_version=None, profile=None):
    api_version = _get_api_version(api_version, profile)

    # Generated from here
    if api_version == 'latest' or api_version == '2016-07-01':
        from .v2016_07_01 import models
        return models
    elif api_version == '2016-02-01':
        from .v2016_02_01 import models
        return models
    raise ValueError("Unsupported API Version: {}".format(api_version))