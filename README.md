# python_bobae
python_bobae

- ncp_setting -
NCP 공인 ip : 27.96.135.53
ssh -l root -p 5000 106.10.32.149

- docker -
- 도커에 우분투 설치 : docker run ubuntu:16.04
- 도커 컨테이너 삭제 : docker rm (컨테이너 id) -f
- 도커 이미지 삭제 : docker rmi (이미지 id)

. 이번에는 /bin/bash 명령어를 입력해서 ubuntu:16.04 컨테이너를 실행
- docker run --rm -it ubuntu:16.04 /bin/bash

//////////////////////////////////////////////////////////////

python 2.7에서 python3으로 업데이트(https://www.whatwant.com/945)
- sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
- update-alternatives --config python
$ python --version
- Python 3.7.5
