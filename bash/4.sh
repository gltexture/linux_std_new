#!/bin/bash

planet=$1

case $planet in
    	"Mercury") echo "Mercury - 0 moons" ;;
   	"Venus") echo "Venus - 0 moons" ;;
    	"Earth") echo "Earth - 1 moon" ;;
    	"Mars") echo "Mars - 2 moons" ;;
   	"Jupiter") echo "Jupiter - 79 moons" ;; 
	"Saturn") echo "Saturn - 82 moons" ;;
    	"Uranus") echo "Uranus - 27 moons" ;;
    	"Neptune") echo "Neptune - 14 moons" ;;
    	*) echo "Error: Planet $planet does not exist." ;;
esac
