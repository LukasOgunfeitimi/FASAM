from zone import Zone
class Alarm(Zone):
    def __init__(self, id, type, zone_id):
        self.id = id
        self.type = type
        self.zone_id = zone_id
        self.activated = False

class FireAlarm(Alarm):
    def __init__(self, id, zone_id):
        super().__init__(id, "Fire", zone_id)
    
    def start_protocol(self):
        self.sprinkler = True
        print(f"[ZONE {self.zone_id}] Sprinklers activated...")

        self.electrics = False
        print(f"[ZONE {self.zone_id}] Electrics deactivated...")

        self.direction_indicators = True
        print(f"[ZONE {self.zone_id}] Direction indicators activated...")

        Zone.start_protocol(self)

class SecurityAlarm(Alarm):
    def __init__(self, id, zone_id):
        super().__init__(id, "Security", zone_id)

    def start_protocol(self):
        self.lock_doors = True
        print(f"[ZONE {self.zone_id}] Doors locked...")

        Zone.start_protocol(self)
