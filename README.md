# Intruscan
IntruScan is a real-time intrusion detection system built with Python and OpenCV. It monitors live video to detect motion and identifies unauthorized entries. Integrated with Twilio API, it instantly sends alert SMS notifications, offering a smart and affordable solution for home and office security.


🚨 IntruScan – Real-Time Intrusion Detection System

Technologies: Python | OpenCV | Twilio API

IntruScan is a real-time intrusion detection and alerting system built using Python and OpenCV. The application continuously monitors a video feed (live camera or pre-recorded) to detect suspicious motion. When any unauthorized movement is identified, the system automatically triggers an instant SMS alert to the user via the Twilio API.

🔍 Key Features

-📹 Real-time Motion Detection using OpenCV (cv2)
-⚠️ Smart Intrusion Detection via frame differencing / contour analysis
-📲 Instant SMS Notifications using Twilio API
-🖥️ Lightweight & Easy Deployment on desktop or single-board systems (e.g., Raspberry Pi)
-🧩 Customizable Alert Logic and sensitivity tuning

🛠️ How It Works

1.The camera feed is continuously captured and processed frame-by-frame.
2.OpenCV compares current and previous frames to detect movement.
3.When motion exceeds a defined threshold, an intrusion event is triggered.
4.Twilio API sends an alert with location/time details to the registered phone number.

🎯 Applications

-Home & Office Security
-Restricted Zone Monitoring
-ATM & Store Surveillance
-Smart IoT-based Safety Systems
