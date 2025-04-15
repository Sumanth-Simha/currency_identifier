# Currency Classifier using YOLOv5

This project uses YOLOv5 to classify and detect different currency denominations.

## Structure
- `dataset/` – contains labeled images and YAML config
- `yolov5/` – YOLOv5 model and training code
- `test_images/` – images used to test trained model
- `currency.yaml` – dataset definition

## How to Train
```bash
python yolov5/train.py --img 640 --batch 16 --epochs 50 --data dataset/currency.yaml --weights yolov5s.pt --name currency_model
