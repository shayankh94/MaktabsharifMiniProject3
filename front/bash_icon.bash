while read -r filename; do
    mv "images/$filename" Icons/
done < url_file.txt
