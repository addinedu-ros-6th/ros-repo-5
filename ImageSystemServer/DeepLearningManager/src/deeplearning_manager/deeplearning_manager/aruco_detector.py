import numpy as np
import cv2

class ArucoDetector:
    def __init__(self, camera_matrix, dist_coeffs, marker_length=0.051, axis_length=0.05):
        # ArUco 마커 사전과 파라미터 생성 (기본 DICT_4X4_50 사용)
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
        self.aruco_params = cv2.aruco.DetectorParameters_create()
        self.camera_matrix = camera_matrix
        self.dist_coeffs = dist_coeffs
        self.marker_length = marker_length
        self.axis_length = axis_length

    def detect_and_annotate(self, frame):
        # ArUco 마커 탐지
        corners, ids, _ = cv2.aruco.detectMarkers(frame, self.aruco_dict, parameters=self.aruco_params)
        detected_markers = []

        # 마커가 감지되었을 때 ID와 위치 좌표 표시
        if ids is not None:
            # 3D 위치 좌표 추정을 위해 Pose 계산
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, self.marker_length, 
                                                                  self.camera_matrix, self.dist_coeffs)
            for i, corner in enumerate(corners):
                marker_id = ids[i][0]
                corners_reshaped = corner.reshape((4, 2))
                top_left = (int(corners_reshaped[0][0]), int(corners_reshaped[0][1]))

                # ID와 2D 위치 좌표 표시
                cv2.putText(frame, f"ID: {marker_id}", top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.polylines(frame, [corners_reshaped.astype(int)], True, (0, 255, 0), 2)

                # 중심 좌표 계산
                center_x = int(np.mean(corners_reshaped[:, 0]))
                center_y = int(np.mean(corners_reshaped[:, 1]))

                # 3D 위치 정보 추출
                tvec = tvecs[i][0]
                position_3d = (tvec[0], tvec[1], tvec[2])

                # 카메라와 마커 간 거리 계산
                distance = np.linalg.norm(tvec)

                # 중심 좌표와 3D 위치 및 거리 정보를 detected_markers 리스트에 저장
                detected_markers.append({
                    "id": marker_id,
                    "center_2d": (center_x, center_y),
                    "position_3d": position_3d,
                    "distance": distance
                })

                # 중심 좌표와 3D 위치 정보 및 거리 표시
                cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)
                cv2.putText(frame, f"X: ({position_3d[0]:.2f}, Y: {position_3d[1]:.2f}, Z: {position_3d[2]:.2f})", 
                            (center_x + 10, center_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                cv2.putText(frame, f"Distance: {distance:.2f} m", (center_x + 10, center_y + 40), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # 3D 좌표계 그리기
                cv2.drawFrameAxes(frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i], self.axis_length)

        return frame, detected_markers
