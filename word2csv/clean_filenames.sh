#! /bin/bash
cd "/home/bhervy/Temp/Donnees"
for file in *.html; do
    filename=${file%.*}
    file_clean=`echo $filename | tr -cs "[a-zA-Z0-9éèàôçîêâ-]_" _ `
    final="$file_clean.html"
    mv -n "$file" "$final"
    #mv "$file" "$(echo $file | sed -e 's/ô/o/g' | sed -e 's/[^A-Za-z0-9._-éè,\\'']/_/g')"
done
cd ..
