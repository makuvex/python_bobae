#!/bin/bash

read -p "커밋 메시지 입력: " msg
echo "$msg"


if [ -z "$msg" ]; then
    echo "커밋 메시지를 작성해주세요."
else
    echo "asdzzzz [${msg}]"
fi

