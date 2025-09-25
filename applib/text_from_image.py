try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import cv2
from time import sleep



class TextFromImage:
    def __init__(self, imagepath: str) -> None:
        self._imagepath = imagepath

    
    def extract(self) -> str:
        # 1. Загружаем изображение
        img = cv2.imread(self._imagepath)

        # 2. Переводим в ч/б (grayscale)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Применяем бинаризацию (выделяем белый текст на фоне)
        _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

        # 4. (опционально) убираем шумы
        thresh = cv2.medianBlur(thresh, 3)

        # 5. Сохраняем промежуточный результат (для проверки)
        cv2.imwrite("processed.png", thresh)

        # 6. Распознаем текст
        text = pytesseract.image_to_string(thresh, lang="rus")
        
        return text

