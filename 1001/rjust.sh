#!/usr/bin/env bash

set -o errexit -o nounset
#set -o xtrace #debug

function fail {
    local msg="$1"
    >&2 echo "$msg"
    exit 1
}

function validation_err {
    local var="$1"
    fail "Required \$$var but invalid: \`${!var}\`"
}

function maxw {
    awk '{ if (length > maxw) { maxw=length } } END { print maxw }'
}

function rjust {
    local width=${1:-}
    local stdin="$(< /dev/stdin)"
    [ -z "$width" ] && width="$(maxw <<< "$stdin")"
    [[ "$width" =~ [0-9]+ ]] || validation_err "width"
    while IFS= read -r line; do
        local line_len=${#line}
        local required_spaces=$((width - line_len))
        for ((i = 1; i <= $required_spaces; ++i)); do
            echo -n " "
        done
        echo "$line"
    done <<< "$stdin"
}

if [ "${BASH_SOURCE[0]}" == "$0" ]; then rjust $@; fi
