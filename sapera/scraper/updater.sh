python3 $1/sapera/scraper/updater.py &> /dev/null &
s='s'
while ps | grep $! &>/dev/null; do
    printf .
    sleep 0.1
done
echo " Done"