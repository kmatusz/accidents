import numpy as np

lum_map = {
    '1': 'Full day',
    '2': 'Twilight or dawn',
    '3': 'Night without public lighting',
    '4': 'Night with public lighting not lit',
    '5': 'Night with public lighting on'
}

agg_map = {
    '1': 'Out of agglomeration',
    '2': 'In built-up areas'
}
# Characteristics.csv

int_map = {
    '1': 'Out of intersection',
    '2': 'Intersection in X',
    '3': 'Intersection in T',
    '4': 'Intersection in Y',
    '5': 'Intersection with more than 4 branches',
    '6': 'Giratory',
    '7': 'Place',
    '8': 'Level crossing',
    '9': 'Other intersection'
}

atm_map = {
    '1': 'Normal',
    '2': 'Light rain',
    '3': 'Heavy rain',
    '4': 'Snow - hail',
    '5': 'Fog - smoke',
    '6': 'Strong wind - storm',
    '7': 'Dazzling weather',
    '8': 'Cloudy weather',
    '9': 'Other'
}

col_map = {
    '1': 'Two vehicles - frontal',
    '2': 'Two vehicles - from the rear',
    '3': 'Two vehicles - by the side',
    '4': 'Three vehicles and more - in chain',
    '5': 'Three or more vehicles - multiple collisions',
    '6': 'Other collision',
    '7': 'Without collision'
}

gps_map = {
    'M': 'Métropole',
    'A': 'Antilles (Martinique or Guadeloupe)',
    'G': 'Guyane',
    'R': 'Réunion',
    'Y': 'Mayotte'
}

# Users.csv

catu_map = {
    '1': 'Driver',
    '2': 'Passenger',
    '3': 'Pedestrian',
    '4': 'Pedestrian in rollerblade or scooter'
}

grav_map = {
    '1': 'Unscathed',
    '2': 'Killed',
    '3': 'Hospitalized wounded',
    '4': 'Light injury'
}

sexe_map = {
    '1': 'Male',
    '2': 'Female'
}

secu_map = {
    '1': 'yes',
    '2': 'no',
    '3': np.nan
}

actp_map = {
    '0': 'not specified or not applicable',
    '1': 'Meaning bumping vehicle',
    '2': 'Opposite direction of the vehicle',
    '3': 'Crossing',
    '4': 'Masked',
    '5': 'Playing - running',
    '6': 'With animal',
    '9': 'Other'
}

etatp_map = {
    '1': 'Only',
    '2': 'Accompanied',
    '3': 'In a group'
}


# Places.csv

catr_map = {
    '1': 'Highway',
    '2': 'National Road',
    '3': 'Departmental Road',
    '4': 'Communal Way',
    '5': 'Off public network',
    '6': 'Parking lot open to public traffic',
    '9': 'other'
}

circ_map = {
    '1': 'One way',
    '2': 'Bidirectional',
    '3': 'Separated carriageways',
    '4': 'With variable assignment channels'
}


vosp_map = {
    '1': 'Bike path',
    '2': 'Cycle Bank',
    '3': 'Reserved channel'
}

prof_map = {
    '1': 'Dish',
    '2': 'Slope',
    '3': 'Hilltop',
    '4': 'Hill bottom'
}

plan_map = {
    '1': 'Straight part',
    '2': 'Curved on the left',
    '3': 'Curved right',
    '4': 'In "S"'
}


surf_map = {
    '1': 'normal',
    '2': 'wet',
    '3': 'puddles',
    '4': 'flooded',
    '5': 'snow',
    '6': 'mud',
    '7': 'icy',
    '8': 'fat - oil',
    '9': 'other'
}

infra_map = {
    '1': 'Underground - tunnel',
    '2': 'Bridge - autopont',
    '3': 'Exchanger or connection brace',
    '4': 'Railway',
    '5': 'Carrefour arranged',
    '6': 'Pedestrian area',
    '7': 'Toll zone'
}

situ_map = {
    '1': 'On the road',
    '2': 'On emergency stop band',
    '3': 'On the verge',
    '4': 'On the sidewalk',
    '5': 'On bike path'
}
