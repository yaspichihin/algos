import random


# Упрощенная сортировка по корзинам.
# Тут сортируются только числа, нет
# привязки к их владельцам (ученики).
def bucket_sort(scores):

    # Создаем 100 корзин для оценок.
    buckets = [[] for _ in range(101)]

    # Раскидываем оценки по корзинам.
    for score in scores:
        buckets[score].append(score)

    sorted_scores = []
    for bucket in buckets:
        sorted_scores.extend(bucket)

    return sorted_scores

if __name__ == "__main__":

    # В классе 30 учеников с оценками от 0 до 100.
    scores = [random.randint(0, 100) for _ in range(30)]
    assert bucket_sort(scores) == sorted(scores), "Ошибка сортировки"
