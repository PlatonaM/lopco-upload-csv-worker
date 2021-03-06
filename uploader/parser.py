"""
   Copyright 2020 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


__all__ = ("Parser",)


import paho.mqtt.client
import threading
import os
import json
import time


class Parser(threading.Thread):
    def __init__(self, ds_id: str, srv_id: str, file: str, dc_path: str, delimiter: str, client: paho.mqtt.client.Client):
        super().__init__(name="parser-{}".format(file), daemon=True)
        self.__ds_id = ds_id
        self.__srv_id = srv_id
        self.__file_path = os.path.join(dc_path, file)
        self.__delimiter = delimiter
        self.__client = client
        self.__pub_count = 0

    def run(self) -> None:
        print("publishing messages for '{}'".format(self.__srv_id))
        with open(self.__file_path, "r") as file:
            fields = file.readline()
            fields = fields.strip()
            fields = fields.split(self.__delimiter)
            for line in file:
                line = line.strip()
                line = line.split(self.__delimiter)
                data = dict()
                for i in range(0, len(fields)):
                    if line[i].isnumeric():
                        try:
                            data[fields[i]] = int(line[i])
                        except ValueError:
                            data[fields[i]] = line[i]
                    elif "." in line[i] or "," in line[i]:
                        try:
                            data[fields[i]] = float(line[i])
                        except ValueError:
                            data[fields[i]] = line[i]
                    else:
                        data[fields[i]] = line[i]
                self.__produce(json.dumps(data))
        print("published '{}' messages for '{}'".format(self.__pub_count, self.__srv_id))

    def __produce(self, data: str):
        while True:
            msg_info = self.__client.publish(topic=self.__ds_id+"/"+self.__srv_id, payload=data, qos=2)
            msg_info.wait_for_publish()
            if msg_info.rc == paho.mqtt.client.MQTT_ERR_SUCCESS:
                self.__pub_count += 1
                break
            print("failed to publish message '{}' for '{}'".format(self.__pub_count, self.__srv_id))
            time.sleep(5)
