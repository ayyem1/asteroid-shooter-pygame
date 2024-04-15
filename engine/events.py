from enum import Enum
from typing import Union

import pygame


class CustomEventType(Enum):
    pass


class EventSystem(object):
    _instance = None
    _events: dict[CustomEventType, pygame.event.Event] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventSystem, cls).__new__(cls)
            # Put any initialization here.
            cls._instance.user_event_slot = pygame.event.custom_type()

        return cls._instance

    def create_custom_event(
        self, custom_event_type: CustomEventType
    ) -> pygame.event.Event:
        if custom_event_type in self._events:
            print("This event already exists")
            return

        event = pygame.event.Event(
            self.user_event_slot, custom_event_type=custom_event_type
        )

        self._events[custom_event_type] = event

        return event

    def get_custom_event(
        self, custom_event_type: CustomEventType
    ) -> Union[pygame.event.Event, None]:
        if custom_event_type not in self._events:
            return None

        return self._events[custom_event_type]
