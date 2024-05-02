from zone import Zone
from alarm import FireAlarm, SecurityAlarm
from test import *
# Main requirements:
# 1. Any activated alarms should not be ignored
# 2. In an event of a fire alarm, the sprinkler system
# should be activated, electrics should turn off and 
# direction indicators should illuminate
# 3. In an event of a security alarm, internal doors should lock
# 4. In every alarm that is activated, the other alarms should be checked
# for false alarms

zones = []

# Seen as there's 2 fire and 2 security alarms
# in each zone, if theres 1 alarm of a type we'll
# call it a false alarm
# eg. 1 Fire alarm activated = False fire alarm
# eg. 2 Fire alarm activated = Real fire emergency
def check():
    for zone in zones:
        print(f"[ZONE {zone.id}] Checking", end='')
        print()
        activated = zone.check_alarms()
        if len(activated) == 0:
            print(f"[ZONE {zone.id}] Clear")
            print()
            continue

        fire_alarms = [a for a in activated if isinstance(a, FireAlarm)]
        print(f"[ZONE {zone.id}] ", end='')
        match len(fire_alarms):
            case 0:
                print("No fire alarms activated")
            case 1:
                print("False alarm detected")
            case 2:
                print("Real Fire alarm detected")
                fire_alarms[0].start_protocol()
        
        print()
        security_alarms = [a for a in activated if isinstance(a, SecurityAlarm)]
        print(f"[ZONE {zone.id}] ", end='')
        match len(security_alarms):
            case 0:
                print("No security alarms activated")
            case 1:
                print("False security alarm detected")
            case 2:
                print("Real security alarm detected")
                security_alarms[0].start_protocol()
        print()



# 3 zones, 4 alarms each (2 fire, 2 security)
def populate():
    for i in range(3):
        zone = Zone(i + 1, FireAlarm, SecurityAlarm)
        zones.append(zone)
    activate_every_alarm(zones)
    #activate_every_alarm_in_specified_zone(zones, 1)
    #activate_false_alarm_everywhere(zones)
    #activate_false_alarm_in_specificed_zone(zones, 1)
    check()

if __name__ == "__main__":
    populate()

