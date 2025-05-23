
<<<<<<< Updated upstream
=======
input_dir="$1"


if [[ ! -d "$input_dir" ]]; then
    echo "Error: '$input_dir' is not a valid directory."
    exit 1
fi


for item in "$input_dir"/*; do
    if [[ -d "$item" ]]; then
        name=$(basename "$item")
        count=$(ls -1A "$item" | wc -l)
        echo "$count" > "${input_dir}/${name}.txt"
    fi
done

>>>>>>> Stashed changes
