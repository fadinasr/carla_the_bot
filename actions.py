# This files contains your custom actions which can be used to run
# custom Python code.

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text


class ContactForm(FormAction):

    def name(self):
        return "contact_us_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "first_name",
            "last_name",
            "email",
            "company"
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict]:

        dispatcher.utter_message("Thank you for getting in touch, we’ll contact you soon")
        return []
