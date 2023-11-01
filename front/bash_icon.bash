mkdir Icons
while read -r filename; do
    mv "$filename" Icons/
done < icons.txt
