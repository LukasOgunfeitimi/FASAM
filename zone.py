class Zone:
    def __init__(self, id, fire_class, security_class):
        self.id = id
        self.alarms = [
            fire_class(1, self),
            fire_class(2, self),
            security_class(3, self),
            security_class(4, self)
        ]
        self.lock_doors = False
        self.sprinkler = False
        self.direction_indicators = False
        self.electrics = True

    # Check all alarms and append activated ones to an array
    def check_alarms(self):
        return [alarm for alarm in self.alarms if alarm.activated]

    def start_protocol(self):
        confirmed_fire_alarms = [alarm for alarm in self.alarms if isinstance(alarm, FireAlarm) and alarm.activated]
        confirmed_security_alarms = [alarm for alarm in self.alarms if isinstance(alarm, SecurityAlarm) and alarm.activated]

        if confirmed_fire_alarms:
            self.activate_fire_protocol()
        if confirmed_security_alarms:
            self.activate_security_protocol()

        self.call_emergency_services()

    def activate_fire_protocol(self):
        self.sprinkler = True
        self.electrics = False
        self.direction_indicators = True
        print(f"[ZONE {self.id}] Fire protocol activated: Sprinklers on, Electrics off, Direction indicators on.")

    def activate_security_protocol(self):
        self.lock_doors = True
        print(f"[ZONE {self.id}] Security protocol activated: Doors locked.")

    def call_emergency_services(self):
        print(f"[ZONE {self.id}] Calling emergency services...")
