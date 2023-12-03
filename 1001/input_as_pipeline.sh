#!/usr/bin/env bash

[ $# -ge 1 ] && { label=$1; shift; }
case ${label:-all} in
    all) ;&

    S0)
        res="$(./S0.py)"
    ;&

    S1)
        [ -z "$res" ] && res="$(< /dev/stdin)"
        res="$(./S1.py <<< "$res")"
    ;&

    S2)
        [ -z "$res" ] && res="$(< /dev/stdin)"
        res="$(./S2.py <<< "$res")"
    ;&

    $'\0') # finally
        echo "$res"
    ;;

    *) >&2 echo "Invalid label: \`$label\`"; exit 1 ;;
esac
