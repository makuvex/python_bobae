# python_bobae
python_bobae

- ncp_setting -
NCP 공인 ip : 27.96.135.53

ssh -l root -p 5000 106.10.32.149

- 도커에 우분투 설치 : docker run ubuntu:16.04
- 도커 컨테이너 삭제 : docker rm (컨테이너 id) -f
- 도커 이미지 삭제 : docker rmi (이미지 id)

. 이번에는 /bin/bash 명령어를 입력해서 ubuntu:16.04 컨테이너를 실행
- docker run --rm -it ubuntu:16.04 /bin/bash

mysql root 암호 - malice77
. mysql 설치
docker run -d -p 3306:3306 \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
  --name mysql \
  mysql:5.7
