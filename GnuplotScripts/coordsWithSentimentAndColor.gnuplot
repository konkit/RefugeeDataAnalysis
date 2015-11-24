set terminal png size 1680,1080 enhanced font "Helvetica,20"
set output 'coordsWithSentimentInColor.png'
set palette model RGB defined ( -1 'red', 1 'green' )
plot 'world_110m.txt' with lines lt rgb 'black', 'coordsWithSentiment.dat' using 3:4:5 with points palette
