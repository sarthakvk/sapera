#this script is for running the updater.py
#to update the list of algorithms we have in data/.list-of-algorithms

python3 "$1"/sapera/scraper/updater.py &>/dev/null &#running updater.py

while ps | grep $! &>/dev/null; do #This is a simple progress bar thread
  printf .
  sleep 0.1
done

echo " Done" #prints done when updating the list is done
