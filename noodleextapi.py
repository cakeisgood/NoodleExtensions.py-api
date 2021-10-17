import random
import noodleextensions_com
from noodleextensions_com import *




class get:
    mappers=(api.noodleextensions.com.mappers.__mappers__)

    mappers_random_list=(api.noodleextensions.com.mappers.__mappers_random_list__)
    random_mapper=(random.choice(mappers_random_list))
    
    noodle_maps=(api.noodleextensions.com.maps.__maps_rand_list__)

    class maps:
        random_noodle_map=(random.choice(api.noodleextensions.com.maps.__maps_rand_list__))


class github:



    class noodle:
        latest=("https://github.com/Aeroluna/NoodleExtensions/releases/latest")



class discord_noodle:
    class noodleapi:     
        def rand_mapper():
            noodle_com_api_rand_mapper_list=(api.noodleextensions.com.mappers.__mappers_random_list__)
            noodle_com_api_rand_mapper=(random.choice(noodle_com_api_rand_mapper_list))
            return (noodle_com_api_rand_mapper)

        def rand_map():
            noodle_com_api_rand_map_list=(api.noodleextensions.com.maps.__maps_rand_list__)
            noodle_com_api_rand_map=(random.choice(noodle_com_api_rand_map_list))
            return (noodle_com_api_rand_map)