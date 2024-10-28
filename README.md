
# PeopleCountAnalytics

# People Count Analytics

## Project Overview
This repository contains the code for an innovative people counting system designed to analyze videos uploaded by users. Utilizing Python with Flask as the backend framework, it allows users to define specific areas within their videos for analysis. The analytical engine is powered by YOLOv3 (You Only Look Once version 3), ensuring accurate real-time object detection. For seamless user interaction, React has been employed as the frontend technology.

## Features
- Video upload functionality allowing users to provide their own footage.
- Custom area selection tool enabling targeted analysis within videos.
- Integration of YOLOv3 for cutting-edge object detection and analytics.
- Interactive frontend designed with React for optimal user experience.

## How It Works
1. Users upload their video files.
2. Using our custom tool, they draw areas on their videos where they want to count people.
3. Our system processes these selected areas using YOLOv3 to accurately detect individuals.
4. Results are displayed through our React-based frontend interface.

## Installation & Setup

For installation, you'll need to set up the backend. Follow these commands:

1. ```
    cd back_end
    ```

2. ```
   pip install -r requirements.txt
   ```

## Usage

To run the backend, execute the following command:

1. ```
    cd back_end
    ```

2. ```
   python main.py
   ```

After running the listed commands, you can start the frontend. Execute the following commands:

1. ```
    cd ..
    ```

2. ```
    cd yolo-person-counter
    ```

3. ```
   npm start
```

>>>>>>> 775708c (Removendo sub-repositório yolo-person-counter)
