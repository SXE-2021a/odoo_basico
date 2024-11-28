#https://www.odoo.com/forum/help-1/question/how-to-import-images-for-products-in-binary-to-the-database-1868
echo \"External ID\",\"foto\" > $2
while IFS="|" read f1 f2; do
echo -n $f1, >> $2
#If second column represents the picture's filename (not the key), please use this command
cat "$(echo ${f2} | tr -d '\r' | tr -d '"')" | base64 --wrap=0 >> $2

#If second column represents the key to match with the filename, please use this command
#cat $(echo ${f2} | tr -d '\r' | tr -d '"').jpg | base64 --wrap=0 >> $2
#Carrier return at end of line
echo >> $2
done < $1
