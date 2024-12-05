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
|-----|-----------------------------------------------------------|
|개발환경 / 언어|     <img src="https://img.shields.io/badge/Ubuntu 22.04-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/VS Code-3E8DCC?style=for-the-badge&logo=coderwall&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/ROS2-22314E?style=for-the-badge&logo=ros&logoColor=white"> &nbsp; <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">  | 
|DataBase / GUI     |                    |
|     |                    |

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

## 4. Trash Bot Demo
### 4.1 로봇  호출 기능 (24p)

### 4.2 ArUco Marker Align

