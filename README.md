# ros-repo-5
파이널 프로젝트 5조 저장소. 사무실 쓰레기 수거 로봇

## 1. 개요
![preview_img](https://github.com/user-attachments/assets/12dd4860-07f0-460c-ad9a-2eabc95e4190)

### 1.1 프로젝트 소개

- Trash Bot의 사무실 쓰레기 수거 자동화 및 이와 관련된 작업 호출, 할당 등울 통해 사무실 실내 청결 관리를 자동화 할 수 있는 시스템.

### 1.2 조원 소개 및 역할

|이름 | 맡은 역할 |
|-----------|--------------------------------------------|
|강지훈(팀장)| &#8226; DB 구조 설계 <br> &#8226; Path planning 설계 및 구현 <br> &#8226; 다중로봇 충돌 방지 설계 및 구현 |
|서성혁| &#8226; 시스템 구성도 설계 <br> &#8226; YOLOv8 Model 생성 <br> &#8226; ROS 통신을 활용한 중앙제어 시스템 구현 |
|김정현| &#8226; 기능리스트 설계 <br> &#8226; TaskManager Job 관리/배분 기능 구현 <br> &#8226; 로봇 예상 도착시간 계산 구현 |
|김제백| &#8226; Hardware 설계 및 제작 <br> &#8226; Aruco Marker를 이용한 로봇 위치 보정 <br> &#8226; 딥러닝 인식 객체 회피 동작 |

### 1.3 기술스택 

|분류| 사용기술|
|:-----:|-----------------------------------------------------------|
|개발환경 / 언어|     <img src="https://img.shields.io/badge/Ubuntu 22.04-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/VS Code-3E8DCC?style=for-the-badge&logo=VS Code&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/ROS2-22314E?style=for-the-badge&logo=ros&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">  | 
|DataBase / GUI     | <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/PyQt5-7FFF00?style=for-the-badge&logo=PyQt5&logoColor=white"> |
|Network | <img src="https://img.shields.io/badge/ROS2-000000?style=for-the-badge&logo=ROS2&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/TCP / IP-DC143C?style=for-the-badge&logo=TCP / IP&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/Socket-C93CD7?style=for-the-badge&logo=socket&logoColor=white">                  |
|Hardware| <img src="https://img.shields.io/badge/Arduino Mega 2560-00878F?style=for-the-badge&logo=arduino&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/RasberryPi 4-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white"> |
|Cooperation Tool|<img src="https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/CONFLUENCE-172B4D?style=for-the-badge&logo=confluence&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/JIRA-0052CC?style=for-the-badge&logo=jira&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/SLACK-4A154B?style=for-the-badge&logo=slack&logoColor=white"> |

### 1.4 프로젝트 기간 : 2024. 10. 28 ~ 2024. 11. 25



## 2 System Design

### 2.1 System Requirements

![image](https://github.com/user-attachments/assets/cc850fba-3d1f-44ad-8e9f-a90d64d4023b)

### 2.2 System Architecture
![image](https://github.com/user-attachments/assets/ad412b3f-c0e8-423e-af00-5548f3c1e194)

### 2.3 DB설계
![image](https://github.com/user-attachments/assets/afb0002a-589e-4856-99a9-224e9d044c2c)

### 2.4 Robot Hardware
![image](https://github.com/user-attachments/assets/ab0772fa-7e07-49df-855f-9f118a685284)
![image](https://github.com/user-attachments/assets/950418fd-2e82-48ec-ab5f-e6e0b3f0f777)

### 2.5 Deeplearning Recognition Objects
![image](https://github.com/user-attachments/assets/ab67711c-25e5-4fff-a896-5023a671fbfd)

### 2.6 Map
![image](https://github.com/user-attachments/assets/6c42a2a8-a8e1-4742-9683-c510ea62ceb0)

## 3. GUI 
### 3.1.1 USER / Admin GUI
![image](https://github.com/user-attachments/assets/b8f66e4c-6509-4a59-a789-78c0c75ee1ac)

### 3.1.2 Admin GUI Map 
**①탭을 이동하는 버튼 / ②로봇의 상태 관찰 / ③job의 상태 관찰 / ④job 호출과 로봇의 움직임 관찰**
![image](https://github.com/user-attachments/assets/bafd7d16-02f5-4bd1-ae09-5124318ae3e3)

### 3.1.3 Admin GUI Log
**①검색사항 선택 / ②로그 기록**
![image](https://github.com/user-attachments/assets/76de3caf-6358-4598-a13a-8a599fc2d11a)
![log](https://github.com/user-attachments/assets/28d4e8e8-c453-4caf-af9d-3a2d03329d58)

## 4. Trash Bot Demo
### 4.1.1 로봇  호출 기능
![5번까지-주행영상_ui](https://github.com/user-attachments/assets/7ebab6c2-ffe7-46f0-a3f2-c15303c521e5)

### 4.1.2 로봇 호출 영상
https://github.com/user-attachments/assets/7b24fdc3-e9ef-4a6a-8804-35cd1d231945

### 4.2.1 ArUco Marker 좌표계 설명
![image](https://github.com/user-attachments/assets/ca9baf15-aa7c-43e1-8d06-d955771b0d2c)

### 4.2.2 ArUco Marker Align 영상 - 1
![ArUco (1)](https://github.com/user-attachments/assets/16243610-7404-45e5-9738-19a807f38f72)


### 4.2.2 ArUco Marker Align 영상 - 2 
https://github.com/user-attachments/assets/e12e8129-2658-43be-afa5-ad095183cda9

### 4.3 쓰레기 수거 영상
![쓰레기수거영상](https://github.com/user-attachments/assets/060438d4-1585-4b2f-83e3-f91aea4c5752)


### 4.4 쓰레기 수거 후 충전소 복귀
![쓰레기수거후충전소복귀](https://github.com/user-attachments/assets/76b3b245-5b51-4324-b614-b533d7f53d82)

### 4.5 수거함이 가득찼을 때 쓰레기장 이동 (30p)

## 5. DeepLearning
### 5.1 딥러닝 인식 객체
![image](https://github.com/user-attachments/assets/1f134a1c-65ee-45f2-9176-30d28808145e)

### 5.2 목적지 도착 후 쓰레기통이 없을 때 충전소 복귀 영상 - 1(32p)


### 5.3 목적지 도착 후 쓰레기통이 없을 때 충전소 복귀 영상 - 1
![쓰레기수거후충전소복귀](https://github.com/user-attachments/assets/3d0265a0-a992-47b7-9c34-326abc8814e1)


### 5.4 움직이는 사람 인식 시 TrashBot 정지 영상
![쓰레기수거후충전소복귀](https://github.com/user-attachments/assets/0a59d332-f2f2-4a36-a689-97f6c6aa5870)


### 5.5 멈춰있는 사람 인식 시 TrashBot 회피 영상 (35p)


## 6. 다중 로봇 제어
### 6.1 로봇 2대 작업 영상 - 1 (39p)


### 6.2 로봇 2대 작업 영상 - 2 (40p)


### 6.3 로봇간 충돌 방지 영상 (36p)
