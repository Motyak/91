#!/usr/bin/env bash

function S0 {
    cat <<'EOF'
for i in range(1, 45 +1):
    print(i)
EOF
}

function S1 {
    cat <<'EOF'
import sys

def sum_of_digits(n):
    return sum(int(c) for c in str(n))

for i in sys.stdin:
    i = int(i)
    if i % 10 == 0 or sum_of_digits(i) >= 10:
        i = 91 - i
    print(i)
EOF
}

function S2 {
    cat <<'EOF'
import sys

for i in sys.stdin:
    i = int(i)
    i *= 11
    print(i)
EOF
}

# python3 <(S0) | python3 <(S1) | python3 <(S2)

FIRST_STEP="true"
[ $# -ge 1 ] && { label=$1; shift; }
case ${label:-all} in
    all) ;&

    S0) args=("$@"); shift $#
        #~ S0 ~#
        [ ${#args[@]} -ge 1 ] && { mode=$args[0]; args=("${args[@:1]}"); }
        case ${mode:-~} in
            #TODO:
        esac

        if [ ${#args[@]} -ge 1 ]; then
            res="$(cat)"
        fi
        res="$(python3 <(S0))"
        FIRST_STEP="false"
    ;&

    S1) args=("$@"); shift $#
        #~ S1 ~#
        if $FIRST_STEP; then
            res="$(cat)"
        fi
        res="$(python3 <(S1) <<< "$res")"
        FIRST_STEP="false"
    ;&

    S2) args=("$@"); shift $#
        #~ S2 ~#
        if $FIRST_STEP; then
            res="$(cat)"
        fi
        res="$(python3 <(S2) <<< "$res")"
        FIRST_STEP="false"
    ;&

    ~finally)
        echo "$res"
    ;&

    $'\0') ;;
    *) >&2 echo "Invalid label: \`$label\`"; exit 1 ;;
esac
