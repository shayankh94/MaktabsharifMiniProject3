mkdir Icons
while read -r filename; do
    mv "images/$filename" Icons/
done < icons.txt
