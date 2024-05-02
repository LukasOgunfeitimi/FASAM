# Testing functions
def activate_every_alarm(zones): # Every alarm in the building
    for zone in zones:
        for alarm in zone.alarms:
            alarm.activated = True

def activate_every_alarm_in_specified_zone(zones, zoneid): # Every alarm in specific zone
    for zone in zones:
        if zone.id == zoneid:
            for alarm in zone.alarms:
                alarm.activated = True

def activate_false_alarm_everywhere(zones): # Activate 1 Fire and 1 Security alarm everywhere
    # Its layed out as [Fire,Fire,Security,Security]
    # so activate the first and second
    for zone in zones:
        zone.alarms[0].activated = True
        zone.alarms[2].activated = True

def activate_false_alarm_in_specificed_zone(zones, zoneid): # Activate 1 Fire and 1 Security alarm in a zone
    for zone in zones:
        if zone.id == zoneid:
            zone.alarms[0].activated = True
            zone.alarms[2].activated = True