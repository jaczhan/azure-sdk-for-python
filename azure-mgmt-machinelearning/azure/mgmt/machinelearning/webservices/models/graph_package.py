# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphPackage(Model):
    """Defines the graph of modules making up the machine learning solution.

    :param nodes: The set of nodes making up the graph, provided as a nodeId
     to GraphNode map
    :type nodes: dict
    :param edges: The list of edges making up the graph.
    :type edges: list of :class:`GraphEdge
     <azure.mgmt.machinelearning.webservices.models.GraphEdge>`
    :param graph_parameters: The collection of global parameters for the
     graph, given as a global parameter name to GraphParameter map. Each
     parameter here has a 1:1 match with the global parameters values map
     declared at the WebServiceProperties level.
    :type graph_parameters: dict
    """

    _attribute_map = {
        'nodes': {'key': 'nodes', 'type': '{GraphNode}'},
        'edges': {'key': 'edges', 'type': '[GraphEdge]'},
        'graph_parameters': {'key': 'graphParameters', 'type': '{GraphParameter}'},
    }

    def __init__(self, nodes=None, edges=None, graph_parameters=None):
        self.nodes = nodes
        self.edges = edges
        self.graph_parameters = graph_parameters
