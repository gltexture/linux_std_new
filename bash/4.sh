#!/bin/bash

planet=$1

case $planet in
        "Mercury") echo "Mercury-0" ;;
        "Venus") echo "Venus-0" ;;
        "Earth") echo "Earth-1" ;;
        "Mars") echo "Mars-2" ;;
        "Jupiter") echo "Jupiter-98" ;;        
        "Saturn") echo "Saturn-83" ;;
        "Uranus") echo "Uranus-27" ;;
        "Neptune") echo "Neptune-14" ;;
        *) echo "Unknown planet" ;;
esac
