#!/usr/bin/env fish

set --function val 10.0
set --function id SENSOR-(random 1000 9999)
while true
    sleep 0.(random 1 9)
    set --function offset 0.(random 0 7)
    set --function rand (random 0 1)

    if [ $val -lt -10 ] || [ $rand = 0 ]
        set --function val (math $val + $offset)
    else if [ $val -gt 45 ] || [ $rand = 1 ]
        set --function val (math $val - $offset)
    end

    if [ (random 0 25) = 0 ] # Random noise
        echo $id (date -Ins) (math "$val + ("(random 0 6).0" - 3.0)")
    else
        echo $id (date -Ins) $val
    end
end

