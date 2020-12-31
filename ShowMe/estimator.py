# -*- coding: utf-8 -*-
import torch
import torchvision.models
import torchvision.transforms as transforms
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def img2tensor(image):
    """Convert PIL image to PyTorch tensor.
    """
    if image.mode != 'RGB':
        image = image.convert("RGB")

    Transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            ])
    image = Transform(image)
    image = image.unsqueeze(0)
    return image.to(device)


def fetch_model():
    """Return a Resnet-50 model.
    """
    model = torchvision.models.resnet50()
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load('model/model-resnet50.pth', map_location=device))
    return model


def inference(image_path: str) -> float:
    """Predict an image's popularity.
    """

    image = Image.open(image_path)
    image = img2tensor(image)
    model = fetch_model()
    model.eval().to(device)

    with torch.no_grad():
        preds = model(image)

    return preds.item()
