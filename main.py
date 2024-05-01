class Zone:
    def __init__(self, id):
        self.id = id
        self.alarms = []
        self.doors = False
        self.electrics = True
    
    # Check all alarms and append activated
    # ones to an array
    def check_alarms(self):
        activated = []
        for alarm in self.alarms:
            if alarm.activated == True:
                activated.append(alarm)
    
    def lock_doors(self):
        self.doors = True

    def shut_down_electrics(self):
        self.electrics = False

    def call_emergency_services():
        pass

class Alarm:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.activated = False

class FireAlarm(Alarm):
    def __init__(self, id):
        super().__init__(id, "Fire")
        self.sprinkler_status = False
        self.direction_indicator = False
    
    def activate_sprinkler(self):
        self.sprinkler_status = True

    def activate_direction_indicators(self):
        self.direction_indicator = True

class SecurityAlarm(Alarm):
    def __init__(self, id):
        super().__init__(id, "Security")
    pass

zones = []

def check():
    for zone in zones:
        activated = zone.check_alarms()
        fire_alarms = [a for a in activated if isinstance(a, FireAlarm)]
        security_alarms = [a for a in activated if isinstance(a, SecurityAlarm)]



# 3 zones, 4 alarms each (2 fire, 2 security)
def populate():
    for i in range(3):
        zone = Zone(i + 1)
        zone.alarms = [FireAlarm(1), FireAlarm(2), SecurityAlarm(3), SecurityAlarm(4)]
        zones.append(zone)



if __name__ == "__main__":
    populate()