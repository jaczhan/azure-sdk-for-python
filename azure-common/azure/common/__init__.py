#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

__author__ = 'Microsoft Corp. <ptvshelp@microsoft.com>'
__version__ = '1.1.5'


def import_latest_sdk(version, module_name):
    """Import the specified version SDK in the 'module_name' module.

    This works for Autorest generated code only where folders are like:
    - azure.mgmt.compute.v2016_01_01

    Calling import_latest_sdk('v2016_01_01', __name__) in 
    azure.mgmt.compute.__init__.py will allow to use 
    azure.mgmt.compute as it was azure.mgmt.compute.v2016_01_01
    """
    import sys, importlib
    sdk_module = importlib.import_module(module_name)
    versioned_mod_name = ".".join([module_name, version])
    # Import client class in __init__.py file
    versioned_client = importlib.import_module(versioned_mod_name)
    for cls in versioned_client.__all__:
        setattr(sdk_module, cls, getattr(versioned_client, cls))
    # Import "models"
    package_to_import = "models"
    versioned_models = importlib.import_module(".".join([versioned_mod_name, package_to_import]))
    sys.modules[".".join([module_name, package_to_import])] = versioned_models
    setattr(sdk_module, package_to_import, versioned_models)


class AzureException(Exception):
    pass


class AzureHttpError(AzureException):
    def __init__(self, message, status_code):
        super(AzureHttpError, self).__init__(message)
        self.status_code = status_code

    def __new__(cls, message, status_code, *args, **kwargs):
        if cls is AzureHttpError:
            if status_code == 404:
                cls = AzureMissingResourceHttpError
            elif status_code == 409:
                cls = AzureConflictHttpError
        return AzureException.__new__(cls, message, status_code, *args, **kwargs)


class AzureConflictHttpError(AzureHttpError):
    def __init__(self, message, status_code):
        super(AzureConflictHttpError, self).__init__(message, status_code)


class AzureMissingResourceHttpError(AzureHttpError):
    def __init__(self, message, status_code):
        super(AzureMissingResourceHttpError, self).__init__(message, status_code)
