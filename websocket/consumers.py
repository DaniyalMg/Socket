from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json


class AdminNotify(WebsocketConsumer):
    def connect(self):
        # self.room_name = 'admin'
        # self.room_group_name = 'admin_group'
        #
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        self.accept()
        self.send(text_data=json.dumps({
            'status': 'add'
        }))

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass

    def reserve_notify(self, event):
        reserve = event['reserve']

        self.send(text_data=reserve)
