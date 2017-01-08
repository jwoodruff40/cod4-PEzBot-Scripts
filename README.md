# cod4-PEzBot-Scripts
Two python scripts to aid in creating/converting waypoint files for the popular PEzBot mod for CoD 4: Modern Warfare.

ConvertWP converts the standard PEzBot mp_mapname_waypoints.gsc file to the mapname.gsc file used in Bot Warfare mod (based on PEzBot with improvements).

ConvertWPLog reads the games_mp.log file generated after using PEzBot/Bot Warfare's waypoint generator, finds the newest instances of waypoints for a given map, and converts the log output into a usable mapname.gsc file for use with Bot Warfare. It then zips the file into the Bot Warfare .iwd archive. It can be easily adapted for the original PEzBot format however.

Scripts should be run from the directory containing the file to be converted.
