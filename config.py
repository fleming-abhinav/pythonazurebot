#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "164d9dc1-d86f-4153-b466-da7ed4fb6e18")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Coviebot@86216373")


    QNA_KNOWLEDGEBASE_ID = os.environ.get("47a04f69-a13f-4478-abb4-2422d919e263", "")
    QNA_ENDPOINT_KEY = os.environ.get("58e42c52-15ff-4a82-a562-754fd3ade125", "")
    QNA_ENDPOINT_HOST = os.environ.get("https://mycovidbot19.azurewebsites.net/qnamaker", "")
    LUIS_APP_ID = os.environ.get("9269ac15-b039-41c1-9548-126623cae4f7", "")
    LUIS_API_KEY = os.environ.get("a1ef04cf0d2e44079a8fa68eab719469", "")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("https://westus.api.cognitive.microsoft.com/", "")
