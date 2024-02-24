# Рамейко Максим, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
def test_order_200():
    track_test = sender_stand_request.search_orders()
    assert track_test.status_code == 200