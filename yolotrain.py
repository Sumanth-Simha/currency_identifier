import multiprocessing
from yolov5.train import run  # Import your training function

# Main entry point
if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')  # Ensure multiprocessing works on Windows

    # Call your YOLOv5 training function
    run(
        img_size=640,
        batch_size=16,
        epochs=10,
        data='currency.yaml',  # Update with your path to YAML
        weights='yolov5s.pt',
        name='currency_train'
    )
