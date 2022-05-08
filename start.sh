#!/bin/bash
#
# bot起動スクリプト
# 
# Usage:
# 
# '''bash
# bash start.sh
# '''


set -eu


function main() {
  python src/main/main.py
}

pushd `dirname "$0"` > /dev/null
main
popd > /dev/null
