#!/usr/bin/python3

import appdaemon.appapi as appapi



class TimedSlider(appapi.AppDaemon)
    def initialize(self):
        self.slider_name = self.args["slider"];
        self.listen_state(self.state_change, self.args["switch"], new="on")
