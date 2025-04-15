from yolov5.detect import run

run(
    weights='yolov5/runs/train/exp/weights/best.pt',  # path to your trained weights
    source='C:\Users\rsuma\Downloads\currencyproject\Test',  # folder or single image
    conf_thres=0.25,  # confidence threshold
    imgsz=640  # image size
)
