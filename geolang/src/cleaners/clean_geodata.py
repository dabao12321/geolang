import json
import string
import numpy as np

def abbrev_to_state(abbreviations):
    '''Takes in a comma seperated string that lists state abbreviations.
    Outputs a comma seperated string that lists full state names.

    ex. abbrev_to_state("ak, al, ar") --> "alaska, alabama, arkansas"
    '''
    output = ""
    abbrevs = abbreviations.split(", ")
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    for state in abbrevs:
        name = states.get(state.upper())
        if name is None:
            raise ValueError("Invalid parameter input.")
        output += name.lower() + ", "
    return output[:-2]

def get_regions():
    '''
    Returns a dictionary of regions in the U.S. linked to the states they contain.
    Ex. "ozarks" --> missouri, oklahoma, arkansas
    '''
    regions = {"allegheny mountains": abbrev_to_state("md, va, pa, wv"),
                    "appalachians": abbrev_to_state("pa, wv, md, va, nc, ky, tn, nc, ga, al"),
                    "atlantic": abbrev_to_state("me, nh, vt, ma, ct, ri, ny, pa, nj, de, md, dc, va, nc, ga, sc, fl"),
                    "central": abbrev_to_state("ne, ks, mo, ok, ar"),
                    "central atlantic": abbrev_to_state("pa, de, nj, md, dc, va"),
                    "chesapeake bay": abbrev_to_state("md, va"),
                    "delmarva": abbrev_to_state("de, md, va"),
                    "desert southwest": abbrev_to_state("ca, az, nm"),
                    "great lakes": abbrev_to_state("mn, wi, mi, il, in, oh, pa, ny"),
                    "gulf states": abbrev_to_state("tx, la, ms, al, fl"),
                    "inland north": abbrev_to_state("wa, or, id, mt, wy, nd, sd, mn, ia, wi, il, mi, in, oh, pa, ny, nj"),
                    "inland south": abbrev_to_state("ky, tn, al, ms"),
                    "lower mississippi valley": abbrev_to_state("mo, ky, il, tn, ar, la, ms"),
                    "middle atlantic": abbrev_to_state("md, dc, va, nc, sc"),
                    "midland": abbrev_to_state("sd, ne, ia, mo, ok, ar, la, ms, tn, ky, il, in, oh, wv, pa, md, de, nj, va, nc, ga, al, sc"),
                    "mississippi valley": abbrev_to_state("mn, wi, ia, il, mo, ar, ky, tn, la, ms"),
                    "mississippi ohio valleys": abbrev_to_state("mn, wi, ia, il, mo, in, oh, ky"),
                    "new england": abbrev_to_state("vt, nh, me, ma, ct, ri"),
                    "north": abbrev_to_state("wa, or, id, mt, wy, nd, sd, mn, wi, ia, il, mi, in, oh, pa, ny, nj, ct, vt, nh, ma, ri, me"),
                    "north atlantic": abbrev_to_state("me, nh, vt, ny, nj, ma, ct, ri"),
                    "north central": abbrev_to_state("wi, mi, il, in, oh, ky"),
                    "north midland": abbrev_to_state("ne, sd, ia, mo, il, in, oh, wv, pa, md, de, nj"),
                    "northeast": abbrev_to_state("pa, nj, ny, vt, nh, ma, ct, me, ri"),
                    "northwest": abbrev_to_state("wa, or, id, mt, wy"),
                    "ohio valley": abbrev_to_state("il, mo, ky, in, oh"),
                    "okefenokee": abbrev_to_state("ga, fl"),
                    "ozarks": abbrev_to_state("mo, ok, ar"),
                    "pacific": abbrev_to_state("wa, or, ca"),
                    "pacific northwest": abbrev_to_state("wa, or, ca"),
                    "plains states": abbrev_to_state("co, ks, ne"),
                    "rocky mountains": abbrev_to_state("id, mt, wy, co, ut, nv"),
                    "smoky mountains": abbrev_to_state("tn, nc"),
                    "south": abbrev_to_state("tx, la, ms, al, fl, ga, nc, sc, va, dc, md"),
                    "south atlantic": abbrev_to_state("nc, ga, sc, fl"),
                    "south midland": abbrev_to_state("ok, mo, ar, la, ms, il, in, ky, tn, al, oh, wv, va, nc, ga, dc, md, de, sc"),
                    "southeast": abbrev_to_state("ms, tn, al, nc, ga, fl, sc"),
                    "southwest": abbrev_to_state("az, nm, tx, ca, ok"),
                    "upper midwest": abbrev_to_state("nd, sd, ne, mn, ia"),
                    "upper mississippi valley": abbrev_to_state("mn, ia, mo, wi, il"),
                    "west": abbrev_to_state("wa, or, ca, nv, az, id, ut, nm, mt, wy, co, ok, tx, nd, sd, ne, ks, ok"),
                    "west midland": abbrev_to_state("sd, ne, ia, mo, ok, ar, la, ms, il, in, oh, ky, tn, al, wv, va, nc, sc")
                   }
    return regions
