############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color,
                 is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

    def __repr__(self):
        """Defines object representation"""
        return self.name


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    muskmelon.add_pairing("mint")

    casaba = MelonType("Casaba", "cas", 2003, "orange", False, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013, "yellow",
                                  False, True)
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])

    return all_melon_types


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons = {}

    for melon in melon_types:

        melons[melon.code] = melon

    return melons

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    def __init__(self, melon_num, melon_type, shape_rating, color_rating,
                 field, harvester):

        self.melon_num = melon_num
        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        self.is_sellable = self.is_sellable()

    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5:

            if self.field != 3:
                return True

            else:
                return False

        else:
            return False

    def __repr__(self):
        """Defines object representation"""
        return self.melon_num


def make_melons(melons):
    """Returns a list of Melon objects."""

    harvest_melons = []

    melon1 = Melon("M1", melons["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon("M2", melons["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon("M3", melons["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon("M4", melons["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon("M5", melons["cren"], 8, 9, 35, "Michael")
    melon6 = Melon('M6', melons["cren"], 8, 2, 35, "Michael")
    melon7 = Melon('M7', melons['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon("M8", melons["musk"], 6, 7, 4, "Michael")
    melon9 = Melon("M9", melons["yw"], 7, 10, 3, "Sheila")

    harvest_melons.extend([melon1, melon2, melon3, melon4, melon5, melon6,
                           melon7, melon8, melon9])

    return harvest_melons


def get_sellability_report(harvest_melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in harvest_melons:

        if self.is_sellable == True:
            print "{}: Harvested by {} from Field # {}, CAN BE SOLD".format(
                    melon.melon_num, melon.harvester, melon.field)

        else:
            print "{}: Harvested by {} from Field # {}, NOT SELLABLE".format(
                    melon.melon_num, melon.harvester, melon.field)


if __name__ == "__main__":
    melon_types = make_melon_types()
#     print make_melon_type_lookup(melon_types)
    melons = make_melon_type_lookup(melon_types)
    melon_harvest = make_melons(melons)
    get_sellability_report(melon_harvest)
