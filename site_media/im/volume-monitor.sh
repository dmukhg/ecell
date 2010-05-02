while true
do
    if [ -S ~/.awesome_ctl.0 ]; then
        while true
        do
            . ~/.awesome/volume_update.sh

            sleep $speed
        done
    else
        sleep 1
    fi
done
