class Zone:
    def __init__(self, id, FireClass, SecurityClass):
        self.id = id
        self.alarms = [FireClass(1, id), FireClass(2, id), SecurityClass(3, id), SecurityClass(4, id)]
        self.lock_doors = False
        self.sprinkler = False
        self.direction_indicators = False
        self.electrics = True
    
    # Check all alarms and append activated
    # ones to an array
    def check_alarms(self):
        activated = []
        for alarm in self.alarms:
            if alarm.activated == True:
                activated.append(alarm)
        return activated
    
    def getid(self):
        return self.id
    
    def start_protocol(self):
        self.call_emergency_services()

    def call_emergency_services(self):
        print(f"[ZONE {self.zone_id}] Calling emergency services...")