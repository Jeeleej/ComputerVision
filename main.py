from ultralytics import YOLO
import cv2
from sort import Sort
import numpy as np

model = YOLO('yolov8n.pt')

#Image Detection

#img = cv2.imread('car_image_1.jpg')
#results = model(img)
#annotated_frame = results[0].plot()
#cv2.imshow("Detection", annotated_frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cap = cv2.VideoCapture("car_video.mp4")

ret, frame = cap.read()
h, w = frame.shape[:2]

mask = cv2.imread("mask.png", 0)
mask = cv2.resize(mask, (w, h))

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
count_line = [600, 600, 1500, 600]
totalCount = []

while True:
    success, frame = cap.read()
    if not success:
        break
    print(frame.shape)
    print(mask.shape)
     # detection array initialize
    detection = np.empty((0, 5))

    # apply mask
    imgRegion = cv2.bitwise_and(frame, frame, mask=mask)

    results = model(imgRegion, stream=True)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            if label in ['car', 'truck', 'bus', 'motorcycle']:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                #cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                current = np.array([x1, y1, x2, y2, conf])
                detection = np.vstack((detection, current))

    # press q to quit
    #if cv2.waitKey(0) & 0xFF == ord('q'):
    #    break

    # tracking
    resultTracker = tracker.update(detection)
    cv2.line(frame, (count_line[0], count_line[1]), (count_line[2], count_line[3]), (0, 0, 255), 5)
    for x1, y1, x2, y2, _id in resultTracker:
        x1, y1, x2, y2, _id = map(int, (x1, y1, x2, y2, _id))

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        cv2.rectangle(frame, (x1, y1), (x2, y2),
                      (255, 0, 255), 2)

        cv2.putText(frame, f"ID: {_id}",
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0), 2)

        cv2.circle(frame, (cx, cy),
                   5,
                   (255, 0, 255),
                   cv2.FILLED)

        if count_line[0] < cx < count_line[2] and count_line[1]-15 < cy < count_line[3]+15:
            if _id not in totalCount:
                totalCount.append(_id)
                cv2.line(frame, (count_line[0], count_line[1]), (count_line[2], count_line[3]), (0, 255, 0), 5)

    cv2.putText(frame, f"Count: {len(totalCount)}",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 255, 255), 4)
    
    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
