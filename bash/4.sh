#!/bin/bash

planet=$1

case $planet in
        "Mercury") echo "0" ;;
        "Venus") echo "0" ;;
        "Earth") echo "1" ;;
        "Mars") echo "2" ;;
        "Jupiter") echo "98" ;;
        "Saturn") echo "83" ;;
        "Uranus") echo "27" ;;
        "Neptune") echo "14" ;;
        *)
                echo "Unknown planet" 
                exit 1
                ;;
esac
