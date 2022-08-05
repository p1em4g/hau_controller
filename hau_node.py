#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from plexus.nodes.node import BaseNode, PeriodicCallback
import serial
from devices.hau_handler import HAUHandler

class HAUNode(BaseNode):
    """

    """
    def __init__(self, endpoint: str, list_of_nodes: list, is_daemon: bool = True):
        super().__init__(endpoint, list_of_nodes, is_daemon)
        self._annotation = "humidification and aeration unit"

        self.hau_handler = HAUHandler(
            name="hau_handler",
        )

        self.add_device(self.hau_handler)

    def custom_preparation(self):
       pass


if __name__ == "__main__":
    network1 = [
        {"address": "tcp://10.9.0.12:5666",}
    ]
    n1 = HAUNode(network1[0]['address'], list_of_nodes=network1)
    n1.start()
    n1.join()