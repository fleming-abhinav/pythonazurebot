# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai import luis
from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from botbuilder.ai.luis import LuisApplication, LuisPredictionOptions,LuisRecognizer
import requests
class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # The actual call to the QnA Maker service.
        luis_result=await self.LuisReg.recognize(turn_context)
        intent=LuisRecognizer.top_intent(luis_result)
       
        if intent=="booking":
            try:
                city_entities = luis_result.entities.get("city", {})
                date_entities = luis_result.entities.get("date", {})
                city_name=city_entities[0]
                date_of_test=date_entities[0]
                print(city_name,date_of_test)
                await turn_context.send_activity("Your covid test successfully booked on "+date_of_test+" in "+city_name)
            except:
                await turn_context.send_activity("I didnt get you!")

##        await turn_context.send_activity(f"Your Queries related to : {intent}")
        elif intent=="covid_statitics":
            try:
                case_entity = luis_result.entities.get("covidcase", {})
                
                case_val=case_entity[0]
                
                print(case_val)
                
                resp= requests.get("https://api.covidtracking.com/v1/us/current.json")
                x=resp.json()
                if case_val=="positive":
                    print(x[0]["positive"])
                    await turn_context.send_activity("Number of positive cases are "+str(x[0]["positive"]))
                else:
                    print(x[0]["negative"])
                    await turn_context.send_activity("Number of Negative  cases are "+str(x[0]["negative"]))

            except:
                await turn_context.send_activity("I didnt get you!")
        else:
            response = await self.qna_maker.get_answers(turn_context)
            if response and len(response) > 0 and response[0].score>0.8:
                
                intentscore=response[0].score
                print(intentscore)
                await turn_context.send_activity(MessageFactory.text(response[0].answer))
            else:
                await turn_context.send_activity("No QnA Maker answers were found.")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello! How can i help you?")
                
    def __init__(self, config: Config):
        luis_app=LuisApplication ("89b879af-991b-41f5-8ee9-8bdb66eff7cc","2f86262012cf400880c7c048e45e3936","https://westeurope.api.cognitive.microsoft.com/")
        luis_option=LuisPredictionOptions(include_all_intents=True,include_instance_data=True)
        self.LuisReg=LuisRecognizer(luis_app,luis_option,True)
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id="05adcde8-d602-4718-93a6-7dd42ca66042",
                endpoint_key="b24ec397-faab-4e1b-a10c-d0347edd2288",
                host="https://covidbotqna.azurewebsites.net/qnamaker",
        )
    )

















        
