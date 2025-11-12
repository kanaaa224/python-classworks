import cv2
import numpy as np
import os

IMG_PATH = os.path.join(os.path.dirname(__file__), 'image.jpg')

# === 無処理コールバック ===
def nothing(x):
    pass

# === ウィンドウ生成 ===
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.createTrackbar('minR', 'image', 0, 255, nothing)
cv2.createTrackbar('maxR', 'image', 255, 255, nothing)
cv2.createTrackbar('minG', 'image', 0, 255, nothing)
cv2.createTrackbar('maxG', 'image', 255, 255, nothing)
cv2.createTrackbar('minB', 'image', 0, 255, nothing)
cv2.createTrackbar('maxB', 'image', 255, 255, nothing)

# === 画像読み込み ===
img = cv2.imread(IMG_PATH)

if img is None:
    raise FileNotFoundError(f'画像が見つかりません: {IMG_PATH}')

# === カラー範囲のリスト ===
filters = [] # 各要素: (low, high)

print("""
--------------------------------------------------
スライダーで RGB の範囲を調整
s: 現在の範囲を保存（フィルタ追加）
c: すべてのフィルタをクリア
q: 終了
--------------------------------------------------
""")

while True:
    # スライダー値取得
    minR = cv2.getTrackbarPos('minR', 'image')
    maxR = cv2.getTrackbarPos('maxR', 'image')
    minG = cv2.getTrackbarPos('minG', 'image')
    maxG = cv2.getTrackbarPos('maxG', 'image')
    minB = cv2.getTrackbarPos('minB', 'image')
    maxB = cv2.getTrackbarPos('maxB', 'image')

    # 現在の範囲でマスク生成
    mask_current = cv2.inRange(img, np.array([minB, minG, minR]), np.array([maxB, maxG, maxR]))

    # 保存済みフィルタの合成
    mask_total = mask_current.copy()

    for low, high in filters:
        mask_total |= cv2.inRange(img, np.array(low), np.array(high))

    # 結果表示
    filtered = cv2.bitwise_and(img, img, mask=mask_total)

    cv2.imshow('mask', mask_total)
    cv2.imshow('filtered', filtered)

    key = cv2.waitKey(16) & 0xFF

    # --- 保存キー ---
    if key == ord('s'):
        low = [minB, minG, minR]
        high = [maxB, maxG, maxR]

        filters.append((low, high))

        print(f"✅ フィルタ追加: {low}〜{high} (RGB)")
        print(f"現在のフィルタ数: {len(filters)}")

    # --- クリアキー ---
    elif key == ord('c'):
        filters.clear()
        print("🧹 フィルタをすべて削除")

    # --- 終了キー ---
    elif key == ord('q'):
        break

cv2.destroyAllWindows()