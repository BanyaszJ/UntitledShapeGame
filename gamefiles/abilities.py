class Abilities:
    def __init__(self) -> None:
        pass


    '''A Pulse ability can:
    Radiate outwards from the player center.
    Hit a target.
    Deal damage.
    Disappear after radius reached.

    A pulse ability has:
    - current origin point (usually the player coords)
    - current radius to be drawn
    - maximal radius before disappearing
    - points of damage dealt on contact
    - speed of the pulsation? dunno yet, lets see the default value first

    '''
    class Pulse:
        def __init__(self) -> None:
            self.origin = None
            self.current_radius = None
            self.max_radius = None
            self.contact_damage = None
            # self.speed = None  # will decide later if needed

        def radiate(self)->None:
            pass

        def scan_for_hit(self)->None:
            pass

        def deal_contact_damage(self)->None:
            pass

        def disappear(self)->None:
            pass